from fastapi.testclient import TestClient
from fast_api_main import app

client = TestClient(app)

def test_read_fast_api_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Это практическая работа группы 33. Анализ тональности текста. Тест FastAPI приложения. Отправьте текст для оценки токсичности на: <адрес>/checktext/ методом POST"}

def test_read_predict_positive():
    response = client.post("/checktext/",
        json={"text": "love"}
    )
    assert response.status_code == 200
    assert response.text == '"По нашему мнению это доброе высказывание. Уровень достоверности = 98%"'

def test_read_predict_negative():
    response = client.post("/checktext/",
        json={"text": "Shit"}
    )
    assert response.status_code == 200
    assert response.text == '"По нашему мнению это негативное высказывание. Уровень достоверности = 75%"'

def test_read_predict_neutral():
    response = client.post("/checktext/",
        json={"text": "Sky"}
    )
    assert response.status_code == 200
    assert response.text == '"По нашему мнению это высказываение нейтрально. Уровень достоверности = 79%"'