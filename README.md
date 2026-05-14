# 💸 AI-Powered Expense Tracker & Financial Analytics Dashboard

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/FinTech-AI%20Analytics-brightgreen?style=for-the-badge">
  <img src="https://img.shields.io/badge/Dashboard-Streamlit-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/Machine%20Learning-Enabled-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/Visualization-Plotly-success?style=for-the-badge">
</p>

<h1 align="center">💰 AI Expense Tracker</h1>

<p align="center">
📊 Intelligent Personal Finance Analytics & Expense Prediction System
</p>

---

# 🌐 Live Demo

## 🚀 Open Live Dashboard

👉 https://ai-expense-tracker-bcnpvttthcqzcmsqfcs5rs.streamlit.app/

---

# 🖥 Dashboard Preview

<p align="center">
  <img src="outputs/dashboard.png" width="950"/>
</p>

---

# 📌 Project Overview

The AI Expense Tracker & Financial Analytics Dashboard is a production-style FinTech analytics system built using Python, Streamlit, Machine Learning, SQLite, and interactive data visualization tools.

This project simulates a real-world intelligent expense management platform capable of:

- 💳 Tracking financial transactions
- 📊 Visualizing spending behavior
- 🤖 Predicting expense categories
- 📈 Generating financial insights
- 🔮 Forecasting expense trends

The dashboard transforms raw financial records into actionable insights using Machine Learning and Data Science workflows.

---

# ❗ Problem Statement

Most individuals manage expenses manually without extracting meaningful insights from their financial data.

This leads to:

- 💸 Poor financial decisions
- 📉 Lack of spending awareness
- 📊 No budget analysis
- 🔮 No predictive categorization
- 🧾 Difficulty in tracking spending patterns

Traditional expense trackers provide limited analytics and no AI-driven recommendations.

This project solves these challenges using:

- 🤖 Machine Learning
- 📊 Interactive Visualization
- 📈 Financial Analytics
- 💡 Intelligent Insights

---

# 🎯 Project Objectives

✅ Track and manage expenses efficiently  
✅ Analyze spending patterns  
✅ Visualize financial behavior  
✅ Predict expense categories using ML  
✅ Generate smart financial insights  
✅ Build an interactive analytics dashboard  
✅ Improve financial awareness and planning  

---

# 🧠 AI Features

The dashboard includes several AI-powered financial analytics capabilities:

- 🔮 Expense Category Prediction
- 📈 Monthly Expense Trend Analysis
- 📊 Spending Visualization
- 💳 Category-wise Expense Analytics
- 💡 Budget Signals & Alerts
- 🧾 Financial Pattern Detection
- 🤖 Machine Learning Classification

---

# 🧠 System Architecture

```text
User Input (CSV / Default Data)
        ↓
Data Cleaning & Validation
        ↓
Feature Engineering (TF-IDF)
        ↓
Machine Learning Model
        ↓
Predictions + Aggregations
        ↓
Interactive Visualization
        ↓
Insights & Alerts
```

---

# ⚙️ Core Features

# 📊 1. Interactive Dashboard

### KPI Cards

- 💰 Total Spend
- 💵 Total Income
- 📈 Net Savings
- 📊 Spending Ratio

### Dashboard UI

- Wide layout
- Dark professional theme
- Responsive analytics design

---

# 📈 2. Financial Data Visualization

### 📊 Category-wise Analysis

- Bar Charts
- Pie Charts
- Expense Distribution

---

### 📈 Monthly Spending Trends

- Time-series visualization
- Spending behavior analysis
- Monthly financial monitoring

---

# 🔮 3. AI Expense Prediction

### ML Pipeline

```text
Text Description
        ↓
TF-IDF Vectorization
        ↓
Logistic Regression
        ↓
Expense Category Prediction
```

### Example

| Input | Prediction |
|---|---|
| Swiggy Order | Food |
| Uber Ride | Travel |
| Amazon Shopping | Shopping |

---

# 📂 4. CSV Upload & Smart Handling

The system supports custom datasets with automatic preprocessing:

✅ Column normalization  
✅ Missing value handling  
✅ Invalid row filtering  
✅ Date conversion  
✅ Case inconsistency fixing  

### Supported Format

```csv
date,description,amount,category,payment_method
```

---

# 📊 5. Smart Financial Insights

The dashboard generates intelligent insights such as:

- Highest spending category
- Average daily expense
- Spending trends
- Overspending detection
- Budget control feedback

---

# 🛡️ 6. Robust Error Handling

Includes:

✅ Missing column detection  
✅ Invalid date handling  
✅ Empty dataset protection  
✅ ML model availability check  

---

# 📊 Machine Learning Details

| Component | Description |
|---|---|
| Model | Logistic Regression |
| Input | Expense Description |
| Vectorization | TF-IDF |
| Output | Expense Category |

---

# ⚙️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core Programming |
| Pandas | Data Analysis |
| NumPy | Numerical Computing |
| Streamlit | Dashboard Development |
| Plotly | Interactive Charts |
| Matplotlib | Visualization |
| SQLite | Database Storage |
| Scikit-learn | Machine Learning |
| Joblib | Model Saving |
| GitHub | Version Control |
| Streamlit Cloud | Deployment |

---

# 📂 Project Structure

```text
AI-Expense-Tracker/
│
├── app/
│   └── app.py
│
├── src/
│   ├── data/
│   ├── models/
│   ├── utils/
│   └── visualization/
│
├── data/
├── models/
├── outputs/
│
├── requirements.txt
└── README.md
```

---

# 📸 Dashboard Screenshots

# 🖥️ Full Dashboard Overview

<p align="center">
  <img src="outputs/dashboard.png" width="900"/>
</p>

---

# 📊 Category Analysis

<p align="center">
  <img src="outputs/categories.png" width="800"/>
</p>

---

# 🥧 Expense Distribution

<p align="center">
  <img src="outputs/pie_chart.png" width="700"/>
</p>

---

# 📈 Monthly Spending Trends

<p align="center">
  <img src="outputs/trends.png" width="800"/>
</p>

---

# 🔮 AI Prediction System

<p align="center">
  <img src="outputs/predictor.png" width="700"/>
</p>

---

# 🧠 Model Evaluation

<p align="center">
  <img src="outputs/confusion_matrix.png" width="600"/>
</p>

---

# 🚀 Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/sujalkrshaw/AI-Expense-Tracker.git
```

---

## 2️⃣ Open Project Folder

```bash
cd AI-Expense-Tracker
```

---

## 3️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5️⃣ Train ML Model

```bash
python -m src.models.train_model
```

---

## 6️⃣ Run Streamlit Dashboard

```bash
streamlit run app/app.py
```

---

# 🌐 Deployment

This project is deployed using Streamlit Community Cloud.

## 🚀 Live Website

https://ai-expense-tracker-bcnpvttthcqzcmsqfcs5rs.streamlit.app/

---

# 📈 Performance

✅ Lightweight ML model  
✅ Fast prediction speed  
✅ Handles medium-scale datasets efficiently  
✅ Optimized for interactive dashboards  

---

# 💼 Real-World Applications

Applicable in:

- 💳 FinTech Platforms
- 📊 Personal Finance Management
- 🏦 Expense Tracking Systems
- 📈 Budget Planning Tools
- 🤖 AI Financial Assistants

---

# 🚀 Future Enhancements

🔹 User Authentication System  
🔹 PostgreSQL / Cloud Database Integration  
🔹 Mobile App Support  
🔹 Real-time Expense Tracking  
🔹 Fraud Detection System  
🔹 AI Budget Recommendation Engine  
🔹 Voice-based Expense Entry  

---

# 💡 Key Learnings

Through this project, I learned:

✅ End-to-End ML Pipeline Development  
✅ Financial Data Analytics  
✅ Streamlit Dashboard Development  
✅ ML Classification Models  
✅ TF-IDF Feature Engineering  
✅ Data Cleaning & Validation  
✅ Real-world Project Structuring  

---

# 👨‍💻 Author

## Sujal Kumar Shaw

🎓 B.Tech Student | Aspiring Data Scientist

### 🚀 Interests

- 📊 Data Science
- 💰 Financial Analytics
- 🤖 Artificial Intelligence
- 📈 Dashboard Development

---

# 🔗 Project Links

## 🌐 Live Demo

https://ai-expense-tracker-bcnpvttthcqzcmsqfcs5rs.streamlit.app/


# ⭐ Contribution & Support

If you found this project useful:

⭐ Star this repository  
🍴 Fork the project  
📢 Share with others  

---

# 📜 License

This project is licensed for educational and portfolio purposes.

---

# 🚀 Final Note

This project demonstrates how AI, Machine Learning, Financial Analytics, and Interactive Visualization can be combined to build intelligent expense management systems capable of generating meaningful financial insights and predictive analytics.
