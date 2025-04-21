import cv2
import os
import random
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import shutil
from datetime import datetime

BASE_PATH = 'ASL_Alphabet_Dataset/asl_alphabet_train'
LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',  'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'del','space']
DESTINY_PATH = 'AumentedData'
IMG_PER_CLASS = 2000
OFFSET = 70
detector = HandDetector(maxHands=1)
t0_abs = datetime.now()
for letter in LETTERS:
    t0 = datetime.now()
    if not os.path.exists(os.path.join(DESTINY_PATH,letter)):
        os.mkdir(os.path.join(DESTINY_PATH,letter))
        # os.mkdir(os.path.join('dataset',letter,))
        # os.mkdir(os.path.join('dataset',letter,))
        # os.mkdir(os.path.join('dataset',letter))
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
        if hands:#filtro 1
            hand = hands[0]
            x,y,w,h = hand['bbox']
            try:
                img = img[
                    y-OFFSET:y+h+OFFSET,
                    x-OFFSET:x+w+OFFSET
                ]
                img = cv2.resize(img,(300,300))
                has_hands, img = detector.findHands(img,draw=False)
                if has_hands:#filtro 2
                    has_hands2,img = detector.findHands(img,draw=False)

                    if has_hands2:#filtro 3
                        counter+=1
                        category = 'train'
                        dst = os.path.join(DESTINY_PATH,letter,img_name)
                        cv2.imwrite(dst,img)
                    else:
                        no_detected+=1
                else:
                    no_detected+=1
            except:
                pass
        else:
            no_detected +=1
        if counter >= IMG_PER_CLASS:
            break
        cv2.waitKey(1)
    result = f'{letter} has {times} images and  {counter} detectable elements and {no_detected} no detected\n in {datetime.now()-t0}'
    print(result)
    with open('Resume images.txt','a')as f:
        f.write(result)

final_text = f'task done in {datetime.now() - t0_abs}'
with open('Resume images.txt','a')as f:
    f.write(final_text)

