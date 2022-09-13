import telebot
import config
from extensions import APIException, ExchangeRates

my_bot = telebot.TeleBot(config.BOT_TOKEN)
# available_currencies = ['EUR', 'USD', 'BYN']
available_currencies = ExchangeRates().get_list_of_currencies()


@my_bot.message_handler(commands=['values'])
def send_allowed_currencies(message: telebot.types.Message):
    list_of_supported_currencies = ', '.join(available_currencies)
    my_bot.send_message(message.chat.id, list_of_supported_currencies)


@my_bot.message_handler(commands=['start', 'help'])
def send_welcome(message: telebot.types.Message):
    # print(message.text)
    my_bot.send_message(message.chat.id,
                        '<currency, you you to convert from>\n'
                        '<currency, you you to convert to>\n'
                        '<value of first currency to change>\n'
                        'for example to change USD to EUR: EUR USD 100\n'
                        'list of available currencies /values')
    # bot.reply_to(message, f"Welcome, {message.chat.username}")


@my_bot.message_handler(content_types=['text'])
def send_do_job(message: telebot.types.Message):
    try:
        input_list = message.text.split()
        if len(input_list) < 3:
            raise APIException(my_bot, message, 'Wrong number of arguments. 3 args are expected.')
            # my_bot.reply_to(message, f'your input: {message.text}')
        for _ in (0, 1):
            if input_list[_].upper() not in available_currencies:
                raise APIException(my_bot, message, f'Wrong {_ + 1} currency. Must be from a list. See /values')
        if not input_list[2].isdigit():
            raise APIException(my_bot, message, '3d parameter must be integer.')
    except APIException as e:
        print(e)
    else:
        base_, quote_, amount_ = input_list[0].upper(), input_list[1].upper(), int(input_list[2])
        price_ = ExchangeRates().get_price(base=base_, quote=quote_, amount=amount_)
        my_bot.reply_to(message, f"You need {price_} of {quote_} to buy {amount_} of {base_}")


my_bot.polling(none_stop=True)
# rates = ExchangeRates()
# print(len(ExchangeRates().get_list_of_currencies()))
