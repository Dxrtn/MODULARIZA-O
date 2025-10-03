# Questão 1 - Manipulação de listas e strings

frase = input("Digite uma frase: ")
palavra = input("Digite uma palavra para buscar: ")

frase_minuscula = frase.lower()
palavra_minuscula = palavra.lower()
palavras_frase = frase_minuscula.split()
quantidade = 0

def search_words(word, phrase, quant):
    for p in phrase:
        if p == word:
            quant += 1
    return quant

# Quantidade de Palavras
quantity = search_words(palavra_minuscula, palavras_frase, quantidade)
print(quantity)
