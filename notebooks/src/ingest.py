import requests
import json
from datetime import datetime

API_KEY = "51a2c970f6a1ffaf3112a95e831c7953"
CITY = "Campinas"

url = f"https://api.openweathermap.org/data/2.5/weather?q={"CAMPINAS"}&appid={"51a2c970f6a1ffaf3112a95e831c7953"}&units=metric"

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