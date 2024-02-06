# Сделать калькулятор:
# у пользователя спрашивается число,
# потом действие
# и второе число

try:
    a = float(input("Введите первое число: "))
    c = input("Введите действие (+, -, *, /, **, %): ")
    b = float(input("Введите второе число: "))
    act = {
        "+": a + b,
        "-": a - b,
        "*": a * b,
        "/": a / b,
        "**": a ** b,
        "%": a % b
    }

    print(f"РЕЗУЛЬТАТ = {act[c]}")


except ZeroDivisionError as exc:
    print("ОШИБКА! Делить на ноль нельзя!")
except ValueError as exc:
    print("ОШИБКА! Нужно вводить числа цифрами!")
except KeyError as exc:
    print("ОШИБКА! Допустимый ввод действий: +, -, *, /, **, %!")



## ВАРИАНТ С ЦИКЛАМИ

# er_1 = "ОШИБКА! Делить на ноль нельзя!"
# er_2 = "ОШИБКА! Допустимый ввод действий: +, -, *, /, **, %!"
# er_3 = "ОШИБКА! Нужно вводить числа цифрами!"
#
# try:
#     a1 = float(input("Введите первое число: "))
#     c1 = input("Введите действие (+, -, *, /, **, %): ")
#     b1 = float(input("Введите второе число: "))
#
#     if c1 == "+":
#         rez = a1 + b1
#     elif c1 == "-":
#         rez = a1 - b1
#     elif c1 == "*":
#         rez = a1 * b1
#     elif c1 == "/":
#         if not b1:
#             rez = er_1
#         else:
#             rez = a1 / b1
#     elif c1 == "**":
#         rez = a1 ** b1
#     elif c1 == "%":
#         rez = a1 % b1
#     else:
#         rez = er_2
#     print(f"РЕЗУЛЬТАТ = {rez}" if not (rez == er_1 or rez == er_2) else f"{rez}")
#
# except ValueError as exc:
#     print(er_3)
