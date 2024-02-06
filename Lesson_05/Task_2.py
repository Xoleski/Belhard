# Сделать калькулятор:
# у пользователя спрашивается число,
# потом действие
# и второе число

try:
    a = float(input("Введите первое число: "))
    c = input("Введите действие: ")
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
    print("Делить на ноль нельзя!")
except ValueError as ex:
    print("Нужно вводить числа!")
except KeyError as exp:
    print("Допустимый ввод действий: +, -, *, /, **, %!")
