#transformar temperatura fahrenheit em celsius


print("Converter fahrenheit em celsius")
continuar = "s"
while continuar == "s":
    F = float(input("Digite a temperatura em fahrenheit: "))

    c = ((F - 32) * 5) / 9

    print(f" temperatura em celcius = {int(c)}")
    print("-----------------------------------")
    continuar = input("Nova conversão? sou n: ")