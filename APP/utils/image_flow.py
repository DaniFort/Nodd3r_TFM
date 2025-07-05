# import cv2
import numpy as np 
from cv2 import resize
sizes = []

frame = None
def get_frame_info():
    return frame

def update_frame(fr):
    global frame
    print(get_frame_size())

    # fr = resize(fr, (960,540))
    # print('2:',np.shape(fr))
    frame = fr

def get_frame_size():
    global frame
    return np.array(frame).shape