import tensorflow as tf
import numpy as np
model_path = 'APP/Files/models/ASP_3_model_7.keras'
model_web_path = 'APP/Files/models/model_7_tf_215.h5'
LETTERS = ['A', 'B', 'C', 'D',  'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','del', 'space']

class Classifier():
    def __init__(self, is_web):
        print('---------\n'*10,model_path if not is_web else model_web_path,'---------\n'*10)
        self.model = tf.keras.models.load_model(model_path if not is_web else model_web_path)
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