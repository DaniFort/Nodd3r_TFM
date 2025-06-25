#Core
import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
from PIL import Image

#Project
from ui.custom_elements.running_layout import RunningLayout
from vision.web_cam_reader import WebCamReader
from utils.image_flow import get_frame_info,update_frame
from utils import time_control

st.title('HANDS TALK')

class VideoTransformer(VideoTransformerBase):
    def __init__(self):
        self.time_controller = time_control.FrameTimer()
        self.wc = WebCamReader(is_web = True)
        self.lout = RunningLayout()
        self.components_started = False

    def transform(self,frame):
        self.time_controller.should_update()
        img = frame.to_ndarray(format='bgr24')
        update_frame(img)
        if not self.components_started:
            self.wc.start()
            self.lout.start()
            self.components_started = True

        self.wc.update()
        self.lout.update()
        self.lout.draw()

        return img

webrtc_streamer(
    key = 'example', 
    video_transformer_factory = VideoTransformer,
    media_stream_constraints ={'video':True, 'audio':False})

