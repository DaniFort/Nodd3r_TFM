from ui.elements.text_field import TextField
from utils.app_manager import get_writed_text
import cv2

class WritedTextField(TextField):
    def __init__(self, point:tuple,font_face = cv2.FONT_HERSHEY_PLAIN, color = (255,0,0),font_scale = 2,thickness=2):
        super().__init__('', point,font_face, color ,font_scale,thickness)
    
    def update(self):
        super().update()
        self.text = get_writed_text()
