"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user():
    """
    Замените pass на ваш код
    """
    try:
        while True:
            response = input("Как дела? ")
            if response.lower() == "хорошо":
                break
    except KeyboardInterrupt:
        print('Работа программы завершена. Пока!')

if __name__ == "__main__":
    hello_user()
