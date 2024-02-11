# Дан список чисел и на вход поступает число N, необходимо сместить список на
# указанное число, пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4]

def multy_list(list_n: list, n: int | float):
    return [i*n for i in list_n]


f = [2, 4, 8, 9, 13]
t = 4

print(multy_list(f, t))



