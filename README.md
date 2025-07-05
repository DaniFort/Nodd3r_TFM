<h1 align="center">🤖🖐️📣    HANDSTALK    📣🖐️🤖</h1>

<p align="center"><em>Sistema de escritura mediante lenguaje de signos capturado por cámara.</em></p>

<hr>

<h2>📄 Descripción</h2>
<p>Este proyecto es una aplicación desarrollada en Python que permite al usuario escribir utilizando gestos de lenguaje de signos captados por la webcam. 
El sistema combina una estructura de aplicación modular con un modelo de clasificación entrenado para interpretar signos.</p>


<hr>

<h2>🎓 Sobre este proyecto </h2>
<p>Este proyecto fue desarrollado como parte de mi Trabajo Final de Máster de mi Máster en Data Science cursado en Nodd3r.  
Es mi primer proyecto completo combinando visión por computadora, redes neuronales y desarrollo de aplicaciones en Python.</p>

<hr>

<h2>📁 Estructura del repositorio </h2>
<ul>
<li><strong>APP</strong> : Código principal del flujo de la aplicación.</li>
<li><strong>ExploringPredictionResults</strong> : Gráficos y análisis de los resultados de predicción.</li>
<li><strong>Project</strong> : Notebooks y scripts usados para la exploración y tratamiento de datos.</li>
<li><strong>Training</strong> : Entrenamiento de modelos.</li>
<li><strong>LinkVideoPresentacion.txt</strong> : Link al vídeo donde presento el trabajo.</li>
<li><strong>Paper.pdf</strong> : Documento con la memoria escrita del desarrollo de la aplicación.</li>
<li><strong>requirements.txt</strong> : Lista de librerías necesarias para ejecutar el proyecto.</li>

</ul>



<hr>

<h2>✨ Características principales</h2>
<ul>
<li>Escritura mediante gestos captados en tiempo real.</li>
<li>Flujo de ejecución basado en <strong>start-update-draw</strong> para mayor escalabilidad.</li>
<li>Aplicación estructurada en componentes independientes.</li>
<li>Gestión de imagen, sonido y texto de manera eficiente.</li>
<li>Predicción de texto basada en gestos individuales.</li>
</ul>


<hr>

<h2>🛠️ Requisitos</h2>
<ul>
<li>Python 3.8 o superior</li>
<li>numpy</li>
<li>pandas</li>
<li>tensorflow</li>
<li>keras</li>
<li>sklearn</li>
<li>OpenCV (cv2)</li>
<li>cvzone</li>
<li>mediapipe</li>
<li>pygame</li>
<li>gtts</li>
<li>time</li>
<li>os</li>
<li>sys</li>
</ul>

<h2>📊 Datos utilizados</h2>
<ul>
<li>https://www.kaggle.com/datasets/debashishsau/aslamerican-sign-language-aplhabet-dataset</li>
</ul>


<hr>

<h2>🚀 Cómo ejecutar</h2>
<ol>
<li>Clona este repositorio.</li>
<li>Asegúrate de tener todos los paquetes instalados.</li>
<li>Asegúrate de que no haya otro programa usando la cámara de tu dispositivo.</li>
<li>Puedes ejecutar el archivo <code>main.py</code> de la carpeta <strong>APP</strong>.
</ol>
<br>También puedes probar esta versión adaptada a streamlit. <br/>
https://handstalk.streamlit.app/

<hr>

<h2>📈 Futuras mejoras</h2>
<ul>
<li>Crear un detector de manos propio, sin depender de librerías externas.</li>
<li>Mejorar la clasificación de algunas letras difíciles (G, D, J, Z).</li>
<li>Añadir autocompletado y corrección mediante un modelo NLP.</li>
<li>Desplegar la aplicación para dispositivos móviles.</li>
</ul>

<hr>
