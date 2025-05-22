import time
from services.fetch_weather import fetch_weather
from services.txt_file import create_log, logs_read
from services.excel_file import save_to_excel
from services.mysql_db import save_to_mysql
from services.mongodb import save_to_mongo
from datetime import datetime
from config import Config

CITY = input("Podaj nazwę miasta: ")
print("1. Zapisuj do pliku excel")
print("2. Zapisuj do MongoDB")
print("3. Zapisuj do MongoDB i pliku Excel")
print("4. Zapisuj do MySQL")
OPERATION = int(input("Wybierz rodzaj operacji: "))

def start():

    weather = fetch_weather(Config.API_KEY, CITY)
    create_log(
        Config.LOG_FILENAME,
        f"{datetime.now()}: Pobrano dane pogodowe miasta: {Config.CITY}\n"
    )

    match OPERATION:
        case 1:
            save_to_excel(Config.EXCEL_FILENAME, weather)
        case 2:
            save_to_mongo(weather)
        case 3:
            save_to_excel(Config.EXCEL_FILENAME, weather)
            save_to_mongo(weather)
        case 4:
            save_to_mysql(weather)
        case _:
            print("Nie rozpoznano operacji")
    # logs_read(Config.LOG_FILENAME)



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
    time.sleep(10)

