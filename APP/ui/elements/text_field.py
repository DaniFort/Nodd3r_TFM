import cv2
from utils.image_flow import get_frame_info,update_frame

class TextField():
    def __init__(self, text, point:tuple,font_face = cv2.FONT_HERSHEY_PLAIN, color = (255,0,0),font_scale = 2,thickness=2):
        self.text = text
        self.point = point
        self.font_face = font_face
        self.color = color
        self.font_scale = font_scale
        self.thickness = thickness
    
    def update(self):
        pass
        
    def draw(self):
        img = cv2.putText(
            img=get_frame_info(),
            text = self.text,
            org=self.point,
            fontFace=self.font_face,
            color = self.color,
            fontScale= self.font_scale,
            thickness= self.thickness,
        )
        update_frame(img)