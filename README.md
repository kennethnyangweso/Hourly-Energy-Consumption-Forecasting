<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/69ae5d26-c3df-4f29-a263-06e0e11aa43e" />




---

## 📌 Project Overview

This project focuses on predicting **hourly energy consumption** using both **Machine Learning** and **Deep Learning** techniques.

It captures:
- Temporal patterns ⏱️  
- Daily seasonality 📆  
- Consumption trends 📈  

---

## 🏷️ Tech Stack & Badges

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-orange?logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-black?logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-blue?logo=numpy&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-orange?logo=tensorflow&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-blue)
![Seaborn](https://img.shields.io/badge/Seaborn-lightblue)
![Plotly](https://img.shields.io/badge/Plotly-darkblue?logo=plotly)
![Streamlit](https://img.shields.io/badge/Streamlit-red?logo=streamlit&logoColor=white)

---

## 🧠 Data Understanding 📊

The dataset consists of **hourly energy consumption data**.

### Key Variables:
- **Target**
  - `energy_consumption(MW)`

- **Time Features**
  - `year`, `month`, `day`, `day_of_week`, `hour`

👉 Observations:
- Strong **daily and weekly seasonality**
- Repetitive consumption patterns across days
- Time plays a critical role in prediction

---

## 🧹 Data Cleaning

Steps performed:
- Removed missing/null values  
- Ensured correct datetime formatting  
- Eliminated duplicates  
- Sorted data chronologically  

👉 Result:
- Clean, consistent time-series dataset ready for modeling

---

## ⚙️ Feature Engineering

To improve model performance, the following features were created:

### 🔹 Lag Features
- `lag_1` → Previous hour  
- `lag_24` → Same hour previous day  
- `lag_168` → Same hour previous week  

### 🔹 Rolling Statistics
- `rolling_mean_24` → 24-hour average  
- `rolling_mean_168` → 7-day average  

👉 Insight:
- Lag features capture **short-term dependencies**
- Rolling means capture **long-term trends**

---

## 📈 Exploratory Data Analysis (EDA)

EDA was conducted to understand patterns:

### Visualizations Used:
- Line plots (time series trends)  
- Histograms (distribution)  
- Correlation heatmaps
- Bar plot

<img width="624" height="576" alt="image" src="https://github.com/user-attachments/assets/4f883401-32f6-497d-a887-70e0729c3d6e" />


<img width="673" height="459" alt="image" src="https://github.com/user-attachments/assets/ec570a1e-5ec2-4a95-ad91-c1a1432cc501" />


<img width="624" height="494" alt="image" src="https://github.com/user-attachments/assets/55cfc547-35ab-4865-a46c-937e38eda5b3" />


<img width="624" height="404" alt="image" src="https://github.com/user-attachments/assets/2f274373-cddb-45b4-a04f-15be0c4780ca" />


<img width="624" height="529" alt="image" src="https://github.com/user-attachments/assets/e1a18a3b-f58c-4a7a-9f6a-a8a98d8dc577" />


### Key Findings:
- Clear **daily peaks and troughs**
- Weekly recurring patterns  
- Strong correlation between:
  - Current consumption and lag features  
- Rolling averages smooth noisy fluctuations  



---

## 🤖 Modeling

### 🔹 Machine Learning Models
- Random Forest Regressor  
- XGBoost Regressor  

👉 Used:
- Time features  
- Lag features  
- Rolling statistics  

---

### 🔹 Deep Learning Models
- LSTM  
- BiLSTM  

👉 Used:
- Only `energy_consumption(MW)`  
- 24-hour sliding window  

---

## ⏱️ Why 24-Hour Window?

- Energy follows a **daily cycle**
- Captures **intraday dependencies**
- Improves sequential learning  

---

## 📊 Model Evaluation

| Model | RMSE (MW) | MAE (MW) | R² (%) |
|------|--------|--------|--------|
| Random Forest | 669.08 | 429.93 | 98.95 |
| XGBoost | 680.30 | 450.34 | 98.91 |
| LSTM | 1211.30 | 919.16 | 96.56 |
| **BiLSTM** | **658.26** | **397.29** | **98.98** |

**Overall Performance Ranking:**

1.BiLSTM  (Best overall)

2.Random Forest  (Very strong)

3.XGBoost  (Slightly behind RF)

4.LSTM (Weakest)

### 📈 Best Model (BiLSTM) Evaluation Visuals 

<img width="624" height="289" alt="image" src="https://github.com/user-attachments/assets/d542c085-0394-4d8e-80b8-cfa75d207a04" />

<img width="624" height="287" alt="image" src="https://github.com/user-attachments/assets/5aeeeff5-6ff2-4405-a1ea-8a326ea6c956" />

### **Key Insights**

- As a Bidirectional LSTM model, it leverages past and future context within each sequence. The plot likely shows strong alignment with the actual data, capturing both short-term fluctuations and longer-term dependencies in energy consumption.

- The BiLSTM residuals are centered near zero, it suggests the model captures the general consumption patterns well without consistent over- or under-prediction.



---

## 🚀 Deployment

Two models were deployed using **Streamlit**:

### ✅ Random Forest App (`rf_app.py`)
- Uses engineered features  
- Fast predictions  
- Handles structured input  

### ✅ BiLSTM App (`app.py`)
- Uses last 24 hours of consumption  
- Captures temporal dependencies  

---

## 💡 Why Deploy Both Models?

- **Random Forest** → Feature-based predictions  
- **BiLSTM** → Sequence-based predictions  

👉 Benefits:
- Model comparison in real-time  
- Robust forecasting  
- Demonstrates both ML & DL capabilities

#### Results 

<img width="624" height="351" alt="image" src="https://github.com/user-attachments/assets/3856bc03-69c3-44ed-9bb2-a320054f8941" />

<img width="641" height="351" alt="image" src="https://github.com/user-attachments/assets/18aab728-8505-49c5-a47d-4a769a129533" />

<img width="624" height="351" alt="image" src="https://github.com/user-attachments/assets/7fe86d88-2bbf-4d43-8081-dcee162eaf24" />

<img width="624" height="351" alt="image" src="https://github.com/user-attachments/assets/6a7827da-dc66-496d-869a-e76ef471bbf7" />


Links to the video demos :

https://screenrec.com/share/2w4tAYqzcD

https://screenrec.com/share/R1ByEiv75Y


---

## 🏗️ Project Architecture

```text
Dataset → Cleaning → Feature Engineering → EDA → Modeling → Deployment

``` 

---

⚙️ Project Architecture

```text
📁 Energy Consumption Prediction
│
├── 📄 dataset.csv
├── 📄 cleaned_dataset.csv
│
├── 📓 data_understanding.ipynb
├── 📓 data_cleaning_feature_engineering.ipynb
├── 📓 eda.ipynb
├── 📓 machine_learning.ipynb
├── 📓 deep_learning.ipynb
│
├── 📄 rf_energy_model.pkl
├── 📄 bilstm_model.h5
│
├── 📄 app.py              # BiLSTM Streamlit App
├── 📄 rf_app.py           # Random Forest Streamlit App
│
├── 📄 requirements.txt
│
├── 📄 data_report.docx
├── 📄 data_report.pdf
│
└── 📄 README.md

```

## **👤 Author**

**Kenneth Nyangweso**

**Data Scientist | Electrical & Telecommunications Engineer | Machine Learning Engineer | AI Ethusiast**

