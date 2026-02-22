alunos = [
    {
        "Nome": "Marcos ",
        "Disciplina": [
            {"nome": "Matemática", "notas": [7.5, 8.0, 6.5]},
            {"nome": "Fisica", "notas": [8.0, 7.0]}
        ]
    },
]


def media_por_disciplina(aluno):
    medias = {}

    for disc in aluno["Disciplina"]:
        nome_disciplina = disc["nome"]
        notas = disc["notas"]
        media = sum(notas) / len(notas) if notas else 0
        medias[nome_disciplina] = media

    return medias


def media_geral_aluno(aluno):
    total_notas = 0
    qtd_notas = 0

    for disc in aluno["Disciplina"]:
        total_notas += sum(disc["notas"])
        qtd_notas += len(disc["notas"])

    return total_notas / qtd_notas if qtd_notas > 0 else 0



def media_geral(alunos):
    maior_media = -1
    aluno_top = None

    for aluno in alunos:
        total_notas = 0
        qtd_notas = 0

        for disc in aluno["Disciplina"]:
            total_notas += sum(disc["notas"])
            qtd_notas += len(disc["notas"])

        media = total_notas / qtd_notas if qtd_notas > 0 else 0

        if media > maior_media:
            maior_media = media
            aluno_top = aluno["Nome"].strip()

    return aluno_top, maior_media

    return aluno_top, maior_media


def lista_final(alunos):
    resultado = []

    for aluno in alunos:
        nome = aluno["Nome"].strip()
        total_disciplinas = len(aluno["Disciplina"])

        total_notas = 0
        qtd_notas = 0
        for disc in aluno["Disciplina"]:
            total_notas += sum(disc["notas"])
            qtd_notas += len(disc["notas"])

        media_geral = total_notas / qtd_notas if qtd_notas > 0 else 0

        resultado.append([nome, media_geral, total_disciplinas])

    return resultado


print(media_geral(alunos))