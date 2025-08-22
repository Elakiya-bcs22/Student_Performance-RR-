# 🎓 Student Performance Predictor (Ridge Regression)

A **machine learning project** that predicts student performance using **Ridge Regression**.  
This app serves as a practical tool for educators, counselors, and institutions aiming to forecast academic outcomes and provide timely support.

---

## 📌 Project Overview
By analyzing historical student data, the model predicts future performance grades.  
Ideal for **early intervention**, **performance tracking**, and **academic planning**.

---

## ✨ Features
- 🧹 **Data Cleaning & Preprocessing** – Manages missing data, encodes categorical features, and scales numerical values.  
- 📈 **Ridge Regression Model** – A regularized linear model to prevent overfitting.  
- 📊 **Performance Metrics** – MSE, RMSE, MAE, and R² Score to evaluate model quality.  
- 🌐 **Interactive Web App (Flask)** – Input student features to get instant performance predictions.  
- 💾 **Model Persistence** – Saves the trained model (`ridge_model.pkl`) for quick reuse.  

---

## 🗂️ Dataset
Dataset includes features like:
- `study_time`, `attendance_rate`, `past_performance`, `parental_education`, `extracurricular_activities`, etc.  
- 🌟 **Target:** `final_grade` or `performance_score`  

---

## ⚙️ Installation & Setup
```bash
# Clone the repository
git clone https://github.com/Elakiya-bcs22/Student_Performance-RR-.git
cd Student_Performance-RR-

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
```

---

## 🚀 Usage

### 1️⃣ Train the Model
```bash
python train.py
```
This will train the Ridge Regression model and output `ridge_model.pkl` along with any preprocessing artifacts.

### 2️⃣ Run the Web App
```bash
python app.py
```
Open your browser at `http://127.0.0.1:5000/`, enter student data, and receive a **predicted performance score** instantly.

---

## 📊 Example Results
- **R² Score:** ~0.7 – 0.85 (varies depending on dataset quality)  
- **RMSE & MAE:** Low error indicates solid prediction capability.  

---

## 🗁️ Project Structure
```
├── notebooks/             # Jupyter notebooks for exploratory analysis
├── data/                  # Original and processed datasets
├── train.py               # Script to train and save the model
├── app.py                 # Flask app for real-time predictions
├── ridge_model.pkl        # Trained Ridge Regression model
├── requirements.txt       # Required dependencies
└── README.md              # Project documentation
```

---

## 👩‍💻 Author
**Elakiya Kalimuthu**  
📌 [GitHub Repository](https://github.com/Elakiya-bcs22/Student_Performance-RR-)  

