"""
5 -
Dada uma lista com as pontuações de jogadores em um torneio: pontuacoes = [120, 350, 200, 480, 310, 90]
Crie um programa que: Organize o ranking do maior para o menor; Exiba o top 3;
Mostre a posição de um jogador com determinada pontuação informada pelo usuário.
"""

pontuacoes = [120, 350, 200, 480, 310, 90]
ranking = sorted(pontuacoes, reverse=True)
print("Ranking do maior para o menor:", ranking)
print("Top 3 jogadores:", ranking[:3])

pontuacao_usuario = int(input("Digite a pontuação do jogador para ver a posição: "))

if pontuacao_usuario in ranking:
    posicao = ranking.index(pontuacao_usuario) + 1  # +1 pois o índice começa em 0
    print(f"O jogador com {pontuacao_usuario} pontos está na posição {posicao}º do ranking.")
else:
    print("Pontuação não encontrada no ranking.")
