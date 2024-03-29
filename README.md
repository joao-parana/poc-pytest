# poc-pytest

## Testando upload de arquivo

Em um Teminal execute 

```bash
pip3 install fastapi
pip3 install python-multipart
python3 rest-server.py
```

Isso inicia o REST Server que usa FastAPI.

Em outro Terminal execute

```bash
python3 -m pytest -vv -m smoke  tests/test_upload.py
ls -lAt uploaded/
```

Isso executa o teste unitário que faz o Upload. 

Você verá o arquivo `FortiClientVPNOnlineInstaller.exe` que foi `uploaded` 
usando a API `requests` no programa de teste `tests/test_upload.py`.

Voce também pode fazer outos testes interativos usando OpenAPI/Swagger UI 
na URL: http://127.0.0.1:8305/docs como entrypoint para a submissão de requests além de documentar a API.

Outra forma de testar é usando uma página HTML simples. Para isso execute:

```bash
# Para não prender o terminal, termine a linha com o caracter &
python -m http.server 8012 &
python3 rest-server.py
```

Agora abra no Browser a página http://127.0.0.1:8012/UploadUsingFastAPI.html 

Basta escolher algum arquivo binário ou de texto para fazer o Upload. 

Observe as mensagens da App feita com FastAPI no terminal e a saida em JSON no browser.

Confira também o diretório `uploaded` onde a aplicação salva o arquivo.

**OBS:** A pagina HTML `UploadUsingFastAPI.html` é bastante simples e não integra nenhum tratamento de erro mais sofisticado em JavaScript, apenas uns casos de uso triviais. Serve apenas como referência para uso em alguma implementação mais completa. Veja também que é importante usar o middleware CORSMiddleware no lado do servidor FastAPI para gerar os Headers para autorização de acesso cross-origin e enviar ao cliente (browser).

```bash
ls -lA uploaded/
```

## Procedimento usado para criar este repositório

```bash
mkdir ~/dev/python3
cd ~/dev/python3
pip3 install fastapi
pip3 install python-multipart
pip3 install pytest
pip3 install pytest-cov
pip3 install pytest-mock

touch README.md
mkdir tests
mkdir mypkg
touch mypkg/__init__.py
touch mypkg/mycode.py
touch tests/test_mycode.py
# Escreva a a implementação da classe e da classe de teste.
# Escreva a documentação no README
python3 -m pytest -v # Usado para executar os testes
echo ".pytest_cache" >> .gitignore
echo "tests/__pycache__" >> .gitignore
echo "mypkg/__pycache__/" >> .gitignore
echo ".coverage" >> .gitignore
echo "[pytest]" > pytest.ini
echo "markers =" >> pytest.ini
echo "    smoke: smoke test" >> pytest.ini
git init
git status
git add .
git commit -m "first commit"
git remote add origin git@github.com:joao-parana/poc-pytest.git
git push -u origin master


O resultado pode ser visto em https://github.com/joao-parana/poc-pytest.git
```

O Workflow padrão de desenvolvimento é seguir os passos:

1.  altere o código de teste para testar um novo caso de uso, criando um método para tal na classe de teste.
2.  Implemente a funcionalidade na classe correspondente.
3.  Execute `python3 -m pytest -vv --durations=5  --cov . -m smoke  tests/test_mycode.py` e `python3 -m pytest -vv --durations=5  --cov . -m smoke  tests/test_simple_requests_app.py` para verificar se o resultado dos testes mostrou-se adequado e qual foi o percentual de cobertura de codigo testado.
4.  Volte ao passo 1 e recomece novamente para uma nova funcionalidade.

A estrutura de diretório inicial é essa:

``` text
tree .
.
├── README.md
├── mypkg
│   ├── __init__.py
│   └── mycode.py
├── pytest.ini
└── tests
    ├── conftest.py
    ├── mock_get_requests.py
    ├── test_mycode.py
    └── test_mycode_using_class.py
```

## Por que criar Testes Unitários

O principal objetivo de criar testes unitários e prover uma instrumentação para o código fonte que possa ser usada em scripts automatizados para testar a aplicação **garantindo um alto grau de qualidade ao software** desenvolvido ao mesmo tempo que provê mais confiança a equipe para fazer alterações, sabendo-se que um conjunto de testes de regressão poderá indicar algum problema que por ventura possa ter sido inserido sem querer por algum membro da equipe de desenvolvimento.

Em Python esta instrumentação pode ser criada, por exemplo, usando o método `setattr()` como no exemplo abaixo:

``` python
import my_module

def my_mock_function():
    return "mocked result"

setattr(my_module.MyClass, 'my_method', my_mock_function)
```

Após a declaração do método `my_mock_function()` e da execução do método `setattr()` qualquer chamada ao método `my_method` da classe `my_module.MyClass` invocará na verdade o o método `my_mock_function()` da classe que implementa a instrumentação.

Felismente não é necessário usar esta técnica pois temos frameworks de teste em Python para nos ajudar nesta tarefa.

## Porque usar PyTest

O Python 3 vem com um módulo `unittest` integrado, entretanto o `pytest` fornece funcionalidades adicionais ao desenvolvedor para criar código de qualidade. Veremos aqui apenas o básico do teste unitário que servirá como ponto e partida para voos mais altos posteriormente.

Uma convenção comum é colocar todos os seus testes em um diretório `tests` dentro do seu projeto, mas para pequenos scripts um arquivo `test_myapp.py` no mesmo diretório de `myapp.py` é suficiente.

O padrão básico para uso do `pytest` para teste unitário é configurar um acessório que receberá alguns parâmetros e os usará para gerar as entradas de teste e as saídas esperadas desejadas. Por exemplo no caso de testar o método `sum()` de uma calculadora o acessório deverá criar entradas como (2, 2) e saida (4), por exemplo. O seguedo e saber quais as configurações mínimas de teste que devemos gerar no assessório para garantir a qualidade do código.

Para criar este assessório que nos ajuda a desenvolver testes unitários usamos o que se chama `fixture`.

### Usando fixture

Uma `fixture` é um conjunto de objetos, dados ou configurações que são preparados antes da execução de um teste. Esses objetos, dados ou configurações são usados para estabelecer um ambiente consistente e controlado para que o teste possa ser executado de forma confiável e reproduzível. Existem diferentes tipos de fixtures que podem ser usados em testes unitários, dependendo do contexto e da linguagem de programação utilizada. Alguns exemplos comuns incluem:

-   Fixture de configuração: prepara o ambiente de teste configurando variáveis de ambiente, banco de dados, arquivos de configuração, etc.
-   Fixture de dados: cria ou carrega dados que serão utilizados no teste, como registros de banco de dados, arquivos de entrada, etc.
-   Fixture de objetos: cria objetos que serão utilizados no teste, como instâncias de classes ou bibliotecas de funções.

As fixtures são importantes para garantir que os testes sejam executados de forma consistente e previsível, independentemente do ambiente de execução. Além disso, as fixtures permitem que os testes sejam escritos de forma modular e legível. Com `fixture` as configurações e dados necessários para cada teste podem ser definidos separadamente do código fonte da aplicação, facilitando a manutenção do código. Lembre-se que teste é apenas mais um ASPECTO de uma aplicação e deve ser independente desta, caracterizando por uma instrumentação a ser realizada na aplicação, para garantir a qualidade desta.

### Exemplo de uso de fixture

No exemplo abaixo, usamos a fixture `mocker` do pacote `pytest-mock` para substituir o resultado da chamada a função `requests.get()` usada no script `mypkg.simple_requests_app.do_get_google` pelo objeto de resposta falso (fake) criado pela fixture `amend_response` definida no arquivo `tests/conftest.py`.

Isso é feito usando o método `mocker.patch()`, que recebe como argumentos o nome do objeto que queremos substituir (neste caso, `mypkg.simple_requests_app.requests.get`) e o objeto de resposta falso (fake) que queremos usar na instrumentação do teste.

``` python
@pytest.mark.smoke
def test_do_get_google(mocker, amend_response):
    mocker.patch('mypkg.simple_requests_app.requests.get',
                 return_value=amend_response)
    result = do_get_google()
    EXPECTED = { 'message': 'Hello, World!'}
    assert result.json() == EXPECTED
```

Esta é uma forma simples de usar `fixture` mas podemos usar também o `MonkeyPatch` que pode ser util em cenários mais complexos.

## Como usar o MonkeyPatch para *mockar* objetos complexos

Video explicando a implementação: https://youtu.be/PmDjzIzJVZk

Veja alguns cenários em que o **MonkeyPatch** pode ser apropriado:

-   Quando você precisa substituir um objeto em um módulo importado que não é facilmente substituível por outro método, como um banco de dados ou API externa.
-   Quando você está testando código que depende do estado de tempo ou de outras variáveis do sistema que são difíceis de simular diretamente em um ambiente de teste.

Veja: https://docs.pytest.org/en/7.2.x/how-to/monkeypatch.html

No exemplo implementado neste repositório, o método `push()` da classe `Stack` faz um `request` tipo `GET` para um serviço externo e o modulo `fixture` com `monkeypatch` é usado para **alterar a URL** para um endereço interno já que não é possível acessar o endereço externo real por estar em área protegida no cliente final.

Veja a implementação no arquivo `tests/conftest.py`.

**OBS:** Óbviamente não existe necessidade de acessar serviço HTTP externo numa classe que implemente uma `Stack`. Esta implementação tem apenas propósito didático para demonstrar o uso de `fixture` e `monkeypatch` para implementar `Mock Objects`.