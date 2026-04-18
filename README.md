# climate-trend-analyzer
Data science project for analyzing climate trends, detecting anomalies, and forecasting future patterns using Python, Prophet, and Streamlit.

# 🌍 Climate Trend Analyzer

A comprehensive data science project that analyzes historical climate data to identify trends, detect anomalies, and forecast future climate patterns using statistical and machine learning techniques.

---

## 🚀 Project Overview

The **Climate Trend Analyzer** is an end-to-end data science project designed to simulate and analyze climate data such as temperature, rainfall, and humidity.

It helps in:
- Understanding long-term climate trends
- Detecting unusual weather patterns (anomalies)
- Forecasting future temperature changes

---

## 🎯 Objectives

- Analyze climate patterns over time  
- Detect anomalies such as extreme temperature spikes  
- Forecast future climate trends using time-series modeling  
- Build an interactive dashboard for visualization  

---

## 🧠 Key Features

✅ Synthetic climate data generation  
✅ Data preprocessing and cleaning  
✅ Time-series trend analysis  
✅ Anomaly detection using Z-score  
✅ Forecasting using Prophet  
✅ Interactive dashboard using Streamlit  
✅ Downloadable datasets  

---

## 🏗️ Project Architecture
Data Generation → Preprocessing → Analysis → Anomaly Detection → Forecasting → Visualization

---

## 📊 Dashboard Features

- 📈 Temperature trend visualization  
- ⚠️ Anomaly detection highlights  
- 🔮 Future forecasting (1-year prediction)  
- 📊 Key metrics (avg temperature, rainfall, anomalies)  
- ⬇️ Download processed data & anomaly reports  

---

## 🛠️ Tech Stack

- **Python**
- **Pandas, NumPy**
- **Matplotlib, Plotly**
- **Scikit-learn**
- **Prophet (Time-Series Forecasting)**
- **Streamlit (Dashboard UI)**

---

## 📁 Project Structure
Climate-Trend-Analyzer/
│
├── data/ # Generated dataset
├── src/ # Core modules
│ ├── data_loader.py
│ ├── preprocessing.py
│ ├── anomaly_detection.py
│ ├── forecasting.py
│ └── visualization.py
│
├── app/
│ └── dashboard.py # Streamlit dashboard
│
├── outputs/ # Generated outputs
├── main.py # Pipeline execution
├── requirements.txt
└── README.md

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/climate-trend-analyzer.git
cd climate-trend-analyzer

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate     # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

▶️ Run the Project
Run Dashboard
streamlit run app/dashboard.py
Run Backend Pipeline
python main.py

📊 Sample Outputs
Temperature trend graphs
Anomaly detection plots
Forecasted climate trends
CSV download files

🧪 Methodology

📌 Data Simulation
Seasonal patterns using sine waves
Random noise for realism
Injected anomalies

📌 Analysis
Rolling averages
Statistical summaries
📌 Anomaly Detection
Z-score based outlier detection

📌 Forecasting
Prophet model for time-series prediction

🌎 Real-World Applications
Climate change analysis
Weather forecasting systems
Smart city planning
Agricultural planning
Environmental monitoring

📸 Screenshots

Add your dashboard screenshots here

🚀 Future Improvements
Use real-world datasets (NASA, Kaggle)
Add multiple city support
Deploy dashboard online
Add advanced ML models (LSTM)

👩‍💻 Author

Ishwari Belhekar.
