# Без использования collections, написать программу,
# которая будет создавать словарь для подсчитывания
# количества вхождений каждой буквы в текст введенный с клавиатуры

fraza = input("Введите любую фразу: ")

# buk = sorted(set(fraza))

# slovar = {buk[i]: fraza.count(buk[i]) for i in range(len(buk))}

slovar = {fraza[i]: fraza.count(fraza[i]) for i in range(len(fraza))}
print(slovar)

# просто в словарь из текста. при повторе буквы заменит значение