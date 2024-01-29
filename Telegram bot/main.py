import requests
import json
import time

import const


def answer_user_bot(data):
    # Function to send a message to the user or chat
    payload = {
        'chat_id': const.MY_ID,
        'text': data
    }
    url = const.URL.format(
        token=const.TOKEN,
        method=const.SEND_METH
    )
    response = requests.post(url, json=payload)
    # Check response status for potential errors
    if response.status_code != 200:
        print(f"Failed to send message. Status code: {response.status_code}")


def parse_weather_data(data):
    # Function to extract and format weather information from API response
    weather_state = data['weather'][0]['main']
    temp = round(data['main']['temp'] - 273.15, 2)
    city = data['name']
    msg = f'The weather in {city}: Temperature is {temp}°C, State is {weather_state}'
    return msg


def get_weather(location):
    # Function to retrieve weather information for a given location
    url = const.WEATHER_URL.format(city=location,
                                   token=const.WEATHER_TOKEN)
    response = requests.get(url)
    if response.status_code != 200:
        return 'City not found'
    data = response.json()  # Use .json() for better readability
    return parse_weather_data(data)


def get_message(data):
    # Function to extract the text message from the received data
    return data['message']['text']


def save_update_id(update_id):
    # Function to save the latest update_id to a file and update the constant
    with open(const.UPDATE_ID_FILE_PATH, 'w') as file:
        file.write(str(update_id))
    const.UPDATE_ID = update_id
    return True


def main():
    # Main loop to continuously check for updates and respond to messages
    while True:
        url = const.URL.format(token=const.TOKEN, method=const.UPDATE_METH) # Construct the URL for getting updates from the Telegram API
        content = requests.get(url).json() # Make a request to the Telegram API and parse the response as JSON

        result = content.get('result', []) # Extract the 'result' field from the response, which contains updates
        if result:  # Check if there are any updates
            elem = result[-1]  # Only process the most recent update
            chat_id = elem['message']['chat']['id'] # Extract chat_id and update_id from the received message
            if chat_id == const.MY_ID and const.UPDATE_ID != elem.get('update_id'): # Check if the update is for the specified chat and has a new update_id
                message = get_message(elem) # Extract the text message from the received data
                weather_msg = get_weather(message) # Get weather information based on the received message
                answer_user_bot(weather_msg) # Send the weather information as a response to the user
                save_update_id(elem['update_id']) # Save the update_id to avoid processing the same update again

        time.sleep(2)


if __name__ == '__main__':
    main()
