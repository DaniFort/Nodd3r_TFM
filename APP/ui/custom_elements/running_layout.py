from ui.layout import Layout
from ui.custom_elements.animated_circle import AnimatedCircle
from ui.custom_elements.writed_text_field import WritedTextField
from ui.custom_elements.text_box import TextBox
from ui.elements.rectangle import Rectangle
from utils.image_flow import get_frame_size

class RunningLayout(Layout):
    def __init__(self):
        super().__init__()

        
    def start(self):
        img_size = get_frame_size()
        animated_circle = AnimatedCircle(115,110,min_radius=13,max_radius=100,max_thickness=30,min_thickness=3,animation_speed=2)

        text_box = TextBox((0,img_size[0]-150),(img_size[1], img_size[0]),
                           thickness=-1, rectangle_color=(197,197,197),text_color=(203,191,2),x_margin=20, y_margin=60,text_thickness=4)
        self.add_element(animated_circle)

        self.add_element(text_box)
        super().start()