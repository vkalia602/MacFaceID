#!/usr/bin/env python3

import cv2
import numpy as np
import os
print("Preparing Training Data, Please Wait!")
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

faces, labels = prepare_training_data("MacFaceID/testing")
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.train(faces, np.array(labels))
face_recognizer.save("MacFaceID/testing/cascade/saved_instance.xml")
print("Done")
