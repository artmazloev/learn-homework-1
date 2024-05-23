"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
products = [
    {
        'product': 'iPhone 12',
        'items_sold':
        [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]
    },
    {
        'product': 'Xiaomi Mi11',
        'items_sold':
        [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]
    },
    {
        'product': 'Samsung Galaxy 21',
        'items_sold':
        [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]
    },
]


def main():
  """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
  sum_count = 0
  count_of_sales = 0

  for product in products:
    print(f"Модель телефона: {product['product']}")
    print(f"    Сумма продаж:{sum(product['items_sold'])}")
    sum_count += sum(product['items_sold'])
    print(
        f"    Средняя продажа:{round(sum(product['items_sold']) / len(product['items_sold']), 2)}"
    )
    count_of_sales += len(product['items_sold'])
  return print(
      f"Суммарное количество продаж: {sum_count} \nСреднее количество продаж: {round((sum_count / count_of_sales), 2)}"
  )


if __name__ == "__main__":
  main()
