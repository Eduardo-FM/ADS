"""
Peça ao usuário uma lista de números e mostre a lista invertida (sem usar funções prontas como reverse() ou [::-1]).
"""

qtd = int(input("Quantos números deseja digitar? "))

numeros = []
for i in range(qtd):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

invertida = []
for i in range(len(numeros) - 1, -1, -1):
    invertida.append(numeros[i])

print("Lista original:", numeros)
print("Lista invertida:", invertida)