# Пользователь вводит химическую формулу (элементы однобуквенныe и формула без скобок)
# Подсчитать количество молекул
# input: C2H5OH
# output: {"C": 2, "H": 6, "O": 1}

formula = "C12H22O11"
k = list(formula)

g =[]

i = 0

while i < len(k):
    if k[i].isalpha():
        g.extend(list(k[i]))
    elif k[i-1].isdigit() and k[i].isdigit():
        g.extend(list(k[i-2]*(int(k[i-1]+k[i])-1)))
    elif k[i].isdigit() and k[i+1].isalpha():
        g.extend(list(k[i-1]*(int(k[i])-1)))
    i += 1

kor = {g[i]: g.count(g[i]) for i in range(len(g))}
print(kor)




