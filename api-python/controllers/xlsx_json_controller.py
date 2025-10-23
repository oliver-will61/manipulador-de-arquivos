from fastapi import HTTPException
from models.Gerenciador_xlsx import Gerenciador_xlsx

async def xlsx_json_controller(arquivo):
        try:
            
            print(f"📥 Arquivo Recebido no Python: {arquivo.filename}")

            # converte para em um formato de bytes que o Python possa ler
            conteudo = await arquivo.read()

            # abre o arquivo em xlsx e o converte para JSON
            gerenciador =  Gerenciador_xlsx(conteudo)
            arquivo_convertido = gerenciador.converte_json()
            
            return {
                "status": "sucesso",
                "mensagem": "Arquivo convertido com sucesso!",
                "arquivoConvertido": arquivo_convertido 
            }
        
        except Exception as e:
            print(f"❌ Erro no Python: {str(e)}")
            raise HTTPException(status_code=500, detail=f"Erro: {str(e)}")
