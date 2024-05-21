"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def hello_user():
    """
    Замените pass на ваш код
    """
    how_are_you = input("Как дела? ").lower()
    while how_are_you != "хорошо":
        how_are_you = input("Как дела? ").lower()
    print("Отлично! Рад, что так!")
    
if __name__ == "__main__":
    hello_user()
