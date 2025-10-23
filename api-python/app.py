from fastapi import FastAPI, UploadFile, File, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import pandas as pd

import uvicorn

#constante de configuração

HOST = "localhost"
PORT = 5000
DEBUG = True

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/xlsx-json")
async def processaArquivo(arquivo: UploadFile = File(...)):
    try:
        print(f"📥 Arquivo Recebido no Python: {arquivo.filename}")
        print(f"📄 Tipo: {arquivo.content_type}")
        
        # Lê o conteúdo
        conteudo = await arquivo.read()
        print(f"✅ Conteúdo lido: {len(conteudo)} bytes")

        # abre o arquivo xlsx
        df = pd.read_excel(conteudo)
        print(df)
        
        return {
            "status": "sucesso",
            "mensagem": f"Arquivo {arquivo.filename} recebido com sucesso!",
            #"tamanho": len(conteudo),
            "tipo": arquivo.content_type
        }
        
    except Exception as e:
        print(f"❌ Erro no Python: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erro: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(
        "__main__:app",
        host=HOST,
        port=PORT,
        reload=DEBUG
    )