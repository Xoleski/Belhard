# Пользователь вводит 3 числа,
# найти среднее арифмитическое
# с точностью 3

numbers_list = input("Введите три числа через пробел: ")
print(numbers_list)

arithmetic_mean = ((float(numbers_list.split()[0])
                   + float(numbers_list.split()[1])
                   + float(numbers_list.split()[2]))
                   / 3)

print(arithmetic_mean)




