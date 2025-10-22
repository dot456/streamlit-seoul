import streamlit as st
import pandas as pd
import numpy as np

st.title('나으 첫번째 앱이랑께')

st.write('으따 이게 뭣이다냐')
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

