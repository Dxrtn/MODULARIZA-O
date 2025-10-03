# Q6 - Conversor de Moedas
# Crie a função que converte reais para dólares e dólares para reais (arquivo conversor.py)
# real_para_dolar e dolar_para_real. Caso o usuário não passe o tipo (real_para_dolar ou dolar_para_real) o default deve ser real_para_dolar <- padrão

import cambio
import os

def menu():
    print("Selecione 1 para converter de real para dólar\n")
    print("Selecione 2 para converter de dólar para real\n")
    print("Selecione 0 encerrar\n\n")


while True:
    menu()
    option = input("Opção: ")
    match option:
        case "1":
            os.system("cls")
            valor = float(input("Digite o valor em real: "))
            cotacao = float(input("Digite a cotação do dólar: "))
            convert = cambio.real_para_dolar(valor, cotacao)
            print(f"{valor} reais equivale a {convert} dólares.\n")
        case "2":
            os.system("cls")
            valor = float(input("Digite o valor em dólar: "))
            cotacao = float(input("Digite a cotação do dólar: "))
            convert = cambio.dolar_para_real(valor, cotacao)
            print(f"{valor} dólares equivale a {convert} reais.\n")
        case "0":
            os.system("cls")
            break
        case _:
            os.system("cls")
            valor = float(input("Digite o valor em real: "))
            cotacao = float(input("Digite a cotação do dólar: "))
            convert = cambio.real_para_dolar(valor, cotacao)
            print(f"{valor} reais equivale a {convert} dólares.\n")