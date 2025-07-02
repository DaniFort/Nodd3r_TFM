from tensorflow import keras
org_model_path = 'APP/Files/models/ASP_3_model_7.keras'
dst_model_path = 'APP/Files/models/ASP_3_model_7_v215.h5'

model = keras.models.load_model(org_model_path)
print('Model loaded successfuly')


print('Model saved successfuly')
