import json
import os
from datetime import datetime

RAW_PATH = "data/raw"
PROCESSED_PATH = "data/processed"

os.makedirs(PROCESSED_PATH, exist_ok=True)

for file_name in os.listdir(RAW_PATH):
    if file_name.endswith(".json"):

        file_path = os.path.join(RAW_PATH, file_name)

        with open(file_path, "r") as f:
            data = json.load(f)

        cidade = data.get("name")
        temperatura = data.get("main", {}).get("temp")
        umidade = data.get("main", {}).get("humidity")
        timestamp = data.get("dt")
        vento = data.get("wind", {}).get("speed")
        weather_list = data.get("weather, []")
        descricao = weather_list[0].get("description") if weather_list else None
        sensacao = data.get("main", {}).get("feels_like")

        data_formatada = datetime.fromtimestamp(timestamp).strftime('%y-%m-%d %H:%M:%S')

        processed_data = {
            "cidade": cidade,
            "temperatura": temperatura,
            "umidade": umidade,
            "vento": vento,
            "sensacao_termina": sensacao,
            "descricao": descricao,
            "data": data_formatada

        }

        new_file_name = f"processed_{file_name}"
        new_file_path = os.path.join(PROCESSED_PATH, new_file_name)

        with open(new_file_path, "w") as f:
            json.dump(processed_data, f, indent=4)
        
        print(f"Arquivo processado: {new_file_name}")