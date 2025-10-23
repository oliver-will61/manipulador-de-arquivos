from fastapi import FastAPI, UploadFile, File, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional

from models.Gerenciador_xlsx import Gerenciador_xlsx

async def xlsx_json_controller(arquivo):
        try:
            
            print(f"📥 Arquivo Recebido no Python: {arquivo.filename}")

            # Lê o conteúdo
            conteudo = await arquivo.read()
            print(f"✅ Conteúdo lido: {len(conteudo)} bytes")

            # abre o arquivo xlsx
            gerenciador =  Gerenciador_xlsx(conteudo)
            gerenciador.converte_json()
            
            return {
                "status": "sucesso",
                "mensagem": f"Arquivo {arquivo.filename} recebido com sucesso!",
                #"tamanho": len(conteudo),
                "tipo": arquivo.content_type
            }
        
        except Exception as e:
            print(f"❌ Erro no Python: {str(e)}")
            raise HTTPException(status_code=500, detail=f"Erro: {str(e)}")
