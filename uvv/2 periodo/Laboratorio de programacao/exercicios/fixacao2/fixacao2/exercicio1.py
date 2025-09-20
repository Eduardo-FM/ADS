"""
Peça ao usuário uma palavra e conte quantas vogais (a, e, i, o, u) ela contém.
"""

palavra: str = input("Digite uma palavra: ")
vogais: str = "aeiouAEIOU"

numVogais: int = 0

for letra in palavra:
    if letra in vogais:
        numVogais+=1

print(f"Quandidade de vogais: {numVogais}")