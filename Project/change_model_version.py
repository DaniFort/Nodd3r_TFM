from tensorflow import keras
org_model_path = 'APP/Files/models/ASP_3_model_7.keras'
model = keras.models.load_model(org_model_path)
print('Model loaded successfuly')

dst_model_path = 'APP/Files/models/ASP_3_model_7_v210.h5'

model.save(dst_model_path)
print('Model saved successfuly')
