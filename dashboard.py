import streamlit as st
import cv2
from ultralytics import YOLO
from PIL import Image
import tempfile

st.set_page_config(layout="wide")
st.title("🚦 Traffic Violation Detection Dashboard")

model = YOLO("yolov8n.pt")

def process_frame(frame):
    results = model(frame)
    return results[0].plot()

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(uploaded_file.read())
    frame = cv2.imread(temp_file.name)
    output = process_frame(frame)
    st.image(output, channels="BGR", caption="Processed Frame", use_column_width=True)
