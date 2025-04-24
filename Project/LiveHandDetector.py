import cv2
import numpy as np

from cvzone.HandTrackingModule import HandDetector
import tensorflow as tf
import time


LETTERS = ['A', 'B', 'C', 'D',  'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','del', 'space']
model_path = 'Project/Trained/ASP_2_model_11.keras'

model = tf.keras.models.load_model(model_path,compile=False)

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

            data_to_predict = np.expand_dims(imgCrop,axis=0)
            predicction = model.predict(data_to_predict)
            label_text = LETTERS[np.argmax(predicction)]
            
            cv2.putText(imgCrop, label_text,(0,60),cv2.FONT_HERSHEY_SIMPLEX, 2, (255,0,255),3)
            cv2.imshow('Hand img',imgCrop)
        except:
            pass
    cv2.imshow('Image',img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
