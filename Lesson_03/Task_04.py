# Пользователь вводит 3 числа,
# сказать сколько из них положительных
# и сколько отрицательных

number_input = input("Введите три числа через пробел: ")

number_1 = float(number_input.split()[0]) > 0
number_2 = float(number_input.split()[1]) > 0
number_3 = float(number_input.split()[2]) > 0

true_count = (str(number_1)+str(number_2)+str(number_3)).count("True")
false_count = (str(number_1)+str(number_2)+str(number_3)).count("False")

print(f"\nКоличество положительных чисел = {true_count}.")
print(f"Количество отрицательных чисел = {false_count}.")
