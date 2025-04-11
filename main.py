import pyautogui
import pandas as pd
import time

# Importar a base de produtos
tabela = pd.read_csv("./src/produtos.csv")
print(tabela)

pyautogui.PAUSE = 0.5

# Abrir o chrome e acessar o site https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# Aguardar o carregamento da página
time.sleep(4)

# Realizar login (dados fictícios)
pyautogui.click(x=-1186, y=413)
pyautogui.write("teste@email.com")
pyautogui.press("tab")
pyautogui.write("senha@123")
pyautogui.click(x=-969, y=574)

# Percorre cada linha da tabela, em que para cada linha, cadastra um produto.
for linha in tabela.index:
    pyautogui.click(x=-1207, y=298)
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    if not pd.isna(tabela.loc[linha, "obs"]):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.click(x=-1054, y=953)
    pyautogui.scroll(5000)
