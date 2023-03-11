#calcular
# soma-subtração
# divisão-multiplicação



c = "s"
while (c == "s"):

    a = int(input("digite um numero: "))
    operacao = input("qual a opecação: *, /, +, - : ")
    b = int(input("digite mais um numero: "))

    if operacao == "*":
        print(a*b)
    elif operacao == "/":
        print(a/b)
    elif operacao == "-":
        print(a-b)
    elif operacao == "+":
        print(a+b)
    else:
        print("!!!opração invalida!!!")
    c = input("\n\n Deseja calcular novamente? s ou n: ")