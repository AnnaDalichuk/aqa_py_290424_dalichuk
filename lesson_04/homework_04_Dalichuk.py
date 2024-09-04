adventures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

adventures_of_tom_sawer = adventures_of_tom_sawer.replace("\n", " ")
print(adventures_of_tom_sawer)


# task 02 ==
""" Замініть .... на пробіл
"""
adventures_of_tom_sawer = adventures_of_tom_sawer.replace("....", " ")
print(adventures_of_tom_sawer)
# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adventures_of_tom_sawer_split = adventures_of_tom_sawer.split()
adventures_of_tom_sawer = ' '.join(adventures_of_tom_sawer_split)
print(adventures_of_tom_sawer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
quantity_of_h = list(adventures_of_tom_sawer).count("h")
print(f"Кількість літер 'h' становить: {quantity_of_h}")

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
i = 0
for letter in list(adventures_of_tom_sawer):
    if letter.isupper() is True:
        i = i + 1
    else:
        continue
print(f"There are {i} words starting with capital letter")


# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
Tom_index = adventures_of_tom_sawer.replace("Tom", "xxx", 1).index("Tom")
print(f"Tom's place is {Tom_index}")


# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adventures_of_tom_sawer_sentences = adventures_of_tom_sawer.split(".")
print(adventures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print(adventures_of_tom_sawer_sentences[3])
print(adventures_of_tom_sawer_sentences[3].lower())

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
print("By the time" in adventures_of_tom_sawer)

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
last_sentence = adventures_of_tom_sawer_sentences[-2].strip().split()
number_of_words = len(last_sentence)
print(number_of_words)
