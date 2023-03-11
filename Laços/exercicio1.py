#ler um numero entre 0 e 10
# e continuar pedido se o numero for invalido

while True:
    num = int(input("digite um numero entre 0 e 10: "))
    if num >= 0 and num <= 10:
        print("Nota valida!")
        break
    else:
        print("nota invalida! tente novamente.")

print(num)