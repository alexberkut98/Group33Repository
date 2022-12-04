import NewTextTone_core as main

from fastapi import FastAPI
from pydantic import BaseModel

class ItsText(BaseModel):
  text: str

app = FastAPI()

@app.get('/')
def root():
  greeting_text = main.greeting()
  greeting_text = greeting_text.replace('\n','')
  return{'message':greeting_text}

@app.post('/examtext/')
def examtext(text_from_somewhere: ItsText):
  result = main.exam_text(text_from_somewhere.text)
  return result
