ARQUIVO = "clientes.txt"

def inicializar_arquivo():
    open(ARQUIVO, "a", encoding="utf-8").close()

def cadastrar_cliente():
    nome = input("Nome: ").strip()
    email = input("E-mail: ").strip()
    telefone = input("Telefone: ").strip()

    with open(ARQUIVO, "a", encoding="utf-8") as arq:
        arq.write(f"{nome};{email};{telefone}\n")

    print("Cliente cadastrado com sucesso!")

def listar_clientes():
    print("\n--- Lista de Clientes ---")
    with open(ARQUIVO, "r", encoding="utf-8") as arq:
        linhas = arq.readlines()

    if not linhas:
        print("Nenhum cliente cadastrado.")
        return

    for linha in linhas:
        nome, email, telefone = linha.strip().split(";")
        print(f"Nome: {nome} | Email: {email} | Telefone: {telefone}")

def buscar_cliente():
    busca = input("Digite o nome para buscar: ").strip().lower()

    encontrado = False

    with open(ARQUIVO, "r", encoding="utf-8") as arq:
        for linha in arq:
            nome, email, telefone = linha.strip().split(";")
            if busca in nome.lower():
                print(f"\n➡ Encontrado:")
                print(f"Nome: {nome} | Email: {email} | Telefone: {telefone}")
                encontrado = True

    if not encontrado:
        print("Cliente não encontrado.")

def excluir_cliente():
    nome_excluir = input("Digite o nome do cliente a excluir: ").strip().lower()

    linhas_novas = []
    excluiu = False

    with open(ARQUIVO, "r", encoding="utf-8") as arq:
        for linha in arq:
            nome, email, telefone = linha.strip().split(";")
            if nome.lower() == nome_excluir:
                excluiu = True
            else:
                linhas_novas.append(linha)

    with open(ARQUIVO, "w", encoding="utf-8") as arq:
        arq.writelines(linhas_novas)

    if excluiu:
        print("Cliente excluído com sucesso!")
    else:
        print("Cliente não encontrado.")

def menu():
    inicializar_arquivo()

    while True:
        print("\n====== MENU CLIENTES ======")
        print("1 - Cadastrar cliente")
        print("2 - Listar clientes")
        print("3 - Buscar cliente")
        print("4 - Excluir cliente")
        print("5 - Sair")
        opc = input("Escolha uma opção: ")

        if opc == "1":
            cadastrar_cliente()
        elif opc == "2":
            listar_clientes()
        elif opc == "3":
            buscar_cliente()
        elif opc == "4":
            excluir_cliente()
        elif opc == "5":
            print("Encerrando sistema...")
            break
        else:
            print("Opção inválida!")

menu()
