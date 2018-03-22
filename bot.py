#подключение необходимых библиотек
import telebot
import requests
import time


def check_status():
    # идентификаторы бота и вашего с ним чата
    token = '595308349:AAE9f0xyzRWc21o0jLlbiB5ixXgiQB8ilkA'
    your_chat_id = 318882951

    # функция проверки сайта
    def check_200(hostname):
        # создаем экземпляр бота
        bot = telebot.TeleBot(token)
        # делаем запрос к сайту
        r = requests.get(hostname)
        # если что-то не в порядке уведомляем нас об этом средствами бота
        if r.status_code != 200:
            bot.send_message(your_chat_id, ' Ошибка ' + str(r.status_code) + ' на сайте Петрович')
        # возвращать нам ничего не обязательно
        else:
            pass

    # применяем функцию проверки к целевому сайту
    check_200("https://petrovich.ru/")

    time.sleep(10)

while True:
    check_status()