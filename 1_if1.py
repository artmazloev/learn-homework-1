"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""
user_input = int(input("Укажите свой возраст: "))

def main(age):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    input_age = age

    if 0 < input_age < 7:
        profession_of_user = f"Ваш возраст {input_age}. Вы посещаете детский сад"
    elif input_age >= 7 and input_age < 17:
        profession_of_user = f"Ваш возраст {input_age}. Вы посещаете школу"
    elif input_age >= 17 and input_age <= 21:
        profession_of_user = f"Ваш возраст {input_age}. Вы учитесь в ВУЗе"
    elif 21 < input_age < 70:
        profession_of_user = f"Ваш возраст {input_age}. Вы работаете"
    elif input_age >= 70:
        profession_of_user = f"Ваш возраст {input_age}. Возможно вы уже на пенсии"
    else:
        profession_of_user = f"Ваш возраст {input_age}. Мне сложно сказать чем вы занимаетесь. Попробуйте снова"
    
    return profession_of_user


if __name__ == "__main__":
    age_of_user = main(user_input)
    print(age_of_user)

