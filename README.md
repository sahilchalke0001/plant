# Plant Disease Classification using CNN 

##  Project Overview
This project aims to classify plant leaf diseases using a Convolutional Neural Network (CNN). The model is trained on a dataset containing images of healthy and diseased plant leaves. Accurate disease detection helps farmers take timely preventive measures and improve crop yield.

The trained model is deployed on Azure to enable real-time predictions via API.

---

##  Objective
- Build a CNN model to classify various plant diseases.
- Achieve high accuracy using transfer learning and fine-tuning.
- Provide a web interface for users to upload images and get predictions.
- Deploy the model on Microsoft Azure for real-time predictions.

---

##  Tech Stack
- **Python 3.10**  
- **TensorFlow** – For building and training the CNN model  
- **NumPy & Pandas** – Data manipulation  
- **Flask** – Web interface 

---

##  Dataset
- **Source:** [Plant Village Dataset](https://www.kaggle.com/datasets/abdallahalidev/plantvillage-dataset)  
- The dataset contains labeled images of healthy and diseased leaves across multiple plant species.

---

##  Model Architecture
- **Input Layer:** 224x224 RGB image  
- **Conv Layers:** Multiple convolution and pooling layers to extract features  
- **Flatten Layer:** Converts matrix to vector  
- **Fully Connected Layers:** Dense layers for classification  
- **Output Layer:** Softmax for multi-class classification  

---

##  Project Workflow
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

##  CNN Trained from Scratch

In addition to the transfer learning approach, the CNN model was also **built and trained entirely from scratch** — without using any pre-trained weights — to validate the architecture's standalone performance.

###  Architecture (From Scratch)
- 5 custom convolutional blocks with **BatchNormalization** and **MaxPooling**
- **GlobalAveragePooling2D** instead of Flatten to reduce overfitting
- Dense head with **Dropout(0.5)** for regularization
- Output: **Softmax** over 38 plant disease classes

###  Training Configuration
| Parameter | Value |
|-----------|-------|
| Image Size | 224 × 224 |
| Batch Size | 32 |
| Optimizer | Adam (lr = 1e-3) |
| Loss | Categorical Crossentropy |
| Max Epochs | 50 |
| Callbacks | EarlyStopping, ReduceLROnPlateau, ModelCheckpoint |

###  Result
> ** Test Accuracy: 96% — trained from scratch, no pre-trained weights used.**

This demonstrates that a well-designed custom CNN with BatchNormalization, data augmentation, and proper callbacks can rival transfer learning on the PlantVillage dataset.

---

##  Model Performance
- **Accuracy:** 95% on test data  
- **Loss:** Minimal loss during validation  

---

![op2](https://github.com/user-attachments/assets/c3768654-4802-4667-a4bd-15889e89fb22)

![op1](https://github.com/user-attachments/assets/7dce0c72-bc07-46aa-89c4-677fa40b9172)

---

##  Results
- Example predictions with confidence scores.

---

##  Contributing
Contributions are welcome! Please feel free to submit a pull request or report issues.

---

##  Contact
For any queries, reach out to:  
 **sahilchalke0001@gmail.com**  
 [GitHub Profile](https://github.com/sahilchalke0001)

---

##  Plant Disease Classification – Azure Deployment

This project leverages various Azure services to ensure seamless deployment and management of the CNN model used for plant disease classification. Below is a list of the key Azure resources utilized:

---

###  Azure Resources Used:

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

###  Deployment Workflow

1. **Model Training:** Train the CNN model locally or on Azure Machine Learning.
2. **Model Upload:** Store the trained model in the Azure Storage Account.
3. **Endpoint Creation:** Use the Azure ML SDK to create and manage model endpoints.
4. **Container Deployment:** Deploy the model using Azure Container Instances.
5. **Secure Authentication:** Use Azure Identity and Key Vault to manage access securely.
6. **Endpoint Access:** The model is accessible through REST API endpoints for predictions.

---

###  Now you can use the model as API because it is hosted on the Azure cloud and get the predictions!!! Video given below...

https://github.com/user-attachments/assets/d51f94fa-f738-45c1-a035-ac203a71dff7

![Azure1](https://github.com/user-attachments/assets/5b2cb7ec-4685-4f74-9157-0a1b137535f8)

![Azure2](https://github.com/user-attachments/assets/a899f82b-a1dc-4d16-88b5-a18cfd700ec7)

