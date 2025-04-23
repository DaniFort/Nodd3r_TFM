from ui.elements.text_field import TextField
from utils.app_manager import get_writed_text
from utils.image_flow import get_frame_info,update_frame

import cv2

class WritedTextField(TextField):
    def __init__(self, point:tuple,font_face = cv2.FONT_HERSHEY_PLAIN, color = (255,0,0),font_scale = 2,thickness=2,line_spacing = 10):
        super().__init__('', point,font_face, color ,font_scale,thickness,line_spacing)
        self.max_char_per_line = 34
    
    def start(self):
        pass


    def update(self):
        self.text = get_writed_text() 

    def draw(self):
        super().draw()
        img = cv2.putText(
            img=get_frame_info(),
            text = self.text,
            org=(self.point[0],self.point[1]+self.line_spacing),
            fontFace=self.font_face,
            color = self.color,
            fontScale= self.font_scale,
            thickness= self.thickness,
        )
        update_frame(img)

