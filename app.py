# app.py
import streamlit as st
import os
from PIL import Image
from io import BytesIO
from transformer_module import transform_image  # Import the function from the module

# Create input and output directories if they don't exist
input_dir = "input"
output_dir = "output"
os.makedirs(input_dir, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)

st.title("Jigsaw puzzle App")

# File uploader for input image
uploaded_file = st.file_uploader("Choose an input image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded input image
    input_image = Image.open(uploaded_file)
    st.image(input_image, caption="Uploaded Input Image", use_column_width=True)

    # Save the input image to the input folder
    input_filename = os.path.join(input_dir, f"input_{len(os.listdir(input_dir)) + 1}.png")
    input_image.save(input_filename)

    # Button to process the image
    if st.button("Process Image"):
        # Call the transform_image function from the imported module
        output_image = transform_image(input_image)

        # Display the transformed output image
        st.image(output_image, caption="Transformed Output Image", use_column_width=True)

        # Save the output image to the output folder
        output_filename = os.path.join(output_dir, f"output_{len(os.listdir(output_dir)) + 1}.png")
        output_image.save(output_filename)
