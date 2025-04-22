import cv2
from utils.image_flow import update_frame, get_frame_info
from utils.app_manager import get_writed_text,add_update_to_writed_text,get_is_able_to_write,set_is_able_to_write, get_has_written, set_has_written
class WebCamReader():
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.width, self.height = 1280,720
        self.cap.set(3,self.width)
        self.cap.set(4,self.height)
    
    def start(self):
        self.update()

        
    def update(self):
        _, img = self.cap.read()
        can_write = get_is_able_to_write()
        img = cv2.putText(img,str(can_write), (300,300), cv2.FONT_HERSHEY_COMPLEX,3,(255,0,0),3)
        if get_is_able_to_write() and not get_has_written():
            #predecimos iamgen
            key = cv2.waitKey(6)
            if key == ord('w'):
                character = 'T'
                add_update_to_writed_text(character)
                set_is_able_to_write(False)
                set_has_written(True)
            
        update_frame(img)
