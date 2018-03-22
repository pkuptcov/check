#подключение необходимых библиотек
import telebot
import requests
import time


def check_status():
    # идентификаторы бота и вашего с ним чата
    token = '595308349:AAE9f0xyzRWc21o0jLlbiB5ixXgiQB8ilkA'
    your_chat_id = 318882951

    # функция проверки сайта
    def check_petrovich(hostname):
        # создаем экземпляр бота
        bot = telebot.TeleBot(token)
        # делаем запрос к сайту
        r = requests.get(hostname)
        # если что-то не в порядке, уведомляем нас об этом средствами бота
        if r.status_code != 200:
            bot.send_message(your_chat_id, 'Ошибка ' + str(r.status_code) + ' на сайте Петрович')
        # возвращать нам ничего не обязательно
        pass
        # else:
            # bot.send_message(your_chat_id, 'Ошибка ' + str(r.status_code) + ' на сайте Петрович')

    def check_b2b(hostname):
        # создаем экземпляр бота
        bot = telebot.TeleBot(token)
        # делаем запрос к сайту
        r = requests.get(hostname)
        # если что-то не в порядке уведомляем нас об этом средствами бота
        if r.status_code != 200:
            bot.send_message(your_chat_id, 'Ошибка ' + str(r.status_code) + ' на сайте Б2Б')
        # возвращать нам ничего не обязательно
        pass
        # else:
            # bot.send_message(your_chat_id, 'Ошибка ' + str(r.status_code) + ' на сайте Б2Б')

    # применяем функцию проверки к целевому сайту
    check_petrovich("https://petrovich.ru/")
    check_b2b("https://b2b.stdp.ru/")

    time.sleep(20)

while True:
    check_status()