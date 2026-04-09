from src.scraper import iniciar_driver, pegar_preco
from src.utils import salvar_historico, log
from src.notifier import verificar_preco
from src.config import PRECO_ALVO
import time

def executar():
    log("Iniciando monitoramento...")

    driver = iniciar_driver()

    try:
        preco = pegar_preco(driver)

        if preco:
            log(f"Preço encontrado: R$ {preco}")
            salvar_historico(preco)
            verificar_preco(preco, PRECO_ALVO)
        else:
            log("Erro ao pegar preço")

    except Exception as e:
        log(f"Erro: {e}")

    finally:
        driver.quit()

if __name__ == "__main__":
    executar()