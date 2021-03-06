import telebot
import requests
import time


token = ''
chat_id = -1001228160397
# chat_id = 318882951
bot = telebot.TeleBot(token)


def check_petrovich():
    headers = requests.utils.default_headers()
    headers['User-Agent'] = 'petrovich-helper-bot'
    try:
        r = requests.get("https://petrovich.ru/", headers=headers)
        if r.status_code != 200:
            bot.send_message(chat_id, 'Ошибка ' + str(r.status_code) + ' на сайте *Петрович*', parse_mode="Markdown")
    except requests.exceptions.ConnectionError as error:
        bot.send_message(chat_id, error)


def check_b2b():
    headers = requests.utils.default_headers()
    headers['User-Agent'] = 'petrovich-helper-bot'
    try:
        r = requests.get("https://b2b.stdp.ru/", headers=headers)
        if r.status_code != 200:
            bot.send_message(chat_id, 'Ошибка ' + str(r.status_code) + ' на сайте *Б2Б*', parse_mode="Markdown")
    except requests.exceptions.ConnectionError as error:
        bot.send_message(chat_id, error)


def check_propetrovich():
    headers = requests.utils.default_headers()
    headers['User-Agent'] = 'petrovich-helper-bot'
    r = requests.get("https://propetrovich.ru/", headers=headers)
    if r.status_code != 200:
        bot.send_message(chat_id, 'Ошибка ' + str(r.status_code) + ' на сайте *Биржа профессионалов*', parse_mode="Markdown")
    pass


def check_petrovichclub():
    headers = requests.utils.default_headers()
    headers['User-Agent'] = 'petrovich-helper-bot'
    r = requests.get("https://petrovichclub.ru/", headers=headers)
    if r.status_code != 200:
        bot.send_message(chat_id, 'Ошибка ' + str(r.status_code) + ' на сайте *Клуб Друзей Петровича*', parse_mode="Markdown")
    pass


def check_time_petrovich():
    headers = requests.utils.default_headers()
    headers['User-Agent'] = 'petrovich-helper-bot'
    r = requests.get("https://petrovich.ru/", headers=headers).elapsed.total_seconds()
    if r > 5:
        bot.send_message(chat_id, 'Время ответа сервера *Петрович* ' + str(round(r, 2)) + ' s', parse_mode="Markdown")
    pass


def check_time_b2b():
    headers = requests.utils.default_headers()
    headers['User-Agent'] = 'petrovich-helper-bot'
    r = requests.get("https://b2b.stdp.ru/", headers=headers).elapsed.total_seconds()
    if r > 5:
        bot.send_message(chat_id, 'Время ответа сервера *Б2Б* ' + str(round(r, 2)) + ' s', parse_mode="Markdown")
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