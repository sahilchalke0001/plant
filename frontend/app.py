from werkzeug.utils import secure_filename
from flask import Flask, render_template, request
import os
import json
from PIL import Image, UnidentifiedImageError
import numpy as np
import tensorflow as tf
import base64
from io import BytesIO

app = Flask(__name__)

# Load model and class indices
working_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(working_dir, "trained_model/plant_disease_prediction_model.h5")
model = tf.keras.models.load_model(model_path)
class_indices = json.load(open(os.path.join(working_dir, "class_indices.json")))

def load_and_preprocess_image(image_path, target_size=(224, 224)):
    img = Image.open(image_path)
    img = img.resize(target_size)
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array.astype('float32') / 255.0
    return img_array

def predict_image_class(model, image_path, class_indices):
    preprocessed_img = load_and_preprocess_image(image_path)
    predictions = model.predict(preprocessed_img)
    predicted_class_index = np.argmax(predictions, axis=1)[0]
    predicted_class_name = class_indices[str(predicted_class_index)]
    return predicted_class_name

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    image_data = None
    error = None

    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', error="No file uploaded")

        file = request.files['file']
        if file.filename == '':
            return render_template('index.html', error="No file selected")

        try:
            filename = secure_filename(file.filename)

            if not filename.lower().endswith(('jpg', 'jpeg', 'png')):
                error = "Invalid file type. Please upload a JPG, JPEG, or PNG image."
                return render_template('index.html', error=error)

            image = Image.open(file)
            buffered = BytesIO()
            image.save(buffered, format="JPEG")
            image_data = base64.b64encode(buffered.getvalue()).decode("utf-8")

            temp_image_path = os.path.join(working_dir, 'temp_image.jpg')
            file.seek(0)
            file.save(temp_image_path)

            prediction = predict_image_class(model, temp_image_path, class_indices)

            os.remove(temp_image_path)

        except UnidentifiedImageError:
            error = "The uploaded file is not a valid image. Please try again."
        except Exception as e:
            error = f"An unexpected error occurred: {e}"

    return render_template('index.html', prediction=prediction, image_data=image_data, error=error)

if __name__ == '__main__':
    app.run(debug=True)





