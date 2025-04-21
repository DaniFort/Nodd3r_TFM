import tensorflow as tf
import os
import cv2
import numpy as np
LETTERS = ['A', 'B', 'C', 'D',  'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','del', 'space']

model_path = 'Trained/ASP_2_model_12.keras'
model = tf.keras.models.load_model(model_path)
print(model.summary())

img_path = 'AumentedData/test/space/space (2454).jpg'
img = cv2.imread(img_path)

cv2.imshow('ieee',img)
img = np.expand_dims(img,axis = 0)
predicction = model.predict(img)
print(predicction)
print(LETTERS[np.argmax(predicction)])

while True:
    key = cv2.waitKey(1)
    if key == ord('q'):
        break