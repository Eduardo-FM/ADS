"""
1 -
Uma universidade mantém uma lista de listas com as notas dos alunos em três provas,
por exemplo: notas = [[7.5, 8.0, 6.5], [9.0, 9.5, 8.5], [5.0, 6.0, 7.0]]
Crie um programa que:
Calcule a média de cada aluno; Mostre o aluno com maior e menor média;
Retorne a média geral da turma.

"""
notas: list[list[float]] = [[7.5, 8.0, 6.5], [9.0, 9.5, 8.5], [5.0, 6.0, 7.0]]
medias: list[float] = []

def calcMedia(notas: list[float]) -> float:
    return sum(notas) / len(notas)

medias: list[float] = [calcMedia(aluno) for aluno in notas]

print(f"O aluno com maior média tem: {max(medias)}")
print(f"O aluno com menor média tem: {min(medias)}")
print(f"Média da turma: {(sum(medias) / len(medias))}")