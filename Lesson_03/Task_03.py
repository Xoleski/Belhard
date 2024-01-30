# Пользователь вводит Имя, Возраст и Город,
# сформировать приветственное сообщение
# путем форматирования
# 3-мя способами

name = input("Введите имя: ")
age = input("Введите возраст: ")
city = input("Введите город: ")

hi_message = "Меня зовут %s. Мне %s лет. Я из города %s." % (name, age, city)
print(hi_message)

hi_message_02 = "Меня зовут {name}. Мне {age} лет. Я из города {city}.".format(name=name, age=age, city=city)
print(hi_message_02)

hi_message_03 = f"Меня зовут {name}. Мне {age} лет. Я из города {city}."
print(hi_message_03)
