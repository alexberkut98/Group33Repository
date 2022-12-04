import io
import streamlit as st

import NewTextTone_core as main

st.title('NEW Text Tone web версия')
greeting_text = main.greeting()
st.markdown(greeting_text)

config = main.readconfig()
text_input = st.text_area(config['start_text'], value='')

if st.button('Оценить'):
  text_out = main.exam_text(text_input)
  st.header(text_out)
