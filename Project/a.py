import cv2
from cvzone.HandTrackingModule import HandDetector


img_path ='3.jpg'
detector = HandDetector(maxHands=1)
OFFSET = 150

for i in range(3,5):
    img  = cv2.imread(str(i)+'.jpg')
    hands,img = detector.findHands(img,draw=False)
    if hands:
        hand = hands[0]
        x,y,w,h = hand['bbox']
        try:
            img_crop = img[
                y-OFFSET:y+h+OFFSET,
                x-OFFSET:x+w+OFFSET
            ]
            img_crop_resized = cv2.resize(img_crop,(300,300))
            cv2.imshow('Hand img',img_crop)
        except:
            pass
    
cv2.destroyAllWindows()
