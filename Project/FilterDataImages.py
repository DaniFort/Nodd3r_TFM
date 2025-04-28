import cv2
import os
import random
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import shutil
from datetime import datetime

BASE_PATH = 'ASL_Alphabet_Dataset/asl_alphabet_train'
LETTERS = ['A', 'B', 'C', 'D', 'del', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'space', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
DESTINY_PATH = 'dataset'
IMG_PER_CLASS = 900
OFFSET = 70
detector = HandDetector(maxHands=1)
os.mkdir(os.path.join('dataset','train'))
os.mkdir(os.path.join('dataset','validation'))
os.mkdir(os.path.join('dataset','test'))
for letter in LETTERS:
    t0 = datetime.now()
    os.mkdir(os.path.join('dataset','train',letter,))
    os.mkdir(os.path.join('dataset','validation',letter,))
    os.mkdir(os.path.join('dataset','test',letter))
    imgs = np.array(os.listdir(os.path.join(BASE_PATH,letter)))
    counter = 0
    times = 0
    no_detected = 0
    for img_name in imgs:
        times +=1
        img_path = os.path.join(BASE_PATH,letter,img_name)
        img = cv2.imread(img_path)
        img = cv2.resize(img,(512,512))
        hands, img = detector.findHands(img,draw=False)
        if hands:
            hand = hands[0]
            x,y,w,h = hand['bbox']
            try:
                img = img[
                    y-OFFSET:y+h+OFFSET,
                    x-OFFSET:x+w+OFFSET
                ]
                img = cv2.resize(img,(300,300))

                counter+=1
                category = 'train' if counter < 500 else 'validation' if counter < 700 else 'test'
                dst = os.path.join('dataset',category,letter,img_name)
                cv2.imwrite(dst,img)

            except:
                pass
        else:
            no_detected +=1
        if counter >= IMG_PER_CLASS:
            break
        cv2.waitKey(1)
    print(letter,'has',times,'images and', counter,'detectable elements and',no_detected,'no detected\n in',datetime.now()-t0)

