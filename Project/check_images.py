import cv2
from cvzone.HandTrackingModule import HandDetector
import os

BASE_PATH ='dataset'
detector = HandDetector(maxHands=1)
OFFSET = 150
LETTERS = ['A', 'B', 'C', 'D', 'del', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'space', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def add_path(path):
    with open('no_detected.txt','a') as file:
        file.write(path+'\n')

for cat in ['train','test','validation']:
    print('\n\n------------------------',cat.upper(),'--------------------------')
    for letter in LETTERS:
        imgs = os.listdir(os.path.join(BASE_PATH,cat,letter))
        counter = 0
        for img_name in imgs:
            img_path = os.path.join(BASE_PATH,cat,letter,img_name)
            # print(img_path)
            img = cv2.imread(img_path)
            hands, img = detector.findHands(img,draw=False)
            if hands:
                pass
            else:
                add_path(img_path)
                counter+=1

            cv2.waitKey(1)
        print(counter, 'deleted from',letter)
