import streamlit as st
import pandas as pd
import os
from PIL import Image
import glob
from datetime import datetime
import plotly.express as px

# --- Custom CSS for better spacing and style ---
st.markdown("""
<style>
    .main > div.block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .stDataFrame div[data-testid="stDataFrame"] {
        font-size: 14px;
    }
</style>
""", unsafe_allow_html=True)

# Page config
st.set_page_config(
    page_title="🚦 AI Traffic Violation Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🚦 AI Traffic Violation Detection Dashboard")

# File paths
CSV_PATH = "../logs/violations.csv"
IMAGE_DIR = "../static/images"

# Load data
if not os.path.exists(CSV_PATH):
    st.warning("⚠️ violations.csv not found. Please make sure the detection system is logging violations.")
    st.stop()
    
df = pd.read_csv(CSV_PATH)

if df.empty:
    st.info("✅ No violations logged yet.")
    st.stop()

# Convert datetime column to datetime object if exists
if "timestamp" in df.columns:
    df["timestamp"] = pd.to_datetime(df["timestamp"])
else:
    df["timestamp"] = pd.NaT

# Sidebar filters
st.sidebar.header("Filters")

# Date filter
min_date = df["timestamp"].min()
max_date = df["timestamp"].max()
date_range = st.sidebar.date_input("Date range", [min_date.date(), max_date.date()])

# Violation type filter
violation_types = df["violation_type"].unique().tolist()
selected_violations = st.sidebar.multiselect(
    "Select Violation Types",
    options=violation_types,
    default=violation_types
)

# Filter data
filtered_df = df[
    (df["timestamp"].dt.date >= date_range[0]) &
    (df["timestamp"].dt.date <= date_range[1]) &
    (df["violation_type"].isin(selected_violations))
]

# KPI Metrics
st.subheader("Summary Statistics")
kpi1, kpi2, kpi3 = st.columns(3)
kpi1.metric("Total Violations", len(filtered_df))
kpi2.metric("Unique Violation Types", filtered_df["violation_type"].nunique())
if not filtered_df["timestamp"].isnull().all():
    latest_violation = filtered_df["timestamp"].max().strftime("%Y-%m-%d %H:%M:%S")
else:
    latest_violation = "N/A"
kpi3.metric("Latest Violation Time", latest_violation)

st.markdown("---")

# Violation log table
st.subheader("📄 Violation Log")
st.dataframe(filtered_df.reset_index(drop=True), height=300)

# Violation summary bar chart
st.subheader("📊 Violation Summary")

violation_counts = filtered_df["violation_type"].value_counts().reset_index()
violation_counts.columns = ["Violation Type", "Count"]

fig = px.bar(
    violation_counts,
    x="Violation Type",
    y="Count",
    color="Violation Type",
    title="Violation Counts by Type",
    labels={"Count": "Number of Violations"},
    template="plotly_dark"
)

st.plotly_chart(fig, use_container_width=True)

# Recent violation images
st.subheader("📸 Recent Violation Snapshots")
image_files = sorted(
    glob.glob(f"{IMAGE_DIR}/*.jpg"),
    reverse=True
)

display_images = image_files[:10]

cols = st.columns(5)
for idx, img_path in enumerate(display_images):
    with cols[idx % 5]:
        img = Image.open(img_path)
        st.image(img, caption=os.path.basename(img_path), use_column_width=True)

# Sidebar options: Auto-refresh and Clear logs
st.sidebar.markdown("---")
REFRESH = st.sidebar.checkbox("Auto-refresh every 30 seconds")
if REFRESH:
    st.experimental_rerun()

if st.sidebar.button("Clear Logs and Images"):
    if os.path.exists(CSV_PATH):
        os.remove(CSV_PATH)
    for f in glob.glob(f"{IMAGE_DIR}/*.jpg"):
        os.remove(f)
    st.sidebar.success("Logs and images cleared!")
    st.experimental_rerun()
