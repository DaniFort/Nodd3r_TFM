import cv2
from utils.image_flow import get_frame_info, update_frame

class Rectangle:
    def __init__(self, p1,p2, thickness = 5, color =(0,255,0)):
        self.p1 = p1
        self.p2 = p2
        self.thickness = thickness
        self.color = color
    
    def start(self):
        pass
    
    def update(self):
        pass
    
    def draw(self):
        img = cv2.rectangle(get_frame_info(),self.p1, self.p2, self.color, self.thickness)
        update_frame(img)
        pass