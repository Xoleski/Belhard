# Дан список рандомных чисел, необходимо отсортировать его в виде, сначала
# четные, потом нечётные

def sort_chet_l(list_b: list):
    list_b = (list(filter(lambda x: not x % 2, list_b))
              + list(filter(lambda x: x % 2, list_b)))
    b = list(filter(lambda x: not x, list_b))
    i = 0
    while i < len(b):
        list_b.remove(b[i])
        i += 1
    return list_b


ch_nch = [85, 87, 96, 24, 50, 0, 0]
print(sort_chet_l(ch_nch))
