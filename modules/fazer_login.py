from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

def realizar_login(driver, email, senha):
    sleep(2)  # Aguarda carregamento da página

    # Preencher campo de e-mail
    campo_email = driver.find_element(By.ID, 'email')
    campo_email.clear()
    campo_email.send_keys(email)

    # Preencher campo de senha
    campo_senha = driver.find_element(By.ID, 'password')
    campo_senha.clear()
    campo_senha.send_keys(senha)

    # Enviar o formulário pressionando ENTER
    campo_senha.send_keys(Keys.ENTER)

    # Aguarda redirecionamento ou carregamento da próxima tela
    sleep(3)
