small_list = [3, 1, 4, 5, 2, 5, 3]
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
# task 1. Знайдіть всі унікальні елементи в списку small_list
unique_in_small_list = list(set(small_list))
print(unique_in_small_list)
# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list
small_list_average: float = sum(small_list)/len(small_list)
print(small_list_average)

# task 3. Перевірте, чи є в списку big_list дублікати
if len(list(set(big_list))) < len(big_list):
    print("There are duplicates")
else:
    print("There are no duplicates")

base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict
max_value = 0
needed_key =""
for key, value in add_dict.items():
    if value > max_value:
        max_value=value
        needed_key=key
print(needed_key)


# task 5. Створіть новий словник, в якому ключі та значення будуть
# замінені місцями у заданому словнику
add_dict_new: dict[int:str] = {}
for key, value in add_dict.items():
    add_dict_new.update({value: key})
print(add_dict_new)

# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
sum_dict: dict = {}
sum_dict = base_dict | add_dict
print(sum_dict)

# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх
sum_dict: dict = {}
# for

# task 7.
line = "Створіть множину всіх символів, які входять у заданий рядок"
line_set = set(line)
print(line_set)

# task 8. Обчисліть суму елементів двох множин, які не є спільними
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}

set_sum = 0
for x in set_1.symmetric_difference(set_2):
    set_sum = set_sum + x
print(set_sum)

# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]
list1: list = [1, 2, 3, 4]
list2: list = [3, 4, 5, 6]

set3 = set(list1).symmetric_difference(set(list2))
print(set3)

person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]

# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}
# persons_dict = {'10-19': [],
#                 '20-29': [],
#                 '30-39': [],
#                 '40-49': []}


persons_dict = {}

for name, age in person_list:
    if 10 <= age <= 19:
        age_range = '10-19'
    elif 20 <= age <= 29:
        age_range = '20-29'
    elif 30 <= age <= 39:
        age_range = '30-39'
    elif 40 <= age <= 49:
        age_range = '40-49'
    else:
        continue

    if age_range not in persons_dict:
        persons_dict[age_range] = []
    persons_dict[age_range].append(name)

print(persons_dict)