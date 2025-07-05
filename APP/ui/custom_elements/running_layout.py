from ui.layout import Layout
from ui.custom_elements.animated_circle import AnimatedCircle
from ui.custom_elements.writed_text_field import WritedTextField
from ui.custom_elements.text_box import TextBox
from utils.image_flow import get_frame_size

class RunningLayout(Layout):
    def __init__(self):
        super().__init__()

        
    def start(self):
        img_size = get_frame_size()
        writting_speed= 2
        with open('APP\Files\writting_speed.txt','r') as file:
            writting_speed = float(file.read())
        animated_circle = AnimatedCircle(41,40,min_radius=4,max_radius=33,max_thickness=12,min_thickness=2,animation_speed=writting_speed)

        text_box = TextBox((0,img_size[0]-74),(img_size[1], img_size[0]),
                           thickness=-1, rectangle_color=(197,197,197),text_color=(203,191,2),x_margin=20, y_margin=30,text_thickness=4)
        self.add_element(animated_circle)

        self.add_element(text_box)
        super().start()