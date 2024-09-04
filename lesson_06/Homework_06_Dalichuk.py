# task 1
"""  Уявіть, що інопланетянина з кольором alien_color щойно збили в грі.
Створіть змінну під назвою alien_color і призначте їй значення 'green', 'yellow', або 'red'.
Напишіть оператор if, щоб перевірити, чи колір прибульця 'green'.
Якщо так, надрукуйте повідомлення про те, що гравець щойно заробив 5 балів.
"""

# alien_color = input("Enter the alien color. Green, yellow or red can be chosen. \n")
# if alien_color == "green":
#     print("You earn 5 points")


# task 2
"""  Скопіюйте пеопередню відповідь, змініть і доповніть її умовою else.
Якщо колір прибульця зелений, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця не зелений, надрукуйте, що гравець щойно заробив 10 балів.
Зробіть так, щоб виводилася умова else.
"""

# alien_color = input("Enter the alien color. Green, yellow or red can be chosen. \n ")
# if alien_color == "green":
#     print("You earn 5 points")
# else:
#     print("You earn 10 points")

# task 3
# task 4
"""  Скопіюйте пеопередню відповідь, змініть і доповніть її умовою elif.
змінну під назвою alien_color перетворіть у список значень: 'green', 'yellow', 'red'
Якщо колір прибульця зелений, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця не зелений, надрукуйте, що гравець щойно заробив 10 балів.
Якщо прибулець червоний, надрукуйте повідомлення про те, що гравець заробив 15 очок
+ напишіть цикл for що перебере і обробить всі значення списку alien_color
"""

alien_color = ["green", "yellow", "red"]
for color in alien_color:
    if color == "green":
        print("You earn 5 points")
    elif color != "green":
        print("You earn 10 points")
    elif color == "red":
        print("You earn 15 points")

# task 5
"""  Начинки для піци (pizza_topping): напишіть цикл, який пропонує користувачеві ввести ряд начинок
для піци, доки він не введе значення 'quit'. Коли вони введуть кожну начинку,
надрукуйте повідомлення про те, що ви додасте цю начинку до їхньої піци.
"""

# pizza = []
# while True:
#     pizza_topping = input("Please, write the topping you would like to add. When you finish, please, type 'quit'\n Your choice is: ")
#     if pizza_topping == "quit":
#         break
#     else:
#         pizza.append(pizza_topping)
#     print(f"Your pizza will have following toppings: {pizza} .")


# task 6
"""  Напишіть програму, яка знаходить суму всіх цифр цілого числа, яке вводить користувач.
Для перебору вводу від користувача використовуйте цикл. Виведіть суму цифр числа на екран.
Приклад виконання програми:
Введіть число: 12345
Сума цифр числа 12345: 15
"""
# number = list(input("Please, enter the number: "))
# sum_of_digits = 0
# for digit in number:
#     sum_of_digits = sum_of_digits + int(digit)
# print(f"The digits' sum of the provided numer is: {sum_of_digits} .")


# task 7
"""  Потрібно написати програму, яка просить користувача ввести числа, доки він не введе 0.
Програма повинна підрахувати суму всіх введених чисел, окрім 0, і вивести її на екран.
Це повинно працювать як калькулятор, в який ввів цифру - нажав плюс - ввів наступну цифру.
Після введеня 0 показує результат сумування.
Розв'язати з використанням циклу while та break
"""
# calculated_sum = 0
# while True:
#     number = int(input("Please, print number to sum up: "))
#     if number == 0:
#         break
#     else:
#         calculated_sum = calculated_sum + number
# print(f"Sum of the provided numbers = {calculated_sum}")



# task 8
"""  З використанням циклу for реалізуйте гру "Вгадай число".
Початок програми написаний, гравець має 5 спроб відгадати випадкове число від 1 до 20,
яке було згенеровано за допомогою функції randint() модуля random.
У кожній спробі гравець вводить своє припущення, після чого програма повідомляє, чи
було припущення занадто великим або занадто малим, чи гравець вгадав число.
"""

# import random
# secret_number = random.randint(1, 20)
# guesses = 0
# max_guesses = 5
# print("Guess the number from 1 to 20. You have 5 attempts.")
# for i in range(guesses, max_guesses):
#     users_number = int(input("Please, type your number: "))
#     if users_number > secret_number:
#         print("The chosen number is too big.")
#     elif users_number < secret_number:
#         print("The chosen number is too small.")
#     else:
#         print("This guess was successful!")


# task 9
"""  Задача з використанням циклу for та continue. Задано список фруктів 'fruits'
потрібно вивести на екран всі елементи списку, окрім "orange".
"""

fruits = ["apple", "banana", "orange", "grape", "mango"]
for fruit in fruits:
    if fruit != "orange":
        continue
    else:
        fruits.remove(fruit)
print(fruits)

# task 10
"""  Задано список чисел numbers, потрібно знайти список квадратів
парних чисел зі списку. Спробуйте використати if та цикл for в один рядок.
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [i**2 for i in numbers if i % 2 ==0]
print(result)