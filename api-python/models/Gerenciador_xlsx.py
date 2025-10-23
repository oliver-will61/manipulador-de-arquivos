import pandas as pd

class Gerenciador_xlsx:
    def __init__(self, arquivo):
          self.arquivo = arquivo

    def converte_json(self):
            df = pd.read_excel(self.arquivo)
            print(df)