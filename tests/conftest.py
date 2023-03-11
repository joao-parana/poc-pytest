# tests/conftest.py

import pytest
import requests
from requests.models import Response
from mock_get_requests import MockMyRequest

mockURL = "http://localhost:8083/storage"


@pytest.fixture(autouse=True)
def amend_requests_get(monkeypatch):

    def patched_get(*args, **kwargs):
        # raise RuntimeError("Bad! No network for you!")
        # Use args e kwargs para ajustar os casos de uso de teste
        return MockMyRequest(mockURL)

    monkeypatch.setattr(requests, "get", patched_get)

@pytest.fixture(autouse=True)
def amend_requests_post(monkeypatch):

    def patched_post(*args, **kwargs):
        # raise RuntimeError("Bad! No network for you!")
        # Use args e kwargs para ajustar os casos de uso de teste
        return MockMyRequest(mockURL, None)

    monkeypatch.setattr(requests, "post", patched_post)
