#!/usr/bin/env python3
import cv2
from time import sleep
cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0
instr_list = ["Face forward, look into the camera at 1 elbow distance",
              "Face forward, now look at 2 elbow distance",
              "Move your face up", "Move your face down",
              "Move your face slight right",
              "Move your face slight left"]
for instruction in instr_list:
    print(instruction)
    print("Press Space bar when ready")
    while True:
        ret, frame = cam.read()
        cv2.imshow("test", frame)
        if not ret:
            break
        k = cv2.waitKey(1)
        elif k%256 == 32:
            # SPACE pressed
            for i in range(5):
                # change the directory name appropriately
                img_name = "testing/s1/{}.jpeg".format(img_counter)
                cv2.imwrite(img_name, frame)
                print("{} written!".format(img_name))
                img_counter += 1
            break
print("Training data has been recorded, Thank You")

cam.release()

cv2.destroyAllWindows()
