# 🧠 Garbage Classifier Project

An end-to-end AI project to classify garbage images using Convolutional Neural Networks, served through FastAPI and visualized with a user-friendly Streamlit frontend.

---

## 🔍 Project Structure

garbage-classifier/
├── backend/ # FastAPI backend with prediction API
├── data/ # Raw and preprocessed image data
├── frontend/ # Streamlit frontend UI
├── model/ # Trained model and label map
├── notebooks/ # Jupyter notebook for model training
├── utils/ # Preprocessing script
└── requirements.txt # Project dependencies


---

## 🚀 Features

- Image classification using CNN
- Model trained on labeled garbage dataset
- REST API with FastAPI
- Frontend built using Streamlit
- End-to-end prediction system

---

## 🧪 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/garbage-classifier.git
cd garbage-classifier

### 2. Install Requirements

```bash
pip install -r backend/requirements.txt

### 3. Train The Model

```bash
jupyter notebook notebooks/training.ipynb

### 4. Start Backend API

```bash
cd backend
uvicorn main:app --reload

### 5. Run Streamlit Frontend

```bash
cd frontend
streamlit run app.py


📎 License
This project is open-source under the MIT License.

