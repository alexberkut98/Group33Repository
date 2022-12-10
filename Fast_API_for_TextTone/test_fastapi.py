from fastapi.testclient import TestClient
from fast_api_main import app

client = TestClient(app)

def test_read_fast_api_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Это практическая работа группы 33. Анализ тональности текста. Тест FastAPI приложения. Отправьте текст для оценки токсичности на: <адрес>/checktext/ методом POST"}