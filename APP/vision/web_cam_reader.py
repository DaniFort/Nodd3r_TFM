import cv2
from utils.image_flow import update_frame, get_frame_size
from utils.app_manager import add_update_to_writed_text,get_is_able_to_write
from vision.clasiffier import Classifier
from cvzone.HandTrackingModule import HandDetector
from numpy import expand_dims

class WebCamReader():
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        # self.width, self.height = 500,500
        # self.width, self.height = 1080,1920
        # self.width, self.height = 720*3,1280*3
        self.width, self.height = 1920,1080*2
        self.cap.set(3,self.width)
        self.cap.set(4,self.height)
        self.detector = HandDetector(maxHands=1)
        self.model = Classifier()
        self.is_writing = False
    
    def start(self):
        self.update()

        
    def update(self):
        _, img = self.cap.read()
        hands, img = self.detector.findHands(img, draw=False, flipType=True)
        if hands:
            hand = hands[0]
            x,y,w,h = hand['bbox']
            try:
                img_crop = img[y-80:y+h+80,x-80:x+w+80]
                img_crop = cv2.resize(img_crop,(300,300))

                img_pred = cv2.cvtColor(img_crop, cv2.COLOR_BGR2GRAY)
                img_pred = cv2.medianBlur(img_pred, 5)
                img_pred = cv2.adaptiveThreshold(img_pred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
                # cv2.imshow('ieee',img_pred)
                img_pred = expand_dims(img_pred/255, axis=0)
                prediction = self.model.predict(img_pred,get_is_able_to_write())
                img_crop = cv2.putText(img_crop,str(prediction),(30,60),cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255),3) 
                img[:200,get_frame_size()[1]-200:] = cv2.resize(img_crop,(200,200))

                if not get_is_able_to_write() and  self.is_writing:
                    char = self.model.finish_prediction()
                    add_update_to_writed_text(char)
            except:
                pass

        self.is_writing = get_is_able_to_write()

        update_frame(img)