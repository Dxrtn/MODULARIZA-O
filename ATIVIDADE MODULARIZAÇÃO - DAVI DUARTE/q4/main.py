# Questão 4 - Verificador de Números Pares e Ímpares
# Crie uma função que receba um número inteiro e retorne se ele é par ou ímpar.

    
numero = int(input("Digite um número: "))

def verify_even_odd(num):
    if num % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

resposta = verify_even_odd(numero)
print(resposta)