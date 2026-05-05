# =============================
# 1. FIX IMPORT PATH
# =============================
import os
import sys

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(BASE_DIR)

# =============================
# 2. IMPORT LIBRARIES
# =============================
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib

from src.data.load_data import load_data

# =============================
# 3. PAGE CONFIG
# =============================
st.set_page_config(page_title="AI Expense Tracker", layout="wide")

# =============================
# 4. PREMIUM UI STYLING
# =============================
st.markdown("""
<style>
body { background-color: #0e1117; }
h1 { color: #00FFD1; text-align: center; }

[data-testid="metric-container"] {
    background-color: #1f2937;
    border-radius: 12px;
    padding: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.3);
}

.stButton > button {
    background-color: #00FFD1;
    color: black;
    border-radius: 8px;
    font-weight: bold;
}

section[data-testid="stSidebar"] {
    background-color: #111827;
}
</style>
""", unsafe_allow_html=True)

# =============================
# 5. TITLE
# =============================
st.title("💸 AI-Powered Expense Tracker")
st.caption("📊 Smart Financial Dashboard with AI insights")

# =============================
# 6. FILE UPLOAD
# =============================
st.sidebar.header("📂 Upload CSV")
uploaded_file = st.sidebar.file_uploader("Upload your dataset", type=["csv"])

# =============================
# 7. LOAD DATA
# =============================
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.sidebar.success("✅ CSV Loaded")
else:
    df = load_data()
    st.sidebar.info("Using default dataset")

# =============================
# 8. AUTO FIX COLUMNS
# =============================
df.columns = df.columns.str.strip().str.lower()

required_cols = ["date", "description", "amount", "category"]

if not all(col in df.columns for col in required_cols):
    st.error(f"❌ Required columns missing: {required_cols}")
    st.stop()

# =============================
# 9. PREPROCESS
# =============================
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df = df.dropna(subset=["date", "amount"])

df["month"] = df["date"].dt.to_period("M").astype(str)
df["day"] = df["date"].dt.day_name()

expense_df = df[df["amount"] < 0].copy()
expense_df["amount"] = expense_df["amount"].abs()

# =============================
# 10. KPIs
# =============================
total_spend = expense_df["amount"].sum()
income = df[df["amount"] > 0]["amount"].sum()
savings = income - total_spend

c1, c2, c3 = st.columns(3)

c1.metric("💸 Total Spend", f"₹{total_spend:,.0f}")
c2.metric("💰 Income", f"₹{income:,.0f}")
c3.metric("📈 Savings", f"₹{savings:,.0f}")

st.markdown("---")

# =============================
# 11. TABS
# =============================
tab1, tab2, tab3 = st.tabs(["📋 Overview", "📊 Categories", "📈 Trends"])

# ---- OVERVIEW ----
with tab1:
    st.dataframe(df, use_container_width=True)

# ---- CATEGORY ----
with tab2:
    if not expense_df.empty:
        cat = expense_df.groupby("category")["amount"].sum().sort_values(ascending=False)
        st.bar_chart(cat)

        fig, ax = plt.subplots()
        ax.pie(cat, labels=cat.index, autopct="%1.1f%%")
        st.pyplot(fig)
    else:
        st.warning("No expense data")

# ---- TREND ----
with tab3:
    if not expense_df.empty:
        trend = expense_df.groupby("month")["amount"].sum()
        st.line_chart(trend)
    else:
        st.warning("No data")

# =============================
# 12. AI PREDICTION
# =============================
st.markdown("---")
st.header("🔮 Expense Category Predictor")

model_path = os.path.join(BASE_DIR, "models", "expense_model.pkl")

if os.path.exists(model_path):
    model = joblib.load(model_path)

    text = st.text_input("Enter description")

    if st.button("Predict"):
        if text.strip():
            pred = model.predict([text])[0]
            st.success(f"Category: {pred}")
        else:
            st.warning("Enter valid text")
else:
    st.info("Train model first")

# =============================
# 13. INSIGHTS
# =============================
st.markdown("---")
st.header("📊 Smart Insights")

if not expense_df.empty:
    top = expense_df.groupby("category")["amount"].sum().idxmax()
    avg = expense_df.groupby("date")["amount"].sum().mean()

    st.info(f"💸 Highest spend category: {top}")
    st.info(f"📅 Avg daily spend: ₹{avg:,.0f}")

    if total_spend > 20000:
        st.error("⚠️ Overspending")
    else:
        st.success("✅ Spending OK")

# =============================
# 14. FOOTER
# =============================
st.markdown("---")
st.caption("Built with ❤️ using Streamlit + ML")