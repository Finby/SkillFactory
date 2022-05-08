# currency bot and related function

import config
import json
import requests
from pathlib import Path
import telebot


class ExchangeRates:
    def __init__(self):
        if config.API_TOKEN:
            self.api_key = config.API_TOKEN
        else:
            raise Exception("exchangerates site API token is not found")
        self.headers = {"apikey": self.api_key}
        self.payload = {}

    def get_response(self, url_: str, file_name_='') -> dict:
        # TODO: add validation of file update date that file is refreshed
        # get from API or file if file is updated today
        # update data is "cached" to file
        my_file = Path(file_name_)
        if file_name_ and my_file.is_file():   # add validation of file update date
            f = open(file_name_, 'r', encoding='utf-8')
            info = json.load(f)
            f.close()
        else:
            response = requests.request("GET", url_, headers=self.headers, data=self.payload)
            info = json.loads(response.text)
            if file_name_:
                with open(file_name_, 'w', encoding='utf-8') as f:
                    f.write(json.dumps(info, ensure_ascii=False))
        return info

    def get_list_of_currencies(self):
        url = "https://api.apilayer.com/exchangerates_data/symbols"
        file_name = 'list_of_currencies'
        response = self.get_response(url, file_name)
        return response["symbols"].keys()

    def get_price(self, base='USD', quote='RUB', amount=100):
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={quote}&from={base}&amount={amount}"
        response = self.get_response(url)
        return response["result"]


class TeleBotExceptions(Exception):
    pass


class APIException(TeleBotExceptions):
    def __init__(self, bot_: telebot.TeleBot, message_: telebot.types.Message, my_message_: str):
        self.my_chat_message = message_
        self.my_message_to_reply = my_message_
        self.my_bot = bot_
        self.my_bot.reply_to(self.my_chat_message, self.my_message_to_reply)

    def __str__(self):
        return f"for message ID {self.my_chat_message.id} was replied: {self.my_message_to_reply}"
