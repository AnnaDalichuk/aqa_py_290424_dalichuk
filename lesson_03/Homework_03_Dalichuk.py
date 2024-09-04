# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та екрануйте всі символи одинарної дужки у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк
alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don\'t much care where ——" said Alice.\n"Then it doesn\'t matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
Black_Sea_S: int = 436402
Azov_Sea_S: int = 37800
Both_Seas_S: int = Black_Sea_S + Azov_Sea_S
print("\nЗавдання 04\nЗагальна площа обох морів становить " + str(Both_Seas_S) + " км2")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
general_quantity = 375291
stock1and2 = 250449
stock2and3 = 222950

stock3 = general_quantity - stock1and2
stock1 = general_quantity - stock2and3
stock2 = general_quantity - (stock1 + stock3)
print(f'\nЗавдання 05\nНа першому складі перебуває {str(stock1)} товарів, \nна другому складі перебуває {str(stock2)} товарів, \nна третьому складі перебуває {str(stock3)} товарів')


# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

monthly_payment = 1179
print("\nЗавдання 06\nВартість компʼютеру " + str(monthly_payment*18) + " грн.")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
#dividend = input('\nЗавдання 07\nВведіть значення діленого: ')
#divisor = input('Введіть значення дільника: ')
#remainder = int(dividend) % int(divisor)
#print(f'Залишок від ділення {dividend} на {divisor} становить {remainder}')

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

large_pizza_quantity = 4
large_pizza_price = 274

medium_pizza_quantity = 2
medium_pizza_price = 218

juice_quantity = 4
juice_price = 35

cake_quantity = 1
cake_price = 350

water_quantity = 3
water_price = 21

print(f'\nЗавдання 08\nЗагальна вартість замовлення становить: {large_pizza_quantity*large_pizza_price+medium_pizza_quantity*medium_pizza_price+juice_quantity*juice_price+cake_quantity*cake_price+water_quantity*water_price} грн.')

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
photos_quantity = 232
photos_per_page = 8
print(f'\nЗавдання 09\nПотрібно буде {int(photos_quantity/photos_per_page)} сторінок')


# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

distance = 1600
fuel_tank_capacity = 48
print(f'\nЗавдання 10\nДля подорожі з Харкова до Будапешту знабиться {distance/100*9} літрів бензину')
print(f'Для подорожжі потрібно заправитися {int(distance/100*9/fuel_tank_capacity)} рази')
