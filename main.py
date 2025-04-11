from modules.abrir_navegador import abrir_site
from modules.fazer_login import realizar_login
from modules.leitura_csv import ler_dados
from modules.preenchimento_form import preencher_formulario
from modules.utils import delay, esperar_elemento
from selenium.webdriver.common.by import By


def main():
    # 1. Abrir o navegador e acessar o site
    driver = abrir_site(
        "https://dlp.hashtagtreinamentos.com/python/intensivao/login")

    # 2. Fazer login automaticamente
    realizar_login(driver, "teste@email.com", "senha@123")

    # 3. Ler os dados do CSV
    dados = ler_dados('./src/data/produtos.csv')

    # 4. Esperar o campo "codigo" aparecer após login
    esperar_elemento(driver, By.ID, "codigo")

    # 5. Preencher o formulário com os dados
    for _, linha in dados.iterrows():
        preencher_formulario(driver, linha)
        delay(1)


if __name__ == "__main__":
    main()
