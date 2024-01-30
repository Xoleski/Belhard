# Пользователь вводит предложение,
# заменить все пробелы на "-"
# 2-мя способами

input_line = input("Напишите предложение...")
print(input_line)



change_line = input_line.replace(" ", "-")
print(change_line)

change_line_2 = input_line.split()
print(change_line_2)


