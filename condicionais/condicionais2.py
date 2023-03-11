print("Programa pra verificar idade e carteira de motorista")

idade = int(input("digite sua idade: "))
carteira = input("posui carteira = sim ou nao: ")

if idade >= 18 and carteira == "sim":
    print("voce ja pode dirijir!!!")
elif idade < 18 and carteira == "sim":
    print("voce não poderia ter carteira e nem dirigir")
elif idade >= 18 and carteira == "nao":
    print("voce ja pode tirar carteira")
elif idade < 18 and carteira == "nao":
    print("espere seus 18 anos para tirar carteira")
else:
    print(" input invalido")