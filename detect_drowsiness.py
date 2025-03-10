from scipy.spatial import distance as dist
from imutils.video import VideoStream
from imutils import face_utils
from threading import Thread
import numpy as np
import playsound
import argparse
import imutils
import time
import dlib
import cv2
from imutils.video import WebcamVideoStream


def sound_alarm(path):
    playsound.playsound(path)

# Function to calculate Eye Aspect Ratio
def eye_aspect_ratio(eye):
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    C = dist.euclidean(eye[0], eye[3])

    ear = (A+B) / (2.0*C)
    return ear


ap = argparse.ArgumentParser()
ap.add_argument("-a", "--alarm", type=str, default="",
                help="path alarm .WAV file")
args = vars(ap.parse_args())

# Declare a constant which will work as the threshold for EAR value, below which it will be regared as a blink 
EYE_AR_THRESH = 0.28
# Declare another costant to hold the consecutive number of frames to consider for a blink 
EYE_AR_CONSEC_FRAMES = 48
COUNTER = 0
ALARM_ON = False

# Define the path of the shape predictor model
predictor_path = "shape_predictor_81_face_landmarks.dat"

# Intialize the dlib's face detector model as 'detector' and the landmark predictor model as 'predictor'
print("[INFO] Loading facial landmark predictor....")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)

# Grab the indexes of the facial landamarks for left and right eyes respectively
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]


# Start the video stream and allow the camera to warm-up
print("[INFO] Starting video stream thread...")
vs = WebcamVideoStream(0).start()
time.sleep(0.05)

# Loop over all the frames and detect the faces
while True:
    frame = vs.read()
    frame = imutils.resize(frame, width=600)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 0)

    for rect in rects: 
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]
        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)

        ear = (leftEAR + rightEAR) / 2.0

        leftEyeHull = cv2.convexHull(leftEye)
        rightEyeHull = cv2.convexHull(rightEye)
        cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

        if ear < EYE_AR_THRESH:
            COUNTER += 1

            if COUNTER >= EYE_AR_CONSEC_FRAMES:
                if not ALARM_ON:
                    ALARM_ON = True

                    if args["alarm"] != "":
                        t = Thread(target=sound_alarm,
                                   args=(args["alarm"],))
                        t.daemon = True
                        t.start()

                cv2.putText(frame, "DROWSINESS ALERT!", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        else:
            COUNTER = 0
            ALARM_ON = False

            cv2.putText(frame, "EAR: {:.2f}".format(ear), (300, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break
cam.release()
cv2.destroyAllWindows()

cv2.destroyAllWindows()
vs.stop()
