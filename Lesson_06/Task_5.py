# Дан список чисел, необходимо его развернуть без использования метода revese и
# функции reversed, а так же дополнительного списка и среза

def rev_ls(ls_a: list):
    i = 0
    n = -1
    while i < len(ls_a)//2:
        ls_a[i], ls_a[n] = ls_a[n], ls_a[i]
        i += 1
        n += -1
    return ls_a


ch = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(rev_ls(ch))

gf = [5, 9, 1, 0, 41]
print(rev_ls(gf))
