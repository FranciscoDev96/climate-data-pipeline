import requests
import json
import os
from datetime import datetime

API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise ValueError("API_KEY não encontrada. Configure a variável de ambiente.")
CITY = "Campinas"

url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(url)

print(response.status_code)
print(response.text)

if response.status_code == 200:
    data = response.json()

    filename = f"data/raw/weather_{datetime.now()}.json"

    with open(filename, "w") as f:
        json.dump(data, f)

    print("Dados salvos com sucesso!")

else:
    print("Erro na requisição")