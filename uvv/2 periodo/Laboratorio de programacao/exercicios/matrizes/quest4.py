"""
4 - Crie um sistema que permita cadastrar alunos e suas disciplinas usando uma lista de dicionários:

[

    {"nome": "Ana", "disciplinas": ["Matemática", "História"]},

    {"nome": "Carlos", "disciplinas": ["Física", "Biologia"]}

]


Implemente funções para: Adicionar um novo aluno; Adicionar ou remover disciplinas de um aluno específico; Listar todos os alunos e suas disciplinas.

"""

alunos = [{"nome": "Ana", "disciplinas": ["Matemática", "História"]}, {"nome": "Carlos", "disciplinas": ["Física", "Biologia"]}]

novoAluno = {"nome": "Eduardo", "disciplinas": ["Química", "Português"]}
nomeAluno = input("Digite o nome do aluno: ")
disciplinaParaAdicionar = input("Digite a disciplina para ser adicionada: ")
disciplinaParaRemover = input("Digite a disciplina para ser removida: ")


def adicionarAluno(aluno: object) -> None:
    alunos.append(aluno)


def adicionarDisciplina(nome: str, disciplina: str) -> None:
    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower():
            if disciplina not in aluno["disciplinas"]:
                aluno["disciplinas"].append(disciplina)
                print(f"Disciplina '{disciplina}' adicionada ao aluno '{nome}'.")
                print(f"Lista de aluno atualizadas: {alunos}") #todo colocar a funcao para printar alunos
            else:
                print(f"O aluno '{nome}' já possui essa disciplina.")
            return
    print(f"Aluno '{nome}' não encontrado.")

def removerDisciplina(nome: str, disciplina: str) -> None:
    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower():
            if disciplina in aluno["disciplinas"]:
                aluno["disciplinas"].remove(disciplina)
                print(f"Disciplina '{disciplina}' removida do aluno: {nome}.")
                print(f"Lista de aluno atualizadas: {alunos}") #todo colocar a funcao para printar alunos
            else:
                print(f"O aluno '{nome}' não possui esta disciplina.")
            return
    print(f"Aluno '{nome}' não encontrado.")

def listarAlunosEDisciplinas(alunos:  list[dict[str, str | list[str]]]) -> None:
    for aluno in alunos:
        disciplinas = ", ".join(aluno["disciplinas"])
        print(f"Aluno: {aluno['nome']}, Disciplinas: {disciplinas}")

adicionarAluno(novoAluno)
adicionarDisciplina(nomeAluno, disciplinaParaAdicionar)
removerDisciplina(nomeAluno, disciplinaParaRemover)
listarAlunosEDisciplinas(alunos)