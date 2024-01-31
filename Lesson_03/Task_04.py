# Пользователь вводит 3 числа,
# сказать сколько из них положительных
# и сколько отрицательных

number_input = input("Введите три числа через пробел: ")

number_1 = float(number_input.split()[0]) > 0
number_2 = float(number_input.split()[1]) > 0
number_3 = float(number_input.split()[2]) > 0

true_count = number_1 + number_2 + number_3
false_count = 3 - true_count # нужно через знаки, потому что ноль

print(f"\nКоличество положительных чисел = {true_count}.")
print(f"Количество отрицательных чисел = {false_count}.")
