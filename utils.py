import csv
from datetime import datetime

def salvar_historico(preco):
    with open("data/historico.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), preco])

def log(msg):
    print(f"[LOG] {msg}")