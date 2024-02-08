# Написать функцию перевода десятичного числа в двоичное и обратно, без
# использования функции int


def gh(numb):
    k = []
    v = numb
    while v:

        a = v % 2
        k.append(a)
        v = v // 2

    k.reverse()
    l = "".join(list(map(str, k)))

    return l


a = gh(16)
print(a)



