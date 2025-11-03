"""
8 - Considere a lista de filmes e suas avaliações:

filmes = [

    ["Interestelar", 9.5],

    ["A Origem", 9.0],

    ["Matrix", 8.8],

    ["Avatar", 7.5],

    ["Duna", 8.2]

]

Crie um algoritmo que: Permita adicionar novas avaliações; Calcule a média geral das avaliações; Liste apenas os filmes com nota acima da média.
"""

filmes = [
    ["Interestelar", 9.5],
    ["A Origem", 9.0],
    ["Matrix", 8.8],
    ["Avatar", 7.5],
    ["Duna", 8.2]
]

while True:
    adicionar = input("Deseja adicionar um novo filme? (s/n): ").lower()
    if adicionar == "s":
        nome = input("Nome do filme: ")
        nota = float(input("Avaliação do filme (0 a 10): "))
        filmes.append([nome, nota])
    else:
        break

soma_notas = sum(f[1] for f in filmes)
media = soma_notas / len(filmes)
print(f"\nMédia geral das avaliações: {media:.2f}")

print("\nFilmes com nota acima da média:")
for nome, nota in filmes:
    if nota > media:
        print(f"- {nome} ({nota})")
