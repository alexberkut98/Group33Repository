from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

class Text_for_check(BaseModel):
    text: str

app = FastAPI()

classifier = pipeline("sentiment-analysis",   
                      "blanchefort/rubert-base-cased-sentiment")

@app.get("/")
def root():
  return{"message": "Это практическая работа группы 3.3. Анализ тональности текста. Тест FastAPI приложения. Отправьте текст для оценки токсичности на: <адрес>/chektext/ методом POST"}

@app.post("/chektext/")
def chektext(item: Text_for_check):
  text_res = classifier(item.text)[0]
  if text_res["label"]=="NEGATIVE":
    text_out = "Это плохое высказывание от какого-то душнилы"
  elif text_res["label"]=="POSITIVE":
    text_out = "По нашему мнению это доброе высказывание от хорошего человека"
  else: text_out = "Чёрт знает что хотел сказать автор"
  return text_out
