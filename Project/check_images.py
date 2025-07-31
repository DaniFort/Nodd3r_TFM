import cv2
from cvzone.HandTrackingModule import HandDetector
import os

BASE_PATH =os.path.join('Project','AumentedData')
detector = HandDetector(maxHands=1)
OFFSET = 150
LETTERS = ['A', 'B', 'C', 'D', 'del', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'space', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def add_path(path):
    with open('no_detected_f.txt','a') as file:
        file.write(path+'\n')

counter_p_t =0
counter_n_t =0

# for cat in ['train','test','validation']:
for cat in range(1):
    # print('\n\n------------------------',cat.upper(),'--------------------------')
    for letter in LETTERS:
        print('\n\n-------------',letter.upper(),'---------------')
        imgs = os.listdir(os.path.join(BASE_PATH,letter))
        counter_n = 0
        counter_p = 0
        for img_name in imgs:
            # img_path = os.path.join(BASE_PATH,cat,letter,img_name)
            img_path = os.path.join(BASE_PATH,letter,img_name)
            # print(img_path)
            img = cv2.imread(img_path)
            hands, img = detector.findHands(img,draw=False)
            if hands:
                counter_p+=1
            else:
                add_path(img_path)
                counter_n+=1

            cv2.waitKey(1)
        counter_p_t+=counter_p
        counter_n_t+=counter_n
        print(counter_p, 'detected from',letter)
        print(counter_n, 'deleted from',letter)


print('Total: ',counter_p_t,'detected and', counter_n_t,'no detected')
