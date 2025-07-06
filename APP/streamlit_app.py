# Core
import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
from PIL import Image

# Project
from ui.custom_elements.running_layout import RunningLayout
from vision.web_cam_reader import WebCamReader
from utils.image_flow import get_frame_info, update_frame
from utils import time_control
from utils.app_manager import rewrite_writed_text

st.set_page_config(page_title="Hands Talk", layout="centered")

st.title("🧠 HANDS TALK - Transcriptor de lenguaje de signos con IA")

st.markdown("### Proyecto de reconocimiento de lenguaje de signos en tiempo real usando Tensorflow y OpenCV.")

st.markdown("---")

st.markdown("""
Este proyecto es una versión adaptada a streamlit de mi proyecto final de Máster en Data Science cursado en Nodd3r.\n
Esta aplicación desarrollada en Python que permite al usuario escribir utilizando el alfabeto del lenguaje de signos americano en tiempo real. El sistema combina una estructura de aplicación modular con un modelo de clasificación entrenado para interpretar signos.
Es mi primer proyecto completo combinando computer vision,redes neuronales y desarrollo de aplicaciones en Python con OpenCV y streamlit.

Características principales:
- Escritura mediante gestos captados en tiempo real.
- Flujo de ejecución basado en start-update-draw para mayor escalabilidad.
- Aplicación estructurada en componentes independientes.
- Gestión de imagen, sonido y texto de manera eficiente.
- Predicción de texto basada en gestos individuales.
""")


st.markdown("---")

st.markdown("Código fuente del proyecto: 🔗 GitHub [Ir al repositorio de GitHub](https://github.com/DaniFort/HandsTalk)")

st.markdown("---")

writting_speed = st.slider('Velocidad de escritura: ',min_value = 0.5, max_value = 7.0, value = 3.0, step = 0.25)

st.markdown("---")

# st.header("HandsTalk Demo")

class VideoTransformer(VideoTransformerBase):
    def __init__(self):
        with open('APP\Files\writting_speed.txt','w') as file:
            file.write(str(writting_speed))
        print()
        self.time_controller = time_control.FrameTimer()
        self.wc = WebCamReader(is_web=True)
        self.lout = RunningLayout()
        self.components_started = False
        rewrite_writed_text('')

    def transform(self, frame):
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
    

st.markdown("## 📷 HandsTalk Demo ")

col1, col2 = st.columns([2, 1]) 
# heigh, width = 720,1280
heigh, width = 480,640
with col1:
    webrtc_streamer(
        key='example',
        video_transformer_factory=VideoTransformer,
        media_stream_constraints={
            'video': {
                'heigh':{'ideal':heigh},
                'width':{'ideal':width},
            }, 
            'audio': False}
    )

with col2:
    try:
        st.markdown("### 📘 Guía de símbolos")
        symbols_image = Image.open("PlantillaLenguaje.jpg")
        st.image(symbols_image, caption="Tabla de símbolos del lenguaje de signos", use_container_width=True)
    except:
        st.warning("No se encontró la imagen 'symbols_guide.jpg'.")
