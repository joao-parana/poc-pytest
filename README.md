# poc-pytest

## Procedimento usado para criar este repositório

```bash
mkdir ~/dev/python3
cd ~/dev/python3
pip3 install pytest
pip3 install pytest-cov
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

1. altere o código de teste para testar um novo caso de uso, criando um método para tal na classe de teste.
2. Implemente a funcionalidade na classe correspondente.
3. Execute `python3 -m pytest -vv --durations=5  --cov . -m smoke  tests/test_mycode.py` para verificar se o resultado dos testes mostrou-se adequado e qual foi o percentual de cobertura de codigo testado.
4. Volte ao passo 1 e recomece novamente para uma nova funcionalidade.

A estrutura de diretório inicial é essa:

```text
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

## Como usar o MonkeyPatch para *mockar* objetos complexos

Veja: https://docs.pytest.org/en/7.2.x/how-to/monkeypatch.html 

Neste exemplo o método `push()` da classe `Stack` faz um `request` tipo `GET` para um serviço externo e o modulo `fixture` com `monkeypatch` é usado para **alterar a URL** para um endereço interno já que não é possível acessar o endereço externo real por estar em área protegida no cliente final.

Veja a implementação no arquivo `tests/conftest.py`.

**OBS:** Óbviamente não existe necessidade de acessar serviço HTTP externo numa classe que implemente uma `Stack`. Esta implementação tem apenas propósito didático para demonstrar o uso de `fixture` e `monkeypatch` para implementar `Mock Objects`.
