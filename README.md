# poc-pytest

## Procedimento usado para criar este repositório

```bash
mkdir ~/dev/python3
cd ~/dev/python3
pip3 install pytest
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
3. Execute `python3 -m pytest -v` para verificar se o resultado dos testes mostrou-se adequado.
4. Volte ao passo 1 e recomece novamente para uma nova funcionalidade.

A estrutura de diretório inicial é essa:

```text
tree .
.
├── README.md
├── mypkg
│   ├── __init__.py
│   └── mycode.py
└── tests
    └── test_mycode.py
```
