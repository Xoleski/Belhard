# Написать функцию перевода десятичного числа в двоичное и обратно, без
# использования функции int

def vb(numb: int | str):
    def bin_in(dec: int):
        k = []
        v = dec
        while v:
            a = v % 2
            k.append(a)
            v = v // 2
        k.reverse()
        return "".join(list(map(str, k)))

    def bin_out(dva: str):
        i = 0
        while bin_in(i) != dva:
            i += 1
        return i

    if isinstance(numb, int):
        return bin_in(numb)
    else:
        return bin_out(numb)


print(a := vb(13))
print(b := vb("100101"))


