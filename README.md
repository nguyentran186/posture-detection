## backend API for hunchback-detection
A lightweight posture classifier using frontal camera images. Provide API for frontend using client-server method with framework Flask of Python.

## Dependencies

- [OpenCV-Python](https://pypi.org/project/opencv-python/)
- [Mediapipe](https://pypi.org/project/mediapipe/)
- [scikit-learn](https://pypi.org/project/scikit-learn/)
- [win10toast](https://pypi.org/project/win10toast/)

## API usage
Run 'api.py', after the Flask finished preparation, frontend framework can call api through socket with port 5000.
The API receives a list of detected keypoints and returns the prediction according to them. 



## Data Collection

Run `datacollect.py`.
Then switch to an 'okay' posture while pressing the key B.
Then switch to an 'bad' posture while pressing the key C.
Then switch to an 'terrible' posture while pressing the key D.
Data instance count will be shown on the terminal. 400 instances for each category works well for me.
After collecting, press Q to exit the program and a `posture_data.npy` file will be saved.

## Model Training
Run `trainclassifer.py` to train the model, a simple scikit-learn LogisticRegression classifier.
The model will be saved as `model.sav`

In addition, train the model through this Colab Notebook for better accuracy: [ML Pipeline](https://colab.research.google.com/drive/1cfj-1tFn-wlGG-8TjCaFIcZm4ENtPy1R?usp=sharing)

## Demo

To see how well your model is, run `predict_demo.py`. The classified posture will be shown as text on screen.

## Further Usage

Run `predict_nofity.py` to use the actual posture remainder program. 
The classifier will run in the background and pop up a Windows notification in the lower right corner 
whenever you are in a bad sitting posture.
