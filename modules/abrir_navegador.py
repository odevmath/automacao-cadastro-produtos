from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def abrir_site(url: str):
    """
    Inicializa o navegador Chrome, acessa a URL fornecida e retorna o driver.

    Args:
        url (str): URL do site a ser acessado.

    Returns:
        webdriver.Chrome: Instância do driver do navegador.
    """
    options = Options()
    # Abre em tela cheia (você pode mudar)
    options.add_argument('--start-maximized')
    # options.add_argument('--headless')  # Descomente essa linha para rodar em segundo plano (sem abrir o navegador)

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(url)
    return driver
