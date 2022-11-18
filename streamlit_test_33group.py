import io
import streamlit as st

st.title("Анализ тональности текста")
st.markdown("_Практическая_ работа группы 3.3")

from transformers import pipeline

classifier = pipeline("sentiment-analysis",   
                      "blanchefort/rubert-base-cased-sentiment")

text_input = st.text_area("Введите текст для оценки токсичности:", value="")

if st.button("Оценить"):
  text_res = classifier(text_input)[0]
  if text_res["label"]=="NEGATIVE":
    text_out = "Это плохое высказывание от какого-то душнилы"
  elif text_res["label"]=="POSITIVE":
    text_out = "По нашему мнению это доброе высказывание от хорошего человека"
  else: text_out = "Чёрт знает что хотел сказать автор"
  st.header(text_out)
