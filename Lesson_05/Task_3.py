# Вывести четные числа от 2 до N по 5 в строку

n = 14

lis = [i for i in range(2, n+1) if not i % 2]

d = 0

while d < len(lis):
    if len(lis) > 5:
        print(lis[d:(d+5)])
    d += 5
