
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
#using Flask
python app.py
```
[![Apple_Black_Rot](https://i.postimg.cc/2SGggKD1/Whats-App-Image-2025-03-28-at-22-46-26-6a110694.jpg)](https://postimg.cc/JsyTkKt8)
[![Blue_Berry_Image](https://i.postimg.cc/7h1K05P5/Whats-App-Image-2025-03-28-at-22-23-52-9e6ed9e5.jpg)](https://postimg.cc/tnTdHCxb)

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
Here’s a well-structured **README.md** section explaining the Azure resources used for your **Plant Disease Classification** project:

---

## 🌱 Plant Disease Classification – Azure Deployment

This project leverages various Azure services to ensure seamless deployment and management of the CNN model used for plant disease classification. Below is a list of the key Azure resources utilized:

---

### ⚡️ Azure Resources Used:

1. **Azure Resource Group**  
   - Groups related resources, enabling better management, monitoring, and security of Azure assets.

2. **Azure Machine Learning Workspace**  
   - Manages machine learning models, experiments, and endpoints.
   - Provides an interactive interface to train, evaluate, and deploy models.

3. **Azure Machine Learning SDK (v2)**  
   - Programmatically creates and manages endpoints for deploying the CNN model.
   - Facilitates seamless interaction with the Azure Machine Learning Workspace.

4. **Azure Identity**  
   - Ensures secure authentication and access control to Azure resources.
   - Manages credentials securely, preventing unauthorized access.

5. **Azure Container Instances (ACI)**  
   - Hosts the deployed model in a lightweight container environment.
   - Ensures scalability and high availability of the application.

6. **Azure Storage Account**  
   - Stores model artifacts, datasets, and other related files.
   - Enables easy retrieval of model files during deployment.

7. **Azure Key Vault**  
   - Manages sensitive information such as API keys, passwords, and connection strings.
   - Ensures secure access to application secrets and certificates.

---

### 🚀 Deployment Workflow

1. **Model Training:** Train the CNN model locally or on Azure Machine Learning.
2. **Model Upload:** Store the trained model in the Azure Storage Account.
3. **Endpoint Creation:** Use the Azure ML SDK to create and manage model endpoints.
4. **Container Deployment:** Deploy the model using Azure Container Instances.
5. **Secure Authentication:** Use Azure Identity and Key Vault to manage access securely.
6. **Endpoint Access:** The model is accessible through REST API endpoints for predictions.

---

## 📜 License
This project is licensed under the **MIT License**.

---

