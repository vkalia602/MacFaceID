#!/usr/bin/env python3
import cv2

camera_port = 0
ramp_frames = 50
image_number = 0
camera = cv2.VideoCapture(camera_port)

def get_image():
    retval, im = camera.read()
    return im
while True:
    retrn, frame = camera.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    cv2.imshow('frame', frame)
'''
instr_list = ["Face forward, look into the camera at 1 elbow distance",
              "Face forward, now look at 2 elbow distance",
              "Move your face up", "Move your face down",
              "Move your face slight right",
              "Move your face slight left"] 
for instruction in instr_list:
    print("{}". format(instruction))
    cv2.imshow('frame', rgb)
    while True:
        key = input("Press 'return' when you are ready \n")
        if key == "":
            print("Taking pictures now...")
            for new_pic in range(5):
                for i in range(ramp_frames):
                    temp = camera.read()
                camera_capture = get_image()
                filename = "testing/s1/{}.jpg".format(image_number)
                cv2.imwrite(filename, camera_capture)
                image_number+=1
            break
        else:
            print("Sorry, I did not get that, Press 'return' when you are ready")
print("Your training data has been recorded, Thank You")
'''
camera.release()
cv2.destroyAllWindows()
