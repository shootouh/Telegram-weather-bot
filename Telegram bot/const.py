TOKEN = 'your_token_here'

URL = 'https://api.telegram.org/bot{token}/{method}'

UPDATE_METH = 'getUpdates'
SEND_METH = 'sendMessage'

MY_ID = your_id_here

UPDATE_ID_FILE_PATH = 'update_id' 

try:
    with open(UPDATE_ID_FILE_PATH) as file:
        UPDATE_ID = int(file.readline().strip())
except FileNotFoundError:
    UPDATE_ID = None  # No file found, set UPDATE_ID to none.
except ValueError:
    UPDATE_ID = None  # File does not contain a valid integer.

WEATHER_TOKEN = 'your_weather_token_here'

WEATHER_URL = 'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}'
