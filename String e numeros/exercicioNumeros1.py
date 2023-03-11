# Escreva um programa que receba 2 valores do tipo inteiro x e y,
# e calcule o valor de z:
# z = ((𝑥 ** 2) + (𝑦 ** 2)) /  ((x - y) ** 2)

x = int(input("digite o valor de x: "))
y = int(input("digite o valor de y: "))
z = ((x ** 2) + (y ** 2)) / ((x - y) ** 2)
print(f" o resultado é: {z}")