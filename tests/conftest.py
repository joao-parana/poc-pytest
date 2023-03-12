# tests/conftest.py

# Se você deseja que a biblioteca “requests” execute solicitações http 
# de forma controlada e instrumentadaem todos os seus testes, você pode 
# usar usar esta implementação conftest.py que define @pytest.fixture(autouse=True)

import pytest
import requests
from requests.models import Response
from mock_get_and_post_requests import MockMyRequest
from pytest_mock import MockerFixture

mockURL = "http://localhost:8083/storage"

@pytest.fixture(autouse=True)
def amend_requests_get(monkeypatch):

    def patched_get(*args, **kwargs) -> Response:
        # raise RuntimeError("Bad! No network for you!")
        # Use args e kwargs para ajustar os casos de uso de teste
        return MockMyRequest(mockURL).getMock()

    monkeypatch.setattr(requests, "get", patched_get)

@pytest.fixture(autouse=True)
def amend_requests_post(monkeypatch):

    def patched_post(*args, **kwargs) -> Response:
        # raise RuntimeError("Bad! No network for you!")
        # Use args e kwargs para ajustar os casos de uso de teste
        return MockMyRequest(mockURL, None).getMock()

    monkeypatch.setattr(requests, "post", patched_post)

"""
@pytest.fixture(moker:MockerFixture)
def amend_requests_x(moker:MockerFixture):
    fake_response = Response()
    fake_response.status_code = 200
    fake_response.json = mocker.Mock(return_value={"message": "Hello, World!"})
    print(fake_response.json)
"""
