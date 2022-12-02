from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

class Text_for_chek(BaseModel):
    text: str

#Анализ тональности текста
#Практическая работа группы 3.3
#Тест FastAPI приложения

app = FastAPI()

@app.get("/")
def root();
  return{"message": "
Это практическая работа группы 3.3
Анализ тональности текста
Тест FastAPI приложения
Отправьте текст для оценки токсичности на: <адрес>/chektext/ методом POST"}

@app.post("/chektext/")
def chektext(item: Text_for_chek):
  text_res = classifier(Text_for_chek)[0]
  if text_res["label"]=="NEGATIVE":
    text_out = "Это плохое высказывание от какого-то душнилы"
  elif text_res["label"]=="POSITIVE":
    text_out = "По нашему мнению это доброе высказывание от хорошего человека"
  else: text_out = "Чёрт знает что хотел сказать автор"
return text_out
