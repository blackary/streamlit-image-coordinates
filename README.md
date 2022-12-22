# streamlit-image-coordinates

Streamlit component that displays an image and returns the coordinates when you click on it

## Installation instructions

```sh
pip install streamlit-image-coordinates
```

## Usage instructions

```python
import streamlit as st

from streamlit_image_coordinates import streamlit_image_coordinates

value = streamlit_image_coordinates("https://placekidden.com/200/300")

st.write(value)
```
