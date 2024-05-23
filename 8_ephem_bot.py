"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import ephem

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}

planets_list = [
    'Mercury',
    'Venus',
    'Mars',
    'Jupiter',
    'Saturn',
    'Uranus',
    'Neptune',
    'Pluto',
]

command_prefix = "planet"


def check_planet(update, context):
    """
    Функция-обработчик команды /planet
    
    """
    command_parts = update.message.text.split()
    if len(command_parts) == 2: # Проверка, что введены 2 слова через пробел
        planet_name = command_parts[1].capitalize() # Наверное костыль, но это для того чтобы 
                                       # в строке с созвездием выводить только название планеты, а не все данные объекта полученного из Ephem
        planet = planet_name
        if planet_name in planets_list:
            planet = getattr(ephem, planet)()
            planet.compute()
            planet_constellation = ephem.constellation(planet)
            update.message.reply_text(
                f'Планета {planet_name} сегодня находится в созвездии {planet_constellation[1]}'
            )
        else:
            update.message.reply_text(
                'Неизвестная планета. Пожалуйста, введите латинское название одной из известных планет. Например, "/planet Mars"'
            )
    else:
        update.message.reply_text(
            "Неправильный формат команды. Используйте /planet <имя планеты>.")


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def main():
    mybot = Updater("6327846313:AAGAy9UqugKIDykdy18huM9I3g7ZSPf23Ec",
                    use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler(command_prefix, check_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
