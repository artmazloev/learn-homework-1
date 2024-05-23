"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

questions_and_answers = {
    "Как дела?": "Хорошо!",
    "Что делаешь?": "Программирую",
    "Как тебя зовут?": "Меня зовут Артур",
    "Сколько тебе лет?": "Мне 36 лет",
    "Где ты живешь?": "Я живу в Москве",
    "Какая сегодня погода?": "Сегодня солнечно и тепло",
    "Что тебе нравится?": "Мне нравится читать книги и заниматься спортом",
    "Какой твой любимый цвет?": "Мне нравится синий",
    "Что ты умеешь?": "Я умею программировать, готовить и играть на гитаре",
    "Ты человек?": "Да, я человек",
    "Можешь рассказать анекдот?":
    "Конечно! Почему компьютер не любит прогулки? Потому что боится получить вирус!",
    "Какая твоя любимая еда?": "Я люблю пиццу",
    "Сколько планет в Солнечной системе?": "Восемь",
    "Какое сегодня число?": "Не знаю",
}


def ask_user(answers_dict):
    """
    Замените pass на ваш код
    """
    first_question = (input("Задайте свой вопрос: ")).capitalize()

    while first_question in questions_and_answers:
        print(questions_and_answers[first_question])
        first_question = (input("Следующий вопрос: ")).capitalize()
    


if __name__ == "__main__":
    ask_user(questions_and_answers)
