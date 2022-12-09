import string
from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

class PostText(BaseModel):
    text: str

app = FastAPI()
classifier = pipeline("sentiment-analysis",   
                      "blanchefort/rubert-base-cased-sentiment")

@app.get("/")
def root():
    """Start screen"""
    return {"message": "Hello World"}

@app.post("/class/")
def classification(pk: PostText):
    """Checking text"""
    cl = classifier(pk.text)[0]
    return cl["label"]