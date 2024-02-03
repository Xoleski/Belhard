# Заполнить словарь где ключами будут выступать числа от 0 до n,
# а значениями вложенный словарь с ключами "name" и "email",
# а значения для этих ключей будут браться с клавиатуры

n = 2
slovar = {[i for i in range(n+1)][p]: {"Name": input("Name: "), "Email": input("Email: ")} for p in range(n+1)}

print(slovar)
