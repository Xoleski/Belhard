# Пользователь вводит предложение,
# заменить все пробелы на "-"
# 2-мя способами

input_line = input("Напишите предложение: ")
print(input_line)

changed_line = input_line.replace(" ", "-")
print(changed_line)

changed_line_2 = "-".join(input_line.split())
print(changed_line_2)
