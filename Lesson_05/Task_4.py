# Пользователь вводит химическую формулу (элементы однобуквенныe и формула без скобок)
# Подсчитать количество молекул
# input: C2H5OH
# output: {"C": 2, "H": 6, "O": 1}

formula = "C2H5OH"
k = list(formula)

g =[]

i = 0

while i < len(k):
    if k[i].isalpha():
        g.extend(list(k[i]))
    elif k[i].isdigit() and k[i]:
        g.extend(list(k[i-1]*(int(k[i])-1)))
    i += 1

kor = {g[i]: g.count(g[i]) for i in range(len(g))}
print(kor)




