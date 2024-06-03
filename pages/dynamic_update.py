import streamlit as st
from PIL import Image, ImageDraw
from streamlit_image_coordinates import streamlit_image_coordinates

st.set_page_config(
    page_title="Streamlit Image Coordinates: Image Update",
    page_icon="🎯",
    layout="wide",
)

"# :dart: Streamlit Image Coordinates: Image Update"

if "points" not in st.session_state:
    st.session_state["points"] = []


"## Click on image"


def get_ellipse_coords(point: tuple[int, int]) -> tuple[int, int, int, int]:
    center = point
    radius = 10
    return (
        center[0] - radius,
        center[1] - radius,
        center[0] + radius,
        center[1] + radius,
    )


with st.echo("below"), Image.open("kitty.jpeg") as img:
    draw = ImageDraw.Draw(img)

    # Draw an ellipse at each coordinate in points
    for point in st.session_state["points"]:
        coords = get_ellipse_coords(point)
        draw.ellipse(coords, fill="red")

    value = streamlit_image_coordinates(img, key="pil")

    if value is not None:
        point = value["x"], value["y"]

        if point not in st.session_state["points"]:
            st.session_state["points"].append(point)
            st.experimental_rerun()
