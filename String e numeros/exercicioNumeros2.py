
# Escreva um programa que receba o salário
# de um funcionário (float), e retorne o resultado do
# novo salário com reajuste de 35%

salario = float(input(" digite o salario: "))

salario = salario + (35/100) *salario
print(f" salario reajustado é: {salario}")