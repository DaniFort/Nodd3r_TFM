#Core
import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
from PIL import Image

#Project
from ui.custom_elements.running_layout import RunningLayout
from vision.web_cam_reader import WebCamReader
from utils.image_flow import get_frame_info,update_frame


st.title('HANDS TALK')

class VideoTransformer(VideoTransformerBase):
    def __init__(self):
        self.wc = WebCamReader(is_web = True)
        self.lout = RunningLayout()

    def transform(self,frame):
        img = frame.to_ndarray(format='bgr24')
        update_frame(img)
        self.wc.update()
        # self.lout.update()
        # self.lout.draw()

        return img

webrtc_streamer(
    key = 'example', 
    video_transformer_factory = VideoTransformer,
    media_stream_constraints ={'video':True, 'audio':False})

