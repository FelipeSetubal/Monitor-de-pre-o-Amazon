from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.config import URL, TEMPO_ESPERA

def iniciar_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("user-agent=Mozilla/5.0")

    return webdriver.Chrome(options=options)

def pegar_preco(driver):
    try:
        driver.get(URL)

        wait = WebDriverWait(driver, TEMPO_ESPERA)

        preco_elemento = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".a-price-whole"))
        )

        preco_inteiro = preco_elemento.text

        # remove ponto de milhar
        preco_inteiro = preco_inteiro.replace(".", "")

        try:
            preco_decimal = driver.find_element(By.CSS_SELECTOR, ".a-price-fraction").text
        except:
            preco_decimal = "00"

        preco = float(f"{preco_inteiro}.{preco_decimal}")

        return preco

    except Exception as e:
        print("Erro real:", e)
        return None