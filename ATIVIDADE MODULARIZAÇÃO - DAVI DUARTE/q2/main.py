# Q2 - Conversor de Temperatura
# Conversão entre Celsius e Fahrenheit
# Obrigração: criar um arquivo conversor.py e importar as funções

import conversor

print("Conversor de Temperatura")
print("1. Celsius para Fahrenheit")
print("2. Fahrenheit para Celsius")
opcao = int(input("Escolha uma opção (1 ou 2): "))

if opcao == 1:
    celsius = float(input("Digite a temperatura em Celsius: "))
    resultado = conversor.cel_fah(celsius)
    print(f"{celsius}°C equivale a {resultado:.2f}°F")
elif opcao == 2:
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    resultado = conversor.fah_cel(fahrenheit) 
    print(f"{fahrenheit}°F equivale a {resultado:.2f}°C")
else:
    print("Opção inválida.")