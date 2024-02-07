# app.py
import streamlit as st
import os
from PIL import Image
import io

# Function to process the image (example: convert to grayscale)
def process_image(input_image):
    processed_image = input_image.convert('L')
    return processed_image

def main():
    # Create input and output directories if they don't exist
    input_dir = "input"
    output_dir = "output"
    os.makedirs(input_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)

    st.set_page_config(
        page_title="Jigsaw Puzzle App",
        page_icon="🧩",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.title("Jigsaw puzzle Solver")

    # File uploader for input image
    uploaded_file = st.file_uploader("Choose an input image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded input image
        st.text("Input Image")
        input_image = Image.open(uploaded_file)

        # Save the input image to the input folder
        input_filename = os.path.join(input_dir, f"input_{len(os.listdir(input_dir)) + 1}.jpeg")
        input_image.save(input_filename)

        # Display input and output images side by side
        col1, col2 = st.columns(2)

        # Display original input image
        with col1:
            st.image(input_image, caption="Uploaded Input Image", use_column_width=True)

        # Process the image when the "Process Image" button is clicked
        if st.button("Process Image"):
            # Process the image
            output_image = process_image(input_image)

            # Display processed output image
            with col2:
                st.image(output_image, caption="Processed Output Image", use_column_width=True)

            # Save the output image to the output folder
            output_filename = os.path.join(output_dir, f"output_{len(os.listdir(output_dir)) + 1}.png")
            output_image.save(output_filename)

if __name__ == "__main__":
    main()
