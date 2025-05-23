from ui.elements.circle import Circle 
from utils import time_control
from utils.image_flow import get_frame_info
from utils.app_manager import  set_is_able_to_write
import math

class AnimatedCircle(Circle):
    def __init__(self, x,y,radius=10, thickness = 5, color =(224,220,102),max_radius=50, min_radius=25, max_thickness=10, min_thickness=3, animation_speed=4):
        super().__init__(x,y,radius,thickness,color)
        self.max_radius = max_radius
        self.min_radius = min_radius
        self.max_thickness = max_thickness
        self.min_thickness = min_thickness
        self.animation_speed = animation_speed
        self.counter = 0
        self.has_written = False
        self.origin_color = color
    
    def update(self):
        super().update()
        deltatime = time_control.deltatime
        self.counter += deltatime*self.animation_speed
        self.radius = ((self.min_radius+self.max_radius)/2)+((self.max_radius-self.min_radius)/2)*math.sin(self.counter)

        self.thickness = ((self.max_thickness+self.min_thickness)/2)+((self.max_thickness-self.min_thickness)/2)*math.cos(self.counter)
        if math.sin(self.counter) > -0.9:
            self.color = self.origin_color
            set_is_able_to_write(False)
        else:
            self.color = (0,0,255)
            set_is_able_to_write(True)

    def draw(self):
        super().draw()
        img = get_frame_info()
        
