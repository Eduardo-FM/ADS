"""
10 - Um sistema de votação armazena votos em uma lista:

votos = ["Maria", "João", "Maria", "Ana", "João", "Maria", "Ana", "Maria"]

Crie um programa que: Conte os votos de cada candidato; Mostre o vencedor da eleição; Exiba o percentual de votos que cada candidato obteve.


"""
votos = ["Maria", "João", "Maria", "Ana", "João", "Maria", "Ana", "Maria"]

contagem_votos = {}
for candidato in votos:
    if candidato in contagem_votos:
        contagem_votos[candidato] += 1
    else:
        contagem_votos[candidato] = 1

print("Votos de cada candidato:")
for candidato, qtd in contagem_votos.items():
    print(f"- {candidato}: {qtd} votos")

vencedor = max(contagem_votos, key=contagem_votos.get)
print(f"\nVencedor da eleição: {vencedor}")

total_votos = len(votos)
print("\nPercentual de votos de cada candidato:")
for candidato, qtd in contagem_votos.items():
    percentual = (qtd / total_votos) * 100
    print(f"- {candidato}: {percentual:.2f}%")
