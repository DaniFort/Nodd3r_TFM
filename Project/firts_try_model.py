import tensorflow as tf
from tensorflow.keras.preprocessing import image
import cv2
import numpy as np
import matplotlib.pyplot as plt
import time

img_path = 'dataset/test/C/C (1898).jpg'
model_path = 'Trained/ASP_model_7.keras'

# img = image.load_img(img_path, target_size=(300,300))

# img_array = image.img_to_array(img)
# print(img_array.shape)

# img_array1 = np.expand_dims(img_array,axis=0)
# img_array1 = img_array1/255

img_array = np.expand_dims(cv2.imread(img_path),axis=0)

try:
    model = tf.keras.models.load_model(model_path)
    print('modelo cargado correctamente')
except:
    print('error al cargar modelo')

t0 = time.time()

predicctions = model.predict(img_array)

print(f'\n\npredecido en ´{time.time()-t0}')
LETTERS = ['A', 'B', 'C', 'D',  'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','del', 'space']

id_class = np.argmax(predicctions)
print(f'predicted {id_class}, which is {LETTERS[id_class]}')
