import streamlit as st
from PIL import Image

uploaded_image = st.file_uploader("Upload Image")
if uploaded_image:
    img2 = Image.open(uploaded_image)
    gray_img2 = img2.convert("L")
    st.image(gray_img2)

with st.expander("Start Camera"):
    #   Start the camera
    camera_image = st.camera_input("Camera")

if camera_image:
    #   Create a pillow image instance
    img = Image.open(camera_image)

    #   Convert the pillow image to grayscale
    gray_img = img.convert("L")

    #   Render the grayscale image on the webpage
    st.image(gray_img)



