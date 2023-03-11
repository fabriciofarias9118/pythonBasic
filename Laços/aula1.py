# Laço whilw - enquanto

x = 0
y = 0
print("teste 1")
while x <= 10 and y <= 10:
    print(x)
    x = x+1
    y = y+2
print("fim")

y = 0
print("teste 2")
while True:
    y += 1
    print(y)
    if y >= 5:
        break# encerra o laço
    else:
        continue #volta ao inicio do laço
    print("teste")
print("fim")