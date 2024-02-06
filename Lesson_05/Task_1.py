# Вывести первые N чисел кратные M и больше K

numb = []
n = 5
m = 5
k = -5

while len(numb) < n:

    if not (k+1) % m:
        numb.append(k+1)
    k += 1

print(numb)
