import shutil

from fastapi import FastAPI, File, UploadFile

app = FastAPI()

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
