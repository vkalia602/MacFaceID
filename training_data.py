#!/usr/bin/env python3
import cv2
from time import sleep
import os
import numpy as np

cam = cv2.VideoCapture(0)
cv2.namedWindow("Training Pictures")
integer = 0
ramp_frames = 30
def dialog_box(instruction):
    answer = """
        osascript -e '
            tell application "System Events"
                set result to (display dialog "%s" giving up after 3)
            end tell
'
        """ % (instruction)
    os.system(answer)
def get_image():
    retval, im = cam.read()
    return im
def picture():
    for i in range(ramp_frames):
        picture = get_image()
    pic = get_image()
    return pic
img_counter = 0
instr_list = ["",
              "Face forward, look into the camera at 1 arm distance",
              "Face forward, now look at half arm distance",
              "Move your face up",
              "Move your face down",
              "Move your face slight right",
              "Move your face slight left"]
for instruction in instr_list:
#    dialog_box(instruction + "\nPlease press Space bar on Camera window when ready")
    frameWidth = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
    frameHeight = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
    while True:
        ret, frame = cam.read()
        cv2.putText(img = frame, text = instruction,
                    org = (int(frameWidth/6),int(frameHeight) - 100), 
                    fontFace = cv2.FONT_HERSHEY_DUPLEX, 
                    fontScale = 1, 
                    color = (255,0,0),
                    thickness = 2, 
                    lineType = 2)
        cv2.putText(img = frame, text = "Press space bar when ready",
                    org = (int(frameWidth/6),int(frameHeight) - 30), 
                    fontFace = cv2.FONT_HERSHEY_DUPLEX, 
                    fontScale = 1, 
                    color = (255,0,0),
                    thickness = 2, 
                    lineType = 2)
        cv2.imshow("Training Pictures", frame)
        if not ret:
            break
        k = cv2.waitKey(1)
        if integer == 0:
            integer += 1
            break
        if k%256 == 32:
            # SPACE pressed
            for i in range(5):
                # change the directory name appropriately
                pic = picture()
                img_name = "MacFaceID/support/training-data2/s1/{}.jpeg".format(img_counter)
                cv2.imwrite(img_name, pic)
                print("{} written!".format(img_name))
                img_counter += 1
            break
dialog_box("Training data has been recorded, Thank You")
dialog_box("Preparing Training Data, Please Wait!")
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

faces, labels = prepare_training_data("MacFaceID/support/training-data2")
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.train(faces, np.array(labels))
face_recognizer.save("MacFaceID/support/saved_instance2.xml")
dialog_box("Done")
cam.release()
cv2.destroyAllWindows()

