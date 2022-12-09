import io
import streamlit as st
from transformers import pipeline

@st.cache(allow_output_mutation=True)
def load_model():
    return pipeline("sentiment-analysis",   
                      "blanchefort/rubert-base-cased-sentiment")
                      
model = load_model()

st.title("Анализ тональности текста")
st.markdown("Практическая работа группы **33**")
text_input = st.text_area("Введите текст для оценки токсичности:", value="")

if st.button("Оценить"):
  text_res = model(text_input)[0]
  if text_res["label"]=="NEGATIVE":
    text_out = f"По нашему мнению это негативное высказывание. \n Уровень достоверности = {int(round(text_res['score']*100, 0))}%"
  elif text_res["label"]=="POSITIVE":
    text_out = f"По нашему мнению это доброе высказывание. \n Уровень достоверности = {int(round(text_res['score']*100, 0))}%"
  elif text_res["label"]=="NEUTRAL":
    text_out = f"По нашему мнению это высказываение нейтрально. \n Уровень достоверности = {int(round(text_res['score']*100, 0))}%"
  else: text_out = "Чёрт знает что хотел сказать автор"
  st.header(text_out)