import shutil

from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configuração do CORS
origins = [
	"http://localhost",
	"http://localhost:8012",
	"http://localhost:3000",
	"http://127.0.0.1",
	"http://127.0.0.1:8012",
	"http://127.0.0.1:3000"
]

print('Configurando CORS para origens:', origins, '...')
app.add_middleware(
	CORSMiddleware,
	allow_origins=origins,
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

"""
Rota raiz para testar a conexão usando método fetch() do JavaScript no cliente.
Veja o método pingServer() no arquivo UploadUsingFastAPI.html.
"""
@app.get("/")
async def root():
	return {"message": "pong"}

"""Upload de arquivos
Definimos uma rota /uploadfile/ que permite o envio de um arquivo usando o método POST. 
Usamos o decorador @app.post() para registrar uma função que manipula a solicitação POST.

O parâmetro file da função é do tipo UploadFile, que é fornecido pelo pacote fastapi e 
representa um arquivo carregado pelo cliente. Usamos o argumento File(...) para especificar 
que o arquivo é obrigatório e deve ser enviado na solicitação.

Em seguida, retornamos um objeto JSON com o nome do arquivo carregado.
"""
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    print("Recebi", file.filename, "com tamanho", file.size, "e content-type", file.content_type)
    # TODO: grava o arquivo mas não gerencia seu ciclo de vida
    with open("uploaded/recebido_" + file.filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename}
