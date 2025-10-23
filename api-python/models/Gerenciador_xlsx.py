import pandas as pd

class Gerenciador_xlsx:
    def __init__(self, arquivo):
          self.arquivo = arquivo

    def converte_json(self):
            
            #decodifica os bytes em estrutura Excel
            df = pd.read_excel(self.arquivo)

            # 'records' orienta a criação de uma lista de objetos JSON
            # 'indent' adiciona indentação para melhor legibilidade

            arquivo_json = df.to_json('arquivo json', orient='records', indent=4)
            return arquivo_json