TOKEN = '6067418029:AAFtNW-ZGd6xq22l9-qp617oO9Wi4R2Gj9s'

URL = 'https://api.telegram.org/bot{token}/{method}'

UPDATE_METH = 'getUpdates'
SEND_METH = 'sendMessage'

MY_ID = 6692595913

UPDATE_ID_FILE_PATH = 'update_id' 

try:
    with open(UPDATE_ID_FILE_PATH) as file:
        UPDATE_ID = int(file.readline().strip())
except FileNotFoundError:
    UPDATE_ID = None  # No file found, set UPDATE_ID to none.
except ValueError:
    UPDATE_ID = None  # File does not contain a valid integer.

WEATHER_TOKEN = '4b320ea9dc811c5d7c970fbfa00f3fb2'

WEATHER_URL = 'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}'
