import streamlit as st
from PIL import Image

import requests
from io import BytesIO
import numpy as np
from itertools import cycle


sunset_imgs = [
    'https://unsplash.com/photos/-IMlv9Jlb24/download?force=true',
    'https://unsplash.com/photos/ESEnXckWlLY/download?force=true',
    'https://unsplash.com/photos/mOcdke2ZQoE/download?force=true',
    'https://unsplash.com/photos/GPPAjJicemU/download?force=true',
    'https://unsplash.com/photos/JFeOy62yjXk/download?force=true',
    'https://unsplash.com/photos/kEgJVDkQkbU/download?force=true',
    'https://unsplash.com/photos/i9Q9bc-WgfE/download?force=true',
    'https://unsplash.com/photos/tIL1v1jSoaY/download?force=true',
    'https://unsplash.com/photos/-G3rw6Y02D0/download?force=true',
    'https://unsplash.com/photos/xP_AGmeEa6s/download?force=true',
    'https://unsplash.com/photos/4iTVoGYY7bM/download?force=true',
    'https://unsplash.com/photos/mBQIfKlvowM/download?force=true',
    'https://unsplash.com/photos/A-11N8ItHZo/download?force=true',
    'https://unsplash.com/photos/kOqBCFsGTs8/download?force=true',
    'https://unsplash.com/photos/8DMuvdp-vso/download?force=true'
]
st.title('Pattern matching')



with st.expander("This might go well with...", expanded=False):
    filteredImages = sunset_imgs
    cols = cycle(st.columns(3))
    for idx, filteredImage in enumerate(filteredImages):
        next(cols).image(filteredImage, use_column_width=True)