from unittest.mock import patch
from requests.models import Response
from mypkg.simple_requests_app import RemoteAPIAccess
from pytest_mock import MockerFixture
import pytest

# Veja https://pypi.org/project/pytest-mock/

# Para testar use:
# python3 -m pytest -vv --durations=5  --cov . -m smoke  tests/test_simple_requests_app.py

# Usando o pytest-mock para criar um objeto de resposta falso (fake)

@pytest.mark.smoke
def test_do_get_httpbin(mocker:MockerFixture):
    remoteAPIAccess = RemoteAPIAccess("https://httpbin.org/get")
    EXPECTED = {'message': 'Hello, World!'}
    with mocker.patch.object(remoteAPIAccess, 'doGet', 
                             return_value={"message": "Hello, World!"}):  
        assert remoteAPIAccess.doGet() == EXPECTED
