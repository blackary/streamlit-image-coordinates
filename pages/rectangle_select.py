import streamlit as st
from PIL import Image, ImageDraw
from streamlit_image_coordinates import streamlit_image_coordinates

st.set_page_config(
    page_title="Streamlit Image Coordinates: Rectangle Select",
    layout="wide",
    page_icon="🪟",
)

"# 🪟 Streamlit Image Coordinates: Rectangle Select"

"## Click and drag on the image"


if "coordinates" not in st.session_state:
    st.session_state["coordinates"] = None


def get_rectangle_coords(
    points: tuple[tuple[int, int], tuple[int, int]],
) -> tuple[int, int, int, int]:
    point1, point2 = points
    minx = min(point1[0], point2[0])
    miny = min(point1[1], point2[1])
    maxx = max(point1[0], point2[0])
    maxy = max(point1[1], point2[1])
    return (
        minx,
        miny,
        maxx,
        maxy,
    )


st.write(st.session_state)

with st.echo("below"), Image.open("kitty.jpeg") as img:
    draw = ImageDraw.Draw(img)

    # if st.session_state["coordinates"]:
    #    coords = get_rectangle_coords(st.session_state["coordinates"])
    #    draw.rectangle(coords, fill=None, outline="red", width=2)

    cols = st.columns([1, 1, 4])
    with cols[0]:
        value = streamlit_image_coordinates(img, key="rectangle", click_and_drag=True)
        st.write(value)

    if value is not None:
        point1 = value["x1"], value["y1"]
        point2 = value["x2"], value["y2"]

        if (
            point1[0] != point2[0]
            and point1[1] != point2[1]
            and st.session_state["coordinates"] != (point1, point2)
        ):
            st.session_state["coordinates"] = (point1, point2)
            st.rerun()
    # Enlarge the rectangle selected between point1 and point2
    if st.session_state["coordinates"]:
        coords = get_rectangle_coords(st.session_state["coordinates"])
        new_image = img.crop(coords)
        new_image = new_image.resize(
            (int(new_image.width * 1.5), int(new_image.height * 1.5))
        )
        with cols[1]:
            st.image(new_image, use_column_width=False)
