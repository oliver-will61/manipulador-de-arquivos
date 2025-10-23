from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from controllers.xlsx_json_controller import xlsx_json_controller

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

    #chama controller
    return await xlsx_json_controller(arquivo)

if __name__ == "__main__":
    uvicorn.run(
        "__main__:app",
        host=HOST,
        port=PORT,
        reload=DEBUG
    )