import streamlit as st
import glob

st.title("Demo for Image Grid")

@st.cache(allow_output_mutation=True)
def load_images():
    image_files = glob.glob("images/*/*.jpg")
    manuscripts = []
    for image_file in image_files:
        image_file = image_file.replace("\\", "/")
        parts = image_file.split("/")
        if parts[1] not in manuscripts:
            manuscripts.append(parts[1])
    manuscripts.sort()
    return image_files, manuscripts

images, manuscripts = load_images()

manuscripts = st.multiselect("Select Manuscript", manuscripts)

view_images = []
for image in images:
    if any(manuscript in image for manuscript in manuscripts):
        view_images.append(image)

n = st.number_input("Grid Width", 1, 5, 2)

groups = []
for i in range(0, len(view_images), n):
    groups.append(view_images[i:i+n])


for group in groups:
    cols = st.columns(n)
    for i, image in enumerate(group):
        cols[i].image(image)
