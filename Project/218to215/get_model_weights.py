import os
import tensorflow as tf
from tensorflow import keras
print(tf.__version__)

org_model_path = 'APP/Files/models/ASP_3_model_7.keras'
model = keras.models.load_model(org_model_path)
print('Model loaded successfuly')
base_path = os.path.join('Project','218to215')
json_config = model.to_json()
with open(os.path.join(base_path,'model_config.json'),'w') as json_file:
    json_file.write(json_config)

model.save_weights(os.path.join(base_path, 'model_weights.weights.h5'))
print('All saved succesfully')