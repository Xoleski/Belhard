# Без использования collections, написать программу,
# которая будет создавать словарь для подсчитывания
# количества вхождений каждой буквы в текст введенный с клавиатуры

fraza = input("Введите любую фразу: ")

buk = list(fraza)
buk_set = sorted(list(set(buk)))
n = len(buk_set)

col_e = [buk.count(buk[buk.index(buk_set[i])]) for i in range(n)]

some_list = [[buk_set[i], col_e[i]] for i in range(n)]

counter_of_letters = dict(some_list)
print(counter_of_letters)