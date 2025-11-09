"""
1) Crie um programa que permita cadastrar nomes de alunos em uma lista.
 Implemente as funções:

cadastrar_aluno(nome, lista) ? adiciona um nome na lista.

buscar_aluno(nome, lista) ? retorna se o aluno está cadastrado.

listar_alunos(lista) ? mostra todos os alunos cadastrados.


O programa deve permitir ao usuário escolher ações em um menu até digitar “sair”
"""

listaDeAlunos: list[str] = []

def cadastrar_aluno(nome: str, lista: list) -> None:
    """adiciona um nome na lista"""
    lista.append(nome.capitalize())

def buscar_aluno(nome: str, lista: list) -> None:
    """retorna se o aluno está cadastrado"""
    if nome.lower() in (aluno.lower() for aluno in lista):
        print(f"Aluno '{nome}' cadastrado")
    else:
        print("Aluno não cadastrado")


def listar_alunos(lista:list[str]) -> None:
    """adiciona um nome na lista"""
    print("Alunos: ")
    for index, aluno in enumerate(lista, start=1):
        print(f"{index} - {aluno}")

def listar_funcoes() -> int:
    """
    Lista as opcoes possíveis
    :return: opcao selecionada
    """
    opcao: int = int(input("""
    Pressione o número da opcao que você quer selecionar: 
    1 - cadastrar aluno
    2 - buscar aluno
    3 - listar alunos
    4 - sair
    """))
    return opcao

while True:
    try:
        opcaoSelecionada: int = listar_funcoes()
        match opcaoSelecionada:
            case 1:
                nome: str = input("Digite o nome do aluno que quer cadastrar: \n")
                cadastrar_aluno(nome, listaDeAlunos)
            case 2:
                nome: str = input("Digite o nome do aluno que quer buscar: \n")
                buscar_aluno(nome, listaDeAlunos)
            case 3:
                listar_alunos(listaDeAlunos)
            case 4:
                break
            case _:
                print("Opcao inválida")
    except:
        print("Opcao inválida")