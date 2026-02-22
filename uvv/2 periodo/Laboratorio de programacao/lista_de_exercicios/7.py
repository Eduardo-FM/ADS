alunos = [
    {
        "Nome": "Marcos ",
        "Disciplina": [
            {"nome": "Matemática", "notas": [7.5, 8.0, 6.5]},
            {"nome": "Fisica", "notas": [8.0, 7.0]}
        ]
    },
]

numeros_encontrados = []
tipos_numericos = (int, float)

for aluno in alunos:
    for chave, valor in aluno.items():
        if isinstance(valor, tipos_numericos):
             numeros_encontrados.append(valor)
        if chave == "Disciplina":
            for disciplina in valor:
                for disc_chave, disc_valor in disciplina.items():
                    if disc_chave == "notas":
                        for nota in disc_valor:
                            if isinstance(nota, tipos_numericos):
                                numeros_encontrados.append(nota)

def mediaGeral():
    if not numeros_encontrados:
        print("Não há notas para calcular a média geral.")
        return
    media = sum(numeros_encontrados) / len(numeros_encontrados)
    print("🚀 ANÁLISE GERAL DO ALUNO")
    print(f"Média Geral (todas as notas): {media:.2f}")
    if media >= 7:
        print(f"Parabéns, você está APROVADO")
    else:
        print(f"Você está em RECUPERAÇÃO")

def mediaDisciplina():
    print("\n--- MÉDIA POR DISCIPLINA ---")
    for aluno in alunos:
        print(f"\nAluno: {aluno['Nome'].strip()}")
        for disciplina in aluno.get("Disciplina", []):
            nome_materia = disciplina["nome"]
            notas_materia = disciplina["notas"]
            if notas_materia:
                media_materia = sum(notas_materia) / len(notas_materia)
                situacao = "APROVADO" if media_materia >= 7 else "REPROVADO"
                print(f"  {nome_materia}: Média {media_materia:.2f} ({situacao})")
            else:
                print(f"  {nome_materia}: Nenhuma nota registrada.")

#print(numeros_encontrados)
mediaGeral()
#mediaDisciplina()
print("a")