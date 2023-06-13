import streamlit as st
from PIL import Image

from streamlit_image_coordinates import streamlit_image_coordinates

st.set_page_config(
    page_title="Streamlit Image Coordinates",
    page_icon="🎯",
    layout="wide",
)

"# :dart: Streamlit Image Coordinates"

st.code("pip install streamlit-image-coordinates")

"Try clicking on the image below"

st.write("# PNG with Transparency Example")

with st.echo("below"):
    value = streamlit_image_coordinates(
        Image.open("kitty.png"),
        width=250,
        key="png",
    )

    st.write(value)
