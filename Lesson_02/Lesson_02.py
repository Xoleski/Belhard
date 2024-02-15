data = "строка в байты"
print(data.encode())
print((data_d := data.encode()).decode())
data_e = "string byte"
print(data_e.encode())

a = [1, 2**2]
b = [1, 2*2]
x = 2*2
y = 8/2

if x == y:
    print(True)
else:
    print(0)
