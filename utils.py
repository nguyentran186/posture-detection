import cv2
import mediapipe as mp
import pickle
import numpy as np

model_file = 'model.sav'
clf = pickle.load(open(model_file, 'rb'))

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose
target_lm_idx = [0, 2, 5, 9, 10, 11, 12]

def get_predict(images):
    image = cv2.imread(images)
    with mp_pose.Pose(
        model_complexity=1,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as pose:
        
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = pose.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        mp_drawing.draw_landmarks(
            image,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())

        if results.pose_landmarks is not None:
            # Flip the image horizontally for a selfie-view display.
            lm_result = []
            for lm_idx in target_lm_idx:
                lm_result.append(results.pose_landmarks.landmark[lm_idx].x)
                lm_result.append(results.pose_landmarks.landmark[lm_idx].y)
                lm_result.append(results.pose_landmarks.landmark[lm_idx].z)
                lm_result.append(results.pose_landmarks.landmark[lm_idx].visibility)
            lm_result = np.array(lm_result)[None, :]
            pred = clf.predict(lm_result)[0]
            image = cv2.flip(image, 1)
            if pred == 0:
                prediction = 'Excellent Posture'
            if pred == 1:
                prediction = 'Okay Posture'
            if pred == 2:
                prediction = 'Bad Posture'
            if pred == 3:
                prediction = 'Terrible Posture'

    return image, prediction