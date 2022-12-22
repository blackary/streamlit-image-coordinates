# Streamlit-Image-Coordinates

[![Releases](https://img.shields.io/pypi/v/streamlit-image-coordinates)](https://pypi.org/project/streamlit-image-coordinates/)
![Python Versions](https://img.shields.io/pypi/pyversions/streamlit-image-coordinates.svg)
![License](https://img.shields.io/github/license/blackary/streamlit-image-coordinates)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://image-coordinates.streamlit.app)

Author: [@blackary](https://github.com/blackary)

Code: https://github.com/blackary/streamlit-image-coordinates

Streamlit component that displays an image and returns the coordinates when you click on it

## Installation instructions

```sh
pip install streamlit-image-coordinates
```

## Usage instructions

```python
import streamlit as st

from streamlit_image_coordinates import streamlit_image_coordinates

value = streamlit_image_coordinates("https://placekitten.com/200/300")

st.write(value)
```
