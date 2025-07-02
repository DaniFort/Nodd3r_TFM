import json
import os
import tensorflow as tf
from tensorflow import keras
print(tf.__version__)

base_path = os.path.join('Project','218to215')
with open(os.path.join(base_path,'model_config.json'),'r') as json_file:
    json_config = json_file.read()
    print('json config read succesfully')

model = keras.models.model_from_json(json_config)
print('Model creadted from json succesfully')

model.load_weights(os.path.join(base_path, 'model_weights.weights.h5'))
print('Model weights loaded succesfully')

dst_model_path = 'APP/Files/models/ASP_3_model_7_v215.h5'
model.save(dst_model_path)
print('Model saved succesfully')