import tensorflow as tf
import numpy as np
# from utils.app_manager import add_update_to_writed_text
model_path = 'APP/models/ASP_2_model_7.keras'
LETTERS = ['A', 'B', 'C', 'D',  'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','del', 'space']

class Classifier():
    def __init__(self):
        self.model = tf.keras.models.load_model(model_path)
    
    def predict(self, img):
        prediccion = self.model.predict(img)
        char = LETTERS[np.argmax(prediccion)]
        # add_update_to_writed_text(char)
        return char