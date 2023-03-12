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

""""
Usamos a fixture mocker do pacote pytest-mock para substituir o resultado da 
função requests.get() usada no script mypkg.simple_requests_app.do_get_google
pelo objeto de resposta falso (fake) criado pela fixture amend_response definida
no arquivo tests/conftest.py. Isso é feito usando o método mocker.patch(), 
que recebe como argumentos o nome do objeto que queremos substituir 
(no caso, mypkg.simple_requests_app.requests.get) e o objeto de resposta 
falso (fake) que queremos usar na instrumentação do teste.
"""
@pytest.mark.smoke
def test_do_get_google(mocker, amend_response):
    mocker.patch('mypkg.simple_requests_app.requests.get',
                 return_value=amend_response)
    result = do_get_google()
    EXPECTED = { 'message': 'Hello, World!'}
    assert result.json() == EXPECTED
