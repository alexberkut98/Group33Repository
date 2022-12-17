# Connecting the FastAPI, pipeline and BaseModel classes from the 
# fastapi, transformers and pydantic libraries

from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

class Text_for_check(BaseModel):
    text: str
        
# Creating a FastAPI object
app = FastAPI()

# Creating a classifier from the Hugging Face library
classifier = pipeline("sentiment-analysis",   
                      "blanchefort/rubert-base-cased-sentiment")

@app.get("/")
def root():
"""Requests to the root directory of the server"""
    return {"message": "Это практическая работа группы 33. Анализ тональности текста. Тест FastAPI приложения. Отправьте текст дляоценки токсичности на: <адрес>/checktext/ методом POST"}

@app.post("/checktext/")
def chektext(item: Text_for_check):
""" Text analysis output """

    text_res = classifier(item.text)[0]
    
    if text_res["label"] == "NEGATIVE":
        text_out = f"По нашему мнению это негативное высказывание. Уровень достоверности = {int(round(text_res['score']*100, 0))}%"
    
    elif text_res["label"] == "POSITIVE":
        text_out = f"По нашему мнению это доброе высказывание. Уровень достоверности = {int(round(text_res['score']*100, 0))}%"
    
    elif text_res["label"] == "NEUTRAL":
        text_out = f"По нашему мнению это высказываение нейтрально. Уровень достоверности = {int(round(text_res['score']*100, 0))}%"
    
    else: 
        text_out = "Не понятно что хотел сказать автор"
    
    return text_out
