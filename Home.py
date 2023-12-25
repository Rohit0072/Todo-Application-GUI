# Note: This script runs only on a local IDE with "streamlit run main.py"
import streamlit as st
from PIL import Image

def convert_image(input_image):
    img = Image.open(input_image)
    gray_img = img.convert('L')
    return gray_img

st.subheader("Color to Grayscale Converter")

with st.expander("Start camera"):
    camera_image = st.camera_input("Camera")
with st.expander("Upload File"):
    file_upload = st.file_uploader("Upload Image")
if camera_image:
    gray_camera_img = convert_image(camera_image)
    st.image(gray_camera_img)
if file_upload:
    gray_uploaded_img = convert_image(file_upload)
    st.image(gray_uploaded_img)