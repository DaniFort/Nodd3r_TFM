from ui.layout import Layout
from ui.custom_elements.animated_circle import AnimatedCircle
from ui.custom_elements.writed_text_field import WritedTextField
from utils.image_flow import get_frame_size

class RunningLayout(Layout):
    def __init__(self):
        super().__init__()

        
    def start(self):
        super().start()
        animated_circle = AnimatedCircle(115,110,min_radius=13,max_radius=100,max_thickness=30,min_thickness=3,animation_speed=2)
        writed_text_field = WritedTextField(
            point=(30, 100),
            # point=(0, get_frame_size()[1]-100),
            font_scale=4
        )
        self.add_element(animated_circle)
        self.add_element(writed_text_field)
        for i in self.elements:
            try:
                i.start()
            except:
                pass