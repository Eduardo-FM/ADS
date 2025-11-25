alunos = []
for aluno in range(3):
    notas = []
    nome = input("Digite o nome do aluno: ")
    for index, n in enumerate(range(3)):
        nota = float(input(f"Digite o valor da nota {index + 1}: "))
        notas.append(nota)

    dic = {f"aluno": {nome}, "notas" : notas}

    alunos.append(dic)

maiorMedia = 0
alunoMaiorMedia = ''
for index, aluno in enumerate(alunos):
    print(f"Média do aluno {aluno['aluno']}: {sum(aluno['notas']) / len(aluno['notas'])}")

    if (sum(aluno['notas']) / len(aluno['notas'])) > maiorMedia:
        maiorMedia = (sum(aluno['notas']) / len(aluno['notas']))
        alunoMaiorMedia = aluno['aluno']

print(f"Aluno com maior média{alunoMaiorMedia}")