import telebot
import requests
import time


token = '595308349:AAE9f0xyzRWc21o0jLlbiB5ixXgiQB8ilkA'
chat_id = -1001228160397
# chat_id = 318882951
bot = telebot.TeleBot(token)


def check_petrovich():
    headers = requests.utils.default_headers()
    headers['User-Agent'] = 'petrovich-helper-bot'
    r = requests.get("https://petrovich.ru/", headers=headers)
    if r.status_code != 200:
        bot.send_message(chat_id, 'Ошибка ' + str(r.status_code) + ' на сайте Петрович')
    pass


def check_b2b():
    headers = requests.utils.default_headers()
    headers['User-Agent'] = 'petrovich-helper-bot'
    r = requests.get("https://b2b.stdp.ru/", headers=headers)
    if r.status_code != 200:
        bot.send_message(chat_id, 'Ошибка ' + str(r.status_code) + ' на сайте Б2Б')
    pass


def check_propetrovich():
    headers = requests.utils.default_headers()
    headers['User-Agent'] = 'petrovich-helper-bot'
    r = requests.get("https://propetrovich.ru/", headers=headers)
    if r.status_code != 200:
        bot.send_message(chat_id, 'Ошибка ' + str(r.status_code) + ' на сайте Пропетрович')
    pass


def check_petrovichclub():
    headers = requests.utils.default_headers()
    headers['User-Agent'] = 'petrovich-helper-bot'
    r = requests.get("https://petrovichclub.ru/", headers=headers)
    if r.status_code != 200:
        bot.send_message(chat_id, 'Ошибка ' + str(r.status_code) + ' на сайте Клуб Друзей Петровича')
    pass


def check_time_petrovich():
    headers = requests.utils.default_headers()
    headers['User-Agent'] = 'petrovich-helper-bot'
    r = requests.get("https://petrovich.ru/", headers=headers).elapsed.total_seconds()
    if r > 5:
        bot.send_message(chat_id, 'Время ответа сервера Петрович ' + str(r) + ' s')
    pass


def check_time_b2b():
    headers = requests.utils.default_headers()
    headers['User-Agent'] = 'petrovich-helper-bot'
    r = requests.get("https://b2b.stdp.ru/", headers=headers).elapsed.total_seconds()
    if r > 5:
        bot.send_message(chat_id, 'Время ответа сервера Б2Б ' + str(r) + ' s')
    pass


while True:
    time.sleep(10)
    check_petrovich()
    time.sleep(1)
    check_b2b()
    time.sleep(1)
    check_propetrovich()
    time.sleep(1)
    check_petrovichclub()
    time.sleep(1)
    check_time_petrovich()
    time.sleep(1)
    check_time_b2b()
    time.sleep(1)