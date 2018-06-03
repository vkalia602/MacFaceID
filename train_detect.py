#!/usr/bin/env python3
import sys
import os
import cv2
import numpy as np
import support
import matplotlib.pyplot as plt

subjects = ['', 'Sue']

def detect_face(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('MacFaceID/support/opencv-files/haarcascade_frontalface_alt.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    if len(faces) is 0:
        return None, None
    for (x, y, w, h) in faces:
        (x, y, w, h) = faces[0]

    return gray[y:y+w, x:x+h], faces[0]

def prepare_training_data(data_folder_path):
    dirs = os.listdir(data_folder_path)
    faces = []
    labels = []
    for dir_name in dirs:
        if not dir_name.startswith('s'):
            continue

        label = int(dir_name.replace('s', ''))
        subject_dir_path = data_folder_path + "/" + dir_name
        subject_images_names = os.listdir(subject_dir_path)
        for image_name in subject_images_names:
            if image_name.startswith("."):
                continue

            image_path = subject_dir_path + "/" + image_name
            image = cv2.imread(image_path)
            cv2.imshow("training on image...", cv2.resize(image, (400, 500)))
            cv2.waitKey(100)
            face, rect = detect_face(image)

            if face is not None:
                faces.append(face)
                labels.append(label)
    cv2.destroyAllWindows()
    cv2.waitKey(100)
    cv2.destroyAllWindows()
    return faces, labels

print("Preparing data...")
faces, labels = prepare_training_data("MacFaceID/support/training-data")
print("Data Prepared")

face_recognizer = cv2.face.LBPHFaceRecognizer_create()

face_recognizer.train(faces, np.array(labels))
face_recognizer.save("MacFaceID/support/saved_instance.xml")

face_recognizer.read("MacFaceID/support/saved_instance.xml")
def draw_rectangle(img, rect):
      (x, y, w, h) = rect
      cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

def draw_text(img, text, x, y):
      cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)

def predict(test_img):
    if test_img is not None:
        img = test_img.copy()
    else:
        return
    face, rect = detect_face(img)
    try:
        label, confidence = face_recognizer.predict(face)
        print(confidence)
        if confidence > 15.0:
            return None

    except:
        return None
    label_text = subjects[label]
    draw_rectangle(img, rect)
    draw_text(img, label_text, rect[0], rect[1]-5)

    return img

print("Predicting images...")

camera_port = 0 
ramp_frames = 30 
camera = cv2.VideoCapture(camera_port)
def get_image():
     retval, im = camera.read()
     return im 
for i in range(ramp_frames):
    temp = camera.read()

camera_capture = get_image()
filename = "MacFaceID/support/test-data/test1.jpg"
cv2.imwrite(filename,camera_capture)
del(camera)

test_img1 = cv2.imread("MacFaceID/support/test-data/test1.jpg")
predicted_img1 = predict(test_img1)
print("Prediction complete")
if predicted_img1 is None:
    cmd = """ osascript -e 'tell application "System Events"
                        keystroke "wrongpasswordqwerty8477"
                        keystroke return
                        end tell' """
    os.system(cmd)
    print("not a match")
else:
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    
    print("Found Match")
    ax1.imshow(cv2.cvtColor(predicted_img1, cv2.COLOR_BGR2RGB))
    cv2.imshow(subjects[1], predicted_img1)
    cv2.imshow(subjects[1], cv2.resize(predicted_img1, (400, 500)))
    cmd = """ osascript -e 'tell application "System Events"
                        keystroke "bigbang"
                        keystroke return
                        end tell' """
    os.system(cmd)
    os.remove(filename)

cv2.waitKey(1)
cv2.destroyAllWindows()
cv2.waitKey(2)
cv2.destroyAllWindows()
