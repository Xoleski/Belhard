# Написать функцию перевода десятичного числа в двоичное и обратно, без
# использования функции int

def vb(fra):
        def bin_in(fra):
            k = []
            v = fra
            while v:

                a = v % 2
                k.append(a)
                v = v // 2

            k.reverse()
            l = "".join(list(map(str, k)))

            return l

        def bin_out(fra):
            i = 0

            while bin_in(i) != fra:
                i += 1

            return i

        if isinstance(fra, int):
            return bin_in(fra)
        else:
            return bin_out(fra)


print(a := vb(13))
print(b := vb("100101"))

