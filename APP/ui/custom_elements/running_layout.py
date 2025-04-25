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
        # writed_text_field = WritedTextField(
        #     point=(20, 630),
        #     # point=(0, get_frame_size()[1]-100),
        #     font_scale=3,
        #     line_spacing = 60
        # )
        # bottom_rectangle = Rectangle((0,img_size[0]-150),(img_size[1], img_size[0]),thickness=-1, color=(255,255,255))
        text_box = TextBox((0,img_size[0]-150),(img_size[1], img_size[0]),
                           thickness=-1, rectangle_color=(255,0,255),text_color=(0,0,0),x_margin=20, y_margin=60)
        self.add_element(animated_circle)
        # self.add_element(bottom_rectangle)
        # self.add_element(writed_text_field)
        self.add_element(text_box)
        super().start()