from transformers import pipeline

classifier = pipeline("sentiment-analysis",   
                      "blanchefort/rubert-base-cased-sentiment")

print(classifier("Я обожаю инженерию машинного обучения!"))

## Тут была Даша

# Комментарий от Куницкого закоммиченный через VS Code