import cv2

from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)

detector = HandDetector(maxHands=1)
offset = 20
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
            cv2.imshow('Hand img',imgCrop)
        except:
            pass
    cv2.imshow('Image',img)
    img2  = cv2.imread('3.jpg')
    cv2.imshow('hola',img2)
    print(type(img),type(img2))
    cv2.waitKey(1)
