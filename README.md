
# 🌱 Plant Disease Classification using CNN 🌿

## 📚 Project Overview
This project aims to classify plant leaf diseases using a Convolutional Neural Network (CNN). The model is trained on a dataset containing images of healthy and diseased plant leaves. Accurate disease detection helps farmers take timely preventive measures and improve crop yield.

The trained model is deployed on Azure to enable real-time predictions via API.

---

## 🎯 Objective
- Build a CNN model to classify various plant diseases.
- Achieve high accuracy using transfer learning and fine-tuning.
- Provide a web interface for users to upload images and get predictions.
- Deploy the model on Microsoft Azure for real-time predictions.

---

## 🖥️ Tech Stack
- **Python 3.10**  
- **TensorFlow** – For building and training the CNN model  
- **NumPy & Pandas** – Data manipulation  
- **Matplotlib & Seaborn** – Data visualization  
- **Flask** – Web interface 

---

## 📊 Dataset
- **Source:** [Plant Village Dataset](https://www.kaggle.com/datasets/abdallahalidev/plantvillage-dataset)  
- The dataset contains labeled images of healthy and diseased leaves across multiple plant species.

---

## 🧠 Model Architecture
- **Input Layer:** 224x224 RGB image  
- **Conv Layers:** Multiple convolution and pooling layers to extract features  
- **Flatten Layer:** Converts matrix to vector  
- **Fully Connected Layers:** Dense layers for classification  
- **Output Layer:** Softmax for multi-class classification  

---

## 🚀 Project Workflow
1. **Data Collection & Preprocessing:**  
   - Image resizing, normalization, and data augmentation.  
   - Split dataset into training, validation, and testing sets.

2. **Model Training:**  
   - Build CNN architecture.  
   - Compile and fit the model.

3. **Model Evaluation:**  
   - Epochs Used: 5
   - Accuracy Achieved: 97%

4. **Deployment:**  
   - Build a Flask app for real-time predictions.

---

## ⚙️ Setup Instructions
### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/plant-disease-classification.git
cd plant-disease-classification
```

### 2. Create and Activate Virtual Environment
```bash
# Create virtual environment
python3 -m venv env
# Activate (Linux/Mac)
source env/bin/activate
# Activate (Windows)
env\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Model Training
```bash
python app.py
```

### 5. Launch Web Interface (Optional)
```bash
# If using Flask
python app.py
```
- [plant_disease_classifier_1.jpg](sandbox:/mnt/data/plant_disease_classifier_1.jpg)
- [plant_disease_classifier_2.jpg](sandbox:/mnt/data/plant_disease_classifier_2.jpg)

✅ Upload them to your GitHub repo, and you can use these links to add them to your README! 😊
---

## 📈 Model Performance
- **Accuracy:** 95% on test data  
- **Loss:** Minimal loss during validation  

---

## 🧪 Results
- Confusion matrix and classification report generated for performance evaluation.
- Example predictions with confidence scores.

---

## 📝 To-Do List
- [ ] Fine-tune the model with more data.  
- [ ] Add real-time prediction API.  
- [ ] Integrate with IoT for real-time disease detection.  

---

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a pull request or report issues.

---

## 📩 Contact
For any queries, reach out to:  
📧 **your.email@example.com**  
🔗 [GitHub Profile](https://github.com/yourusername)

---

## 📜 License
This project is licensed under the **MIT License**.

---

Let me know if you’d like help generating a `requirements.txt` or improving the web interface! 😊
