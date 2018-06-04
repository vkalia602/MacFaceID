#!/usr/bin/env python3
import cv2
from time import sleep
import os
cam = cv2.VideoCapture(0)
cv2.namedWindow("test")
integer = 0
def dialog_box(instruction):
    answer = """
        osascript -e '
            tell application "System Events"
                set result to (display dialog "%s" giving up after 3)
            end tell
'
        """ % (instruction)
    os.system(answer)
img_counter = 0
instr_list = ["Let us collect some training data now",
              "Face forward, look into the camera at 1 arm distance",
              "Face forward, now look at half arm distance",
              "Move your face up",
              "Move your face down",
              "Move your face slight right",
              "Move your face slight left"]
for instruction in instr_list:
    dialog_box(instruction + "\nPlease press Space bar on Camera window when ready")
    while True:
        ret, frame = cam.read()
        cv2.imshow("test", frame)
        if not ret:
            break
        k = cv2.waitKey(1)
#        if integer == 0:
 #           integer += 1
  #          break
        if k%256 == 32:
            # SPACE pressed
            for i in range(5):
                # change the directory name appropriately
                img_name = "testing/s1/{}.jpeg".format(img_counter)
                cv2.imwrite(img_name, frame)
                print("{} written!".format(img_name))
                img_counter += 1
            break
dialog_box("Training data has been recorded, Thank You")

cam.release()

cv2.destroyAllWindows()
