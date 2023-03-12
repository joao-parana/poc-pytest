import pytest
from pytest_mock import MockerFixture
from mypkg.simple_requests_app import RemoteAPIAccess
from mypkg.simple_requests_app import do_get_google

# Veja https://pypi.org/project/pytest-mock/

# Para testar use:
# python3 -m pytest -vv --durations=5  --cov . -m smoke  tests/test_simple_requests_app.py

# Usando o pytest-mock para criar um objeto de resposta falso (fake)

@pytest.mark.smoke
def test_do_get_httpbin(mocker:MockerFixture):
    remoteAPIAccess = RemoteAPIAccess("https://httpbin.org/get")
    EXPECTED = {'message': 'Hello, World!'}
    with mocker.patch.object(
        remoteAPIAccess, 'doGet', 
        return_value={"message": "Hello, World!"}): 
        assert remoteAPIAccess.doGet(None) == EXPECTED

@pytest.mark.smoke
def test_do_get_google(mocker, amend_response):
    mocker.patch('mypkg.simple_requests_app.requests.get',
                 return_value=amend_response)
    result = do_get_google()
    EXPECTED = { 'message': 'Hello, World!'}
    assert result.json() == EXPECTED
