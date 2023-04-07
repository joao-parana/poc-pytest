# tests/conftest.py

# Se você deseja que a biblioteca “requests” execute solicitações http 
# de forma controlada e instrumentadaem todos os seus testes, você pode 
# usar usar esta implementação conftest.py que define @pytest.fixture(autouse=True)

import pytest
import requests
from requests.models import Response
from mock_get_and_post_requests import MockMyRequest

MOCK_URL = "http://localhost:8083/storage"

@pytest.fixture(autouse=True)
def amend_requests_get(monkeypatch):

    def patched_get(*args, **kwargs) -> Response:
        # raise RuntimeError("Bad! No network for you!")
        # Use args e kwargs para ajustar os casos de uso de teste
        return MockMyRequest(MOCK_URL).getMock()

    monkeypatch.setattr(requests, "get", patched_get)

@pytest.fixture(autouse=False)
def amend_requests_post(monkeypatch):
    def patched_post(*args, **kwargs) -> Response:
        # raise RuntimeError("Bad! No network for you!")
        # Use args e kwargs para ajustar os casos de uso de teste
        return MockMyRequest(MOCK_URL, None).getMock()

    monkeypatch.setattr(requests, "post", patched_post)

"""
Aqui definimos a fixture amend_response, que retorna um objeto 
de resposta falso (fake) que tem o status code 200 e um JSON 
com a mensagem "Hello, World!". Uma função lambda é usada
para definir o método `json()` que pertence a Interface `Response`.

Esta é outra forma de definir uma fixture, pois não usa MonkeyPatch.
"""
@pytest.fixture()
def amend_response():
    fake_response = Response()
    fake_response.status_code = 200
    fake_response.json = lambda: {"message": "Hello, World!"}
    return fake_response
