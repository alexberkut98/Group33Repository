import io
import streamlit as st

st.title("Анализ тональности текста")
st.markdown("_Практическая_ **работа** группы 3.3")

from transformers import pipeline

classifier = pipeline("sentiment-analysis",   
                      "blanchefort/rubert-base-cased-sentiment")

text_for_assasment = st.text_area("Введите текст для оценки токсичности:", value="")

if st.button("Оценить"): st.markdown(classifier(text_for_assasment))
