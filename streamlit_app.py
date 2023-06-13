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

"Try clicking on any of the images below."

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.write("## Url example")

    with st.echo("below"):
        value = streamlit_image_coordinates(
            "https://placekitten.com/200/300",
            key="url",
        )

        st.write(value)

with col2:
    st.write("## Local image example")

    with st.echo("below"):
        value = streamlit_image_coordinates(
            "kitty.jpeg",
            key="local",
        )

        st.write(value)

with col3:
    st.write("## Custom size example")

    with st.echo("below"):
        value = streamlit_image_coordinates(
            "kitty.jpeg",
            width=250,
            key="local2",
        )

        st.write(value)

with col4:
    st.write("## PIL example")

    with st.echo("below"):
        value = streamlit_image_coordinates(
            Image.open("kitty.jpeg"),
            key="pil",
        )

        st.write(value)
