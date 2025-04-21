from ui.elements.circle import Circle 
from utils import time_control
from utils.image_flow import get_frame_info, update_frame
from utils.app_manager import get_is_able_to_write, set_is_able_to_write
import math
import cv2

class AnimatedCircle(Circle):
    def __init__(self, x,y,radius=10, thickness = 5, color =(0,255,0),max_radius=50, min_radius=25, max_thickness=10, min_thickness=3, animation_speed=4):
        super().__init__(x,y,radius,thickness,color)
        self.max_radius = max_radius
        self.min_radius = min_radius
        self.max_thickness = max_thickness
        self.min_thickness = min_thickness
        self.animation_speed = animation_speed
        self.counter = 0
        self.has_written = False
    
    def update(self):
        super().update()
        deltatime = time_control.deltatime
        self.counter += deltatime*self.animation_speed
        self.radius = ((self.min_radius+self.max_radius)/2)+((self.max_radius-self.min_radius)/2)*math.sin(self.counter)

        self.thickness = ((self.max_thickness+self.min_thickness)/2)+((self.max_thickness-self.min_thickness)/2)*math.cos(self.counter)
        if math.sin(self.counter) > -0.9:
            self.color = (0,255,0)
            set_is_able_to_write(False)
        else:
            self.color = (0,0,255)
            #llamaremos a predecir mano
            set_is_able_to_write(True)

    def draw(self):
        super().draw()
        img = get_frame_info()
        # img = cv2.putText(img,str(self.can_write), (300,300), cv2.FONT_HERSHEY_COMPLEX,3,(255,0,0),3)
        
