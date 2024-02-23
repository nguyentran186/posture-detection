import cv2
import mediapipe as mp

# Initialize MediaPipe Pose model
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.2, min_tracking_confidence=0.2)

video_path = 'D:\download\ClassroomActivity\ClassroomActivity\Writting_on_Textbook\Writting_on_Textbook_002.mp4'
# For webcam input:

# Open the video file
cap = cv2.VideoCapture(video_path)  # Replace 'video_file.mp4' with the path to your video file

# Check if the video file was opened successfully
if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

# Loop through the frames of the video
while cap.isOpened():
    # Read a frame from the video
    ret, frame = cap.read()

    # Check if the frame was read successfully
    if not ret:
        break

    # Convert the frame to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Perform pose detection on the frame
    results = pose.process(frame_rgb)

    # Draw pose landmarks on the frame
    if results.pose_landmarks:
        for landmark in results.pose_landmarks.landmark:
            cx, cy = int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0])
            cv2.circle(frame, (cx, cy), 5, (0, 255, 0), -1)

    # Display the frame
    cv2.imshow('Video', frame)

    # Check for key press to exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
