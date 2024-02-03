# obj = [1, "H", 5]
#
# # text = "Hello"
# # print(list(text))
#
# obj[1] = "First"
# print(obj)
#
# obj[1:3] = "fir"
# print(obj)

# zeros = [0 for i in range(10)] # для и в диапазоне от 0 до 100
# print(zeros)
# text = "a"
# obj = [1, "H", 5, text]

# ht = obj.pop(2)
# print(ht)
#
# obj2 = obj[0:2]
# del obj2[0:2]
#
#
# obj.remove(1) # удаляет по значению

# gtr = [2, 5, 1]
# # gtr.append(5) # один объект в конеу
# #
# # gtr.insert(0, 7)
# #
#
# # gtr.extend([5, 6, 7])
#
# print(gtr)

# aaa = [2, 7, 8, 6]
# bbb = aaa
# bbb.append(6)
# print(aaa)
#
# ccc = a[:]
# fff = aaa.copy()




# frt = gtr + gtr
#
# print(frt)

# b = (1, 2, 3)
# a = 1, 2, 3
# c = (1, )

# print(a := 15) # моржовый оператор
# print(a)

# objs = "Hello"
# a = list(objs)
# print(a)
#
# print(len(objs))
#
# # list comprehension генератор списка
# zeros = [i + 2 for i in range(3)]
# print(zeros)

# objs = [2, 1, 7, 8]
# del objs[1]
# del objs[2:]
# print(objs)

# text = "Hello"
# objs = [2, 4, 8, 9, 10, 6, 6, text]
# print(objs[-1] is text)
#
# a = objs.pop(3)
# print(a)
# print(objs)
#
# objs2 = objs[1:3]
# print(objs2)

# objs.remove(6) # удаляет по значению
# print(objs)

# from sys import  getrefcount
# a = []
# a.append(a)
# print(a)
# print(getrefcount(a)) # считает количество ссылок на объект

# a = []
# a.append(5) # добовляет сторого один элемент и добавляет его в конец
#             # за константное время
# print(a)
# a.insert(0, 6)
# print(a)


# a = [1, 3, 4, 12, 45, 89, 4]
# a.extend([5, 6, 8])
# a += [10,11,8] # = extend
# print(a)

# b = a + a
# print(b)

# l = a.index(1) # находит индекс по значению
# print(l)
# print(a.count(4))

# a = [1, 3, 4, 12, 45, 89, 4, -12]
# b = ["Hello", "python", "Age", "apple"]

# a.sort(key=abs, reverse=True)
# b.sort(key=len)
#
# print(a)
# print(b)

# b.sort(key=str.lower)
# print(b)


# s_b = sorted(b, key=str.lower, reverse=True)
# print(b)
# print(s_b)

# a = [1, 3, 4, 12, 45, 89, 4, -12]
# a.reverse()
# print(a)
# b = a[::-1]
# print(a)
# print(b)

# a = [1, 3, 4, 12, 45, 89, 4, -12, []]
# b = a[:]
# c = a.copy()
# print(a)
# print(b)
# c.append(5)
# c[-2].append(0)
# print(c)
# print(a)

# g = (1, )
#
# c = (1, 3, 4, 12, 45, [], 89, 4, -12)
#







