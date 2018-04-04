import telebot
import requests
import time


token = '595308349:AAE9f0xyzRWc21o0jLlbiB5ixXgiQB8ilkA'
chat_id = -1001228160397
# chat_id = 318882951
bot = telebot.TeleBot(token)


def check_petrovich():
    headers = requests.utils.default_headers()
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    r = requests.get("https://petrovich.ru/", headers=headers)
    if r.status_code != 200:
        bot.send_message(chat_id, 'Ошибка ' + str(r.status_code) + ' на сайте Петрович')
    pass


def check_b2b():
    headers = requests.utils.default_headers()
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    r = requests.get("https://b2b.stdp.ru/", headers=headers)
    if r.status_code != 200:
        bot.send_message(chat_id, 'Ошибка ' + str(r.status_code) + ' на сайте Б2Б')
    pass


def check_propetrovich():
    headers = requests.utils.default_headers()
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    r = requests.get("https://propetrovich.ru/", headers=headers)
    if r.status_code != 200:
        bot.send_message(chat_id, 'Ошибка ' + str(r.status_code) + ' на сайте Пропетрович')
    pass


def check_petrovichclub():
    headers = requests.utils.default_headers()
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    r = requests.get("https://petrovichclub.ru/", headers=headers)
    if r.status_code != 200:
        bot.send_message(chat_id, 'Ошибка ' + str(r.status_code) + ' на сайте Клуб Друзей Петровича')
    pass


def check_time_petrovich():
    headers = requests.utils.default_headers()
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    r = requests.get("https://petrovich.ru/", headers=headers).elapsed.total_seconds()
    if r > 5:
        bot.send_message(chat_id, 'Время ответа сервера Петрович ' + str(r) + ' s')
    pass


def check_time_b2b():
    headers = requests.utils.default_headers()
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    r = requests.get("https://b2b.stdp.ru/", headers=headers).elapsed.total_seconds()
    if r > 5:
        bot.send_message(chat_id, 'Время ответа сервера Б2Б ' + str(r) + ' s')
    pass


while True:
    time.sleep(30)
    check_petrovich()
    check_b2b()
    check_propetrovich()
    check_petrovichclub()
    check_time_petrovich()
    check_time_b2b()