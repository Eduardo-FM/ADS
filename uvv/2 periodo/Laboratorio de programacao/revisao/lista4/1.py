"""
Peça ao usuário uma palavra e conte quantas vogais (a, e, i, o, u) ela contém.
"""

palavra = input("Digite uma palavra: ")
vogais = "aeiou"
qtdeVogais = 0

for letra in palavra:
    if letra.lower() in vogais:
        qtdeVogais+=1

print(qtdeVogais)