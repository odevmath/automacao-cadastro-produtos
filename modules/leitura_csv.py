import pandas as pd

def ler_dados(caminho_arquivo):
    return pd.read_csv(caminho_arquivo)