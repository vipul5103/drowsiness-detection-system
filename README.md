vipul5103: create readme for that project

Workspace: Collecting workspace information# Driver Drowsiness Detection

This project aims to detect driver drowsiness using computer vision techniques. The system monitors the driver's eye aspect ratio (EAR) and yawning to determine if the driver is drowsy and triggers an alarm if necessary.

## Project Structure

```
alarm.wav
detect_drowsiness.py
dlib_face_recognition_resnet_model_v1.dat.bz2
Driver Drowsiness Detection.pptx
Final Project Report.docx
shape_predictor_81_face_landmarks.dat
yawn.py
```

- alarm.wav: The alarm sound file.
- detect_drowsiness.py: The main script for detecting drowsiness.
- dlib_face_recognition_resnet_model_v1.dat.bz2: Pre-trained model for face recognition.
- `Driver Drowsiness Detection.pptx`: Presentation file for the project.
- `Final Project Report.docx`: Final project report document.
- shape_predictor_81_face_landmarks.dat: Pre-trained model for facial landmark detection.
- yawn.py: Script for detecting yawning.

## Requirements

- Python 3.x
- OpenCV
- dlib
- imutils
- numpy
- scipy
- playsound

You can install the required packages using the following command:

```sh
pip install opencv-python dlib imutils numpy scipy playsound
```

## Usage

1. Download the pre-trained models:
   - [shape_predictor_81_face_landmarks.dat](http://dlib.net/files/shape_predictor_81_face_landmarks.dat.bz2)
   - [dlib_face_recognition_resnet_model_v1.dat.bz2](http://dlib.net/files/dlib_face_recognition_resnet_model_v1.dat.bz2)

2. Extract the downloaded models and place them in the project directory.

3. Run the detect_drowsiness.py script:

```sh
python detect_drowsiness.py --alarm alarm.wav
```

## Script Details

### detect_drowsiness.py

This script detects drowsiness by monitoring the Eye Aspect Ratio (EAR) and triggers an alarm if the driver is drowsy.

- **Functions**:
  - `sound_alarm(path)`: Plays the alarm sound.
  - `eye_aspect_ratio(eye)`: Calculates the Eye Aspect Ratio (EAR).

- **Main Logic**:
  - Initializes the dlib face detector and shape predictor.
  - Starts the video stream.
  - Continuously processes video frames to detect faces and calculate EAR.
  - Triggers an alarm if the EAR falls below the threshold for a certain number of consecutive frames.

### yawn.py

This script detects yawning by monitoring the distance between the upper and lower lips.

- **Functions**:
  - `alarm(msg)`: Plays a text-to-speech alarm message.
  - `eye_aspect_ratio(eye)`: Calculates the Eye Aspect Ratio (EAR).
  - `final_ear(shape)`: Calculates the final EAR for both eyes.
  - `lip_distance(shape)`: Calculates the distance between the upper and lower lips.

- **Main Logic**:
  - Initializes the dlib face detector and shape predictor.
  - Starts the video stream.
  - Continuously processes video frames to detect faces and calculate EAR and lip distance.
  - Triggers an alarm if the EAR falls below the threshold or if the lip distance exceeds the yawning threshold.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- [dlib](http://dlib.net/)
- [OpenCV](https://opencv.org/)
- [imutils](https://github.com/jrosebr1/imutils)

For more details, refer to the Final Project Report.docx and Driver Drowsiness Detection.pptx.
