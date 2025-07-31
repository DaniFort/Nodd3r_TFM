import cv2
import os
import random
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import shutil
from datetime import datetime

BASE_PATH = os.path.join('Project','ASL_Alphabet_Dataset','asl_alphabet_train')
LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',  'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'del','space']
DESTINY_PATH = 'AumentedData'
DESTINY_PATH = os.path.join('Project','AumentedData')
IMG_PER_CLASS = 2000    
OFFSET = 70
detector = HandDetector(maxHands=1)
t0_abs = datetime.now()
total_imgs = 0
test1_passed = 0
test2_passed = 0
test3_passed = 0

def take_notes_no_detected(img_path):
    with open(os.path.join('Project','new_no_detexted.txt'),'a') as file:
        file.write(img_path+'\n')

for letter in LETTERS:
    t0 = datetime.now()
    if not os.path.exists(os.path.join(DESTINY_PATH,letter)):
        os.mkdir(os.path.join(DESTINY_PATH,letter))
    imgs = np.array(os.listdir(os.path.join(BASE_PATH,letter)))
    counter = 0
    times = 0
    no_detected = 0
    for img_name in imgs:
        total_imgs +=1
        times +=1
        img_path = os.path.join(BASE_PATH,letter,img_name)
        img = cv2.imread(img_path)
        # img = cv2.resize(img,(512,512))
        hands, img = detector.findHands(img,draw=False)
        if hands:#filtro 1
            test1_passed +=1
            hand = hands[0]
            x,y,w,h = hand['bbox']
            try:
                img = img[
                    y-OFFSET:y+h+OFFSET,
                    x-OFFSET:x+w+OFFSET
                ]
                img = cv2.resize(img,(300,300))
                category = 'train'
                dst = os.path.join(DESTINY_PATH,letter,img_name)
                cv2.imwrite(dst,img)
                counter+=1
                # has_hands, img = detector.findHands(img,draw=False)
                # if has_hands:#filtro 2
                #     test2_passed +=1
                #     has_hands2,img = detector.findHands(img,draw=False)

                #     if has_hands2:#filtro 3
                #         test3_passed +=1
                #         counter+=1
                #         category = 'train'
                #         dst = os.path.join(DESTINY_PATH,letter,img_name)
                #         cv2.imwrite(dst,img)
                #     else:
                #         no_detected+=1
                #         take_notes_no_detected(img_path)
                # else:
                #     no_detected+=1
                #     take_notes_no_detected(img_path)
            except:
                pass
        else:
            no_detected +=1
            take_notes_no_detected(img_path)
        # if counter >= IMG_PER_CLASS:
        #     break
        # cv2.waitKey(1)
    result = f'{letter} has {times} images and  {counter} detectable elements and {no_detected} no detected\n in {datetime.now()-t0}'
    print(result)
    with open('Resume images.txt','a')as f:
        f.write(result)

final_text = f'''
Total imágenes analizadas: {total_imgs}
Imagenes que han pasado el test 1: {test1_passed} ---> {test1_passed / total_imgs *100}%
'''
# Imagenes que han pasado el test 2: {test2_passed} ---> {test2_passed / total_imgs *100}%
# Imagenes que han pasado el test 3: {test3_passed} ---> {test2_passed / total_imgs *100}%
print(final_text)
final_text = final_text + f'\ntask done in {datetime.now() - t0_abs}'
print(final_text)
with open('Resumenimagenespost2.txt','a')as f:
    f.write(f'Resume text done in {datetime.now()}')
    f.write(final_text)

