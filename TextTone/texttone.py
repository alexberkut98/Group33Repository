print("Анализ тональности текста")
print("Практическая работа группы 3.3")

from transformers import pipeline

classifier = pipeline("sentiment-analysis",   
                      "blanchefort/rubert-base-cased-sentiment")

text_input = input("Введите текст для оценки токсичности:\t")

text_res = classifier(text_input)[0]
if text_res["label"]=="NEGATIVE":
  text_out = f"Это плохое высказывание от какого-то душнилы на {int(round(text_res['score']*100, 0))}%"
elif text_res["label"]=="POSITIVE":
  text_out = f"По нашему мнению это доброе высказывание от хорошего человека на {int(round(text_res['score']*100, 0))}%"
else: text_out = "Чёрт знает что хотел сказать автор"
print(text_out)
