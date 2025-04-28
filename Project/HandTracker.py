import cv2
import numpy as np

from cvzone.HandTrackingModule import HandDetector


LETTERS = ['A', 'B', 'C', 'D',  'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','del', 'space']

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)
offset = 70
while True:
    success, img = cap.read()
    hands, img = detector.findHands(img,draw=False,flipType=True)
    if hands:
        hand = hands[0]
        x,y,w,h = hand['bbox']
        try:
            imgCrop = img[
                y-offset:y+h+offset,
                x-offset:x+w+offset
            ]
            imgCrop = cv2.resize(imgCrop,(300,300))
            imgCrop = imgCrop/255
            cv2.imshow('Hand img',imgCrop)

    
        except:
            pass
    cv2.imshow('Image',img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
