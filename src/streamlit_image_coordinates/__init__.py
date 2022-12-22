from __future__ import annotations

import base64
import hashlib
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

# Tell streamlit that there is a component called streamlit_image_coordinates,
# and that the code to display that component is in the "frontend" folder
frontend_dir = (Path(__file__).parent / "frontend").absolute()
_component_func = components.declare_component(
    "streamlit_image_coordinates", path=str(frontend_dir)
)


# Create the python function that will be called
def streamlit_image_coordinates(
    source: str | Path,
    height: int | None = None,
    width: int | None = None,
    key: str | None = None,
):
    """
    Take an image source and return the coordinates of the image clicked

    Parameters
    ----------
    source : str | Path
        The image source
    height : int | None
        The height of the image. If None, the height will be the original height
    width : int | None
        The width of the image. If None, the width will be the original width
    """

    if not str(source).startswith("http"):
        content = Path(source).read_bytes()
        src = "data:image/png;base64," + base64.b64encode(content).decode("utf-8")
    else:
        src = str(source)

    _str_repr = f"streamlit_image_coordinates({src}, {height}, {width}, {key})"

    _key = hashlib.md5(_str_repr.encode("utf-8")).hexdigest()

    component_value = _component_func(
        src=src,
        height=height,
        width=width,
        key=_key,
    )

    return component_value


def main():
    st.set_page_config(
        page_title="Streamlit Image Coordinates",
        page_icon="🎯",
        layout="wide",
    )
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("## Url example")

        with st.echo():
            value = streamlit_image_coordinates(
                "https://placekitten.com/200/300",
                key="url",
            )

            st.write(value)

    with col2:
        st.write("## Local image example")

        with st.echo():
            value = streamlit_image_coordinates(
                "kitty.jpeg",
                key="local",
            )

            st.write(value)

    with col3:
        st.write("## Custom size example")

        with st.echo():
            value = streamlit_image_coordinates(
                "kitty.jpeg",
                width=250,
                key="local2",
            )

            st.write(value)


if __name__ == "__main__":
    main()
