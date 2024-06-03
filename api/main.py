from fastapi import FastAPI ,File, UploadFile
import tensorflow as tf
import uvicorn 
from io import BytesIO
import tensorflow as tf
from PIL import Image
import numpy as np
#######################
app = FastAPI()
prod_model = tf.keras.models.load_model("../models/model_1.h5")
beta_model = tf.keras.models.load_model("../models/model_2.h5")
class_name = ['Potato___Early_blight','Potato___Late_blight', 'Potato___healthy']
#######################
@app.get("/ping")
async def ping():
  return "Hello"
def read_image(data) -> np.ndarray:
  return np.asarray(Image.open(BytesIO(data)))

@app.post("/predict")
async def predict(
  file: UploadFile = File(...)
): 
  image_read = read_image(await file.read())
  img_batch = np.expand_dims(image_read,0)
  prediction = model.predict(img_batch)
  prediction_class =  class_name[np.argmax(prediction[0])]
#########################
if __name__ == "__main__":
   uvicorn.run(app,host='localhost',port=8080)