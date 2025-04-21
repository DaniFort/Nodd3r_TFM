# import time_control
from utils import time_control
from ui.custom_elements.running_layout import RunningLayout
from vision.web_cam_reader import WebCamReader

from utils.image_flow import get_frame_info

import cv2 

time_controller = time_control.FrameTimer(fps=60)

counter = 0
wc = WebCamReader()
lout = RunningLayout()
    
wc.start()
lout.start()

while True:
    if not time_controller.should_update():
        time_control.time.sleep(0.001)
        continue
    wc.update()
    
    
    lout.update()

    lout.draw()
    cv2.imshow('image', get_frame_info())
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
print('Fin Programa')

