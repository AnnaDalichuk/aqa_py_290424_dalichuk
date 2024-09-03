# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    multiplier = 1
    str_to_print = ""
    while multiplier <= 10:
        result = number * multiplier
        if result > 25:
            break
        str_to_print += str(number) + "x" + str(multiplier) + "=" + str(result)+ "\n"
        multiplier += 1
    return str_to_print
print(multiplication_table(3))

# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
'''Два варіанти запису'''

def summ_function(number1, number2):
    result = number1 + number2
    return result
print(f"The summ equals {summ_function(3, 4)}.")
#OR
def summ_function2(number1, number2):
    return print(f"The summ of {number1} and {number2} equals {number1+number2}.")
summ_function2(4,5)


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def list_average(numbers):
    average = sum(numbers)/len(numbers)
    return average
numbers = [2,6,4,9]
print(f"Average of number's list is {list_average(numbers)}.")

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reversed_list(initial_str):
    return initial_str[::-1]
initial_str="Happy New Year!"
print(reversed_list(initial_str))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_word_list(words_list):
    max_length=0
    for word in words_list:
        if len(word) > max_length:
            max_length = len(word)
            longest_word = word
    return longest_word
words_list=["school", "vacation", "mother", "dad", "evacuation"]
print("The longest word in the provided list is " + longest_word_list(words_list))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

def find_substring(str1, str2):
    if str2 in str1:
        return str1.find(str2)
    else:
        return -1

# str1 = "Hello, world!"
# str2 = "world"
# print(find_substring(str1, str2))  # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))  # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
"""  task 7. Задано список фруктів 'fruits'
потрібно вивести на екран всі елементи списку, окрім "orange".
"""
def no_orange_list(fruits):
    for fruit in fruits:
        if fruit != "orange":
            continue
        else:
            fruits.remove(fruit)
    return fruits

fruits = ["apple", "banana", "orange", "grape", "mango"]
print(no_orange_list(fruits))

""" task 8. Задано список чисел numbers, потрібно знайти список квадратів
парних чисел зі списку. 
"""
def even_square(numbers):
    result = [i**2 for i in numbers if i % 2 ==0]
    return result
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(even_square(numbers))

"""  task 9. Напишіть програму, яка знаходить суму всіх цифр цілого числа. 
"""
def figures_sum(number):
    number = list(str(number))
    sum_of_digits = 0
    for digit in number:
        sum_of_digits = sum_of_digits + int(digit)
    return sum_of_digits

print(figures_sum(12345))

""" task 10. Exists some car data with color, year, engine_volume, car type , price
We have search_criteria as tuple of ( year>= , engine_volume >= , price<=)
write code that will help us to get cars that satisfy search_criteria."""

def cars_filter(car_data):
    car_dict = {}
    for car_name, car_parametr in car_data.items():
        if car_parametr[1]>=2017 and car_parametr[2]>=1.6 and car_parametr[4]<=50000:
            car_dict[car_name]=car_parametr
    return car_dict

car_data = {
    'Mercedes': ('silver', 2019, 1.8, 'sedan', 50000),
    'Audi': ('black', 2020, 2.0, 'sedan', 55000),
    'BMW': ('white', 2018, 3.0, 'suv', 70000),
    'Lexus': ('gray', 2016, 2.5, 'coupe', 45000),
    'Toyota': ('blue', 2021, 1.6, 'hatchback', 25000)
}
print(cars_filter(car_data))