import telebot
import requests
import time


token = '595308349:AAE9f0xyzRWc21o0jLlbiB5ixXgiQB8ilkA'
chat_id = 318882951
bot = telebot.TeleBot(token)


def check_petrovich():
    r = requests.get("https://petrovich.ru/")
    if r.status_code != 200:
        bot.send_message(chat_id, 'Ошибка ' + str(r.status_code) + ' на сайте Петрович')
    pass


def check_b2b():
    r = requests.get("https://petrovich.ru/")
    if r.status_code != 200:
        bot.send_message(chat_id, 'Ошибка ' + str(r.status_code) + ' на сайте Б2Б')
    pass


def check_time():
    r = requests.get("https://b2b.stdp.ru/").elapsed.total_seconds()
    if r > 1:
        bot.send_message(chat_id, 'Время ответа сервера ' + str(r) + ' s')
    pass

    time.sleep(5)

while True:
    check_petrovich()
    check_b2b()
    check_time()