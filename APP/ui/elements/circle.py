import cv2
from utils.image_flow import get_frame_info, update_frame

class Circle:
    def __init__(self, x,y,radius=10, thickness = 5, color =(0,255,0)):
        self.x = x
        self.y = y
        self.radius = radius
        self.thickness = thickness
        self.color = color
    
    def update(self):
        pass
    
    def draw(self):
        img = cv2.circle(get_frame_info(), (self.x,self.y), int(self.radius), self.color, int(self.thickness))
        update_frame(img)
        pass