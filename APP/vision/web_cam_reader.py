import cv2
from utils.image_flow import update_frame, get_frame_info, get_frame_size
from utils.app_manager import get_writed_text,add_update_to_writed_text,get_is_able_to_write,set_is_able_to_write, get_has_written, set_has_written
from vision.clasiffier import Classifier
from cvzone.HandTrackingModule import HandDetector
from numpy import expand_dims

class WebCamReader():
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.width, self.height = 1280,720
        self.cap.set(3,self.width)
        self.cap.set(4,self.height)
        self.detector = HandDetector(maxHands=1)
        self.model = Classifier()
    
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
                cv2.imshow('ieee',img_pred)
                img_pred = expand_dims(img_pred/255, axis=0)
                prediction = self.model.predict(img_pred)
                img_crop = cv2.putText(img_crop,str(prediction),(30,60),cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255),3) 
                img[:200,get_frame_size()[1]-200:] = cv2.resize(img_crop,(200,200))

                if get_is_able_to_write() and not get_has_written():
                    print('------------------------------------------****',prediction,'****---------------------------------------------------------------')
                    add_update_to_writed_text(prediction)
                    set_has_written(True)
                    key = cv2.waitKey(6)
                    if key == ord('w'):
                        character = 'T'
                        add_update_to_writed_text(character)
                        set_is_able_to_write(False)
                        set_has_written(True)
            except:
                pass

        update_frame(img)
