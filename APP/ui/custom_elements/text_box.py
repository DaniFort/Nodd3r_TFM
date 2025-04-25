from ui.elements.rectangle import Rectangle
from ui.custom_elements.writed_text_field import WritedTextField
import cv2
class TextBox(Rectangle):
    def __init__(self, p1,p2, thickness = 5, rectangle_color=(255,255,255),text_color=(0,0,0),x_margin = 10, y_margin = 10):
        super().__init__(p1,p2,thickness,rectangle_color)
        self.x_margin = x_margin
        self.y_margin = y_margin

        self.text = WritedTextField(
            point=(p1[0]+x_margin, p1[1]+y_margin),
            font_scale=3,
            line_spacing = 60,
            color = text_color,
            max_char_per_line = 2
            )

    def start(self):
        super().start()   
        self.text.start()
    
    def update(self):
        super().update()   
        self.text.update()
    
    def draw(self):
        super().draw()   
        self.text.draw()
