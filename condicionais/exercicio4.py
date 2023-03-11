#imprimir o maior numero

print("exibi o maior entre dois numeros")

cont = "s"

while cont == "s":
    n1 = int(input("Digite o primeiro numero: "))
    n2 = int(input("Digite o segundo numero: "))

    if n1 > n2:
        print(f" o maior é o {n1}")
    elif n1 == n2:
        print(f" {n1} e {n2} são iguais")
    else:
        print(f"O maior é {n2}")

    print("--------------------------")
    cont = input("continuar? s ou n: ")