from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from modules.utils import delay, esperar_elemento
import pandas as pd

def preencher_formulario(driver, produto):
    # Preenche os campos um a um
    esperar_elemento(driver, By.ID, "codigo").send_keys(str(produto['codigo']))
    driver.find_element(By.ID, "marca").send_keys(str(produto['marca']))
    driver.find_element(By.ID, "tipo").send_keys(str(produto['tipo']))
    driver.find_element(By.ID, "categoria").send_keys(str(produto['categoria']))
    driver.find_element(By.ID, "preco_unitario").send_keys(str(produto['preco_unitario']))
    driver.find_element(By.ID, "custo").send_keys(str(produto['custo']))
    
    # Trata 'obs' vazio ou NaN
    obs = "" if pd.isna(produto['obs']) else str(produto['obs'])
    campo_obs = driver.find_element(By.ID, "obs")
    campo_obs.send_keys(obs)

    delay(1)  # Espera breve antes de enviar

    # Envia com ENTER no campo 'obs'
    campo_obs.send_keys(Keys.ENTER)

    delay(2)  # Aguarda a submissão antes do próximo item
