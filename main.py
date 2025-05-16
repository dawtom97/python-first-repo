import time
from services.fetch_weather import fetch_weather
from services.txt_file import create_log, logs_read
from services.excel_file import save_to_excel
from datetime import datetime
from config import Config

def start():
    weather = fetch_weather(Config.API_KEY, Config.CITY)
    create_log(
        Config.LOG_FILENAME,
        f"{datetime.now()}: Pobrano dane pogodowe miasta: {Config.CITY}\n"
    )
    logs_read(Config.LOG_FILENAME)
    save_to_excel(Config.EXCEL_FILENAME, weather)


while True:
    try:
        start()
        print("Pobrano dane")
    except Exception as e:
        print(e)
        create_log(
            Config.LOG_FILENAME,
            f"{datetime.now()}: Wystapil blad {e} podczas pobierania danych dla miasta: {Config.CITY}\n"
        )
    time.sleep(5)

