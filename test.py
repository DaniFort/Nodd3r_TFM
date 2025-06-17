import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import cv2
from PIL import Image
import numpy as np

st.title('Holaaaa')

class VideoTransformer(VideoTransformerBase):
    def transform(self, frame):
        img = frame.to_ndarray(formar='bgr24')
        return img
webrtc_streamer(
    key='exameple',
    video_transformer_factory = VideoTransformer,
    media_stream_constraints = {'video':True, 'audio':False}
)


# img_file_buffer = st.camera_input('Hac click para capturar la imagen')
# if img_file_buffer is not None:
#     #leer imagen como array de opnecv
#     img = Image.open(img_file_buffer)

#     img_np = np.array(img)
#     img_bgr = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

#     st.write('Imagen capturada: ')
#     st.image(img_np, channels = 'RGB')