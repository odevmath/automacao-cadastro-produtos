import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def delay(segundos=2):
    time.sleep(segundos)


def esperar_elemento(driver, by, valor, timeout=10):
    """Espera até que o elemento esteja visível na tela."""
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((by, valor))
    )
