from fastapi import HTTPException, Response
from models.Gerenciador_xlsx import Gerenciador_xlsx
import json

async def xlsx_json_controller(arquivo):
        try:
            
            print(f"📥 Arquivo Recebido no Python: {arquivo.filename}")

            # Lê o conteúdo em bytes
            conteudo = await arquivo.read()

            # abre o arquivo em xlsx e o converte para JSON
            gerenciador =  Gerenciador_xlsx(conteudo)
            arquivo_convertido = gerenciador.converte_json()

            print(f"🔍 Tipo do arquivo_convertido: {type(arquivo_convertido)}")
            #retorna o arquivo como resposta para donwload

            resposta = Response(
                content= arquivo_convertido,
                #envia a respota em json
                media_type = "application/json",
                headers={
                        "Content-Disposition": f"attachment; filename={arquivo.filename}",
                        "Access-Control-Expose-Headers": "Content-Disposition"
                    }
            )

            print(resposta)
            return resposta
                    
        except Exception as e:
            print(f"❌ Erro no Python: {str(e)}")
            raise HTTPException(status_code=500, detail=f"Erro: {str(e)}")
