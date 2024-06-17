from __future__ import annotations

from io import BytesIO
from pathlib import Path

import numpy as np
import plotly.express as px
import requests
import streamlit as st
from PIL import Image


# Create the python function that will be called
def streamlit_image_coordinates(
    source: str | Path | np.ndarray | object,
    height: int | None = None,
    width: int | None = None,
    key: str | None = None,
    use_container_width: bool = False,
    click_and_drag: bool = False,
):
    """
    Take an image source and return the coordinates of the image clicked

    Parameters
    ----------
    source : str | Path | object
        The image source
    height : int | None
        The height of the image. If None, the height will be the original height
    width : int | None
        The width of the image. If None, the width will be the original width
    use_column_width : "auto", "always", "never", or bool
        If "auto", set the image's width to its natural size,
        but do not exceed the width of the column.
        If "always" or True, set the image's width to the column width.
        If "never" or False, set the image's width to its natural size.
        Note: if set, `use_column_width` takes precedence over the `width` parameter.
    click_and_drag: bool
        If true, the event is not sent until the user releases the mouse. The
        mouse down event is returned as x1, y1 and the mouse up event is returned
        as x2, y2. Note that x2 and y2 may be outside the image.
    """

    if isinstance(source, (Path, str)):
        if not str(source).startswith("http"):
            content = BytesIO(Path(source).read_bytes())
        else:
            content = BytesIO(requests.get(str(source)).content)
        image = Image.open(content)
    elif hasattr(source, "save") or isinstance(source, np.ndarray):
        image = source
    else:
        raise ValueError("Must pass a string, Path, numpy array or a PIL image")

    fig = px.imshow(image, height=height, width=width)

    if click_and_drag:
        fig.update_layout(
            dragmode="select",
            xaxis={"showticklabels": False},
            yaxis={"showticklabels": False},
            margin={"t": 0, "b": 0, "l": 0, "r": 0},
            height=height,
            width=width,
            # modebar_add=[],
            # modebar_display=False,
        )
    else:
        fig.update_layout(
            clickmode="select",
            xaxis={"showticklabels": False},
            yaxis={"showticklabels": False},
            height=height,
            width=width,
            margin={"t": 0, "b": 0, "l": 0, "r": 0},
            # modebar_add=[],
            # modebar_display=False,
        )

    selection = st.plotly_chart(
        fig,
        on_select="rerun",
        use_container_width=use_container_width,
        config={
            "displayModeBar": False,
        },
        key=key + "_plotly_chart",
        selection_mode="box" if click_and_drag else "points",
    )

    if click_and_drag and (selected_box := selection["selection"].get("box")):
        st.write(selected_box[0])
        x1, x2 = selected_box[0]["x"]
        y1, y2 = selected_box[0]["y"]
        st.session_state[key] = {
            "x1": x1,
            "x2": x2,
            "y1": y1,
            "y2": y2,
        }
        return st.session_state[key]

    return selection["selection"]


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
