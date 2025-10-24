import pandas as pd
from io import BytesIO, StringIO

class Gerenciador_xlsx:
    def __init__(self, arquivo):
          self.arquivo = arquivo

    def converte_json(self):
            
            excel_data = BytesIO(self.arquivo)

            # Lê o arquivo Excel
            df = pd.read_excel(excel_data)


            #Usa stringIO para simular um arquivo em memoria
            json_buffer = StringIO()

            #converte o excel em json 
            # 'records' orienta a criação de uma lista de objetos JSON
            # 'indent' adiciona indentação para melhor legibilidade
            df.to_json(json_buffer, orient='records', indent=4, force_ascii=False)  

            # Pega o conteúdo do buffer
            arquivo_json = json_buffer.getvalue()
            json_buffer.close
            
            return arquivo_json