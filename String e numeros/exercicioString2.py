
#Escreva um programa que solicite uma frase ao usuário
# e escreva a frase toda em maiúscula e sem espaços em branco.

frase = input("digite uma frase: ")

frase = frase.upper()
frase = frase.replace(" ","")
print(frase)