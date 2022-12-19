import streamlit as st 
x = 4
st.write(x, 'squared is', x * x)

x = st.slider('x')  # 👈 this is a widget
#st.write(x, 'squared is', x * x)
