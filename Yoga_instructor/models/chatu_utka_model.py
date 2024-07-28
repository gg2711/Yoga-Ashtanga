# Import necessary libraries
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

# Load the model from the saved file
script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_dir, 'chatu_utka_model.h5')
model = load_model(model_path)

def predict_image(image_path):
    test_image = load_img(image_path, target_size=(64, 64))
    test_image = img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    result = model.predict(test_image)
    if result[0][0] == 0:
        prediction = 'chatu'
    else:
        prediction = 'utka'
    return prediction
