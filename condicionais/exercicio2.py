#ler 4 notas e verificar se passou

c = "s"
print("*****verificar se passou ou não*****")
while (c == "s"):
    nota1 = float(input("digite sua primeira nota: "))
    nota2 = float(input("digite sua segunda nota: "))
    nota3 = float(input("digite sua terceira nota: "))
    nota4 = float(input("digite sua quarta nota: "))
    media = (nota1+nota2+nota3+nota4)/4
    
    if media >= 6:
        print("\nsua media é : ",media)
        print("Parabuens!!! Voce passou.")
    elif (media < 6) and (media>= 4):
        print("\nsua media é : ", media)
        print(" voce ficou de prova final!")
    else:
        print("\nsua media é : ", media)
        print("voce reprovou!!!")

    print("-----------------------------------")
    c = input("deseja calcular nota novamnte? s ou n: ")