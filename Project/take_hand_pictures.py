import os
import cv2
from cvzone.HandTrackingModule import HandDetector

DESTINY_PATH = 'AumentedData'

LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',  'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'del','space']
letter_index = 27
#haremos 250 para train, 120 para validación y  100 para test
cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)
offset = 70
print(f'Imágenes')

for i in range(470):
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
                has_hands, imgCrop = detector.findHands(imgCrop,draw=False)
                if has_hands:    
                    cv2.imshow('Hand img',imgCrop)
                    cv2.imwrite(os.path.join(DESTINY_PATH,LETTERS[letter_index],f'mano_dani{i}.jpg'),imgCrop)
                    break
            except:
                print('failed to save')
                pass
        cv2.imshow('Image',img)
        cv2.waitKey(1)
    print(i)
