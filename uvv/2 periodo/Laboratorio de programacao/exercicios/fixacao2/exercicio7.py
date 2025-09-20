"""
Peça ao usuário uma frase e conte quantas vezes cada letra aparece (ignorar maiúsculas/minúsculas).
"""


frase = input("Digite uma frase: ")

frase = frase.lower()

contagem = {}

for char in frase:
    if char.isalpha():
        contagem[char] = contagem.get(char, 0) + 1


for letra, qtd in contagem.items():
    print(f"'{letra}' aparece {qtd} vezes")