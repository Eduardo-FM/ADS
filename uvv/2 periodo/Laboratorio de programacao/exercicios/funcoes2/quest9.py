"""
9 - Dada uma lista com valores repetidos:

valores = [3, 5, 3, 2, 5, 5, 7, 2, 9, 3]

Escreva um programa que: Crie uma nova lista apenas com os valores únicos, sem usar set(); Conte quantas vezes cada número apareceu; Retorne o número mais frequente e sua contagem.
"""
valores = [3, 5, 3, 2, 5, 5, 7, 2, 9, 3]

valores_unicos = []
for v in valores:
    if v not in valores_unicos:
        valores_unicos.append(v)
print("Valores únicos:", valores_unicos)

contagens = {}
for v in valores:
    if v in contagens:
        contagens[v] += 1
    else:
        contagens[v] = 1

print("\nContagem de cada número:")
for numero, qtd in contagens.items():
    print(f"{numero} apareceu {qtd} vezes")

mais_frequente = None
maior_contagem = 0

for numero, qtd in contagens.items():
    if qtd > maior_contagem:
        mais_frequente = numero
        maior_contagem = qtd

print(f"\nNúmero mais frequente: {mais_frequente} (apareceu {maior_contagem} vezes)")
