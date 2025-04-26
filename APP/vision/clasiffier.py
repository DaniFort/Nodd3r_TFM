import tensorflow as tf
import numpy as np
# from utils.app_manager import add_update_to_writed_text
model_path = 'APP/Files/models/ASP_3_model_7.keras'
LETTERS = ['A', 'B', 'C', 'D',  'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','del', 'space']

class Classifier():
    def __init__(self):
        self.model = tf.keras.models.load_model(model_path)
        self.last_predictions = []
    
    def predict(self, img,can_predict:bool):
        prediccion = self.model.predict(img,verbose=0)

        char = LETTERS[np.argmax(prediccion)]
        if can_predict:
            self.last_predictions.append(char)
        return char

    
    def finish_prediction(self):
        if len(self.last_predictions) <=0:
            return None
        char = ''
        count = 0
        for i in self.last_predictions:
            if self.last_predictions.count(i) >count:
                count = self.last_predictions.count(i)
                char = i
        self.reset_predictions()
        return char
    def reset_predictions(self):
        self.last_predictions = []