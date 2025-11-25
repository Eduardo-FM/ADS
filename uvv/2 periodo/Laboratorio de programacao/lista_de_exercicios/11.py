
estoque = {}

while True:
    print("\n--- Menu ---")
    print("1 - Adicionar produto")
    print("2 - Consultar produto")
    print("3 - Listar estoque")
    print("4 - Sair")

    opc = input("Escolha uma opção: ")

    if opc == "1":
        nome = input("Nome do produto: ").strip()
        qtd = int(input("Quantidade: "))
        estoque[nome] = qtd
        print("Produto adicionado com sucesso!")

    elif opc == "2":
        nome = input("Digite o nome do produto para consultar: ").strip()
        if nome in estoque:
            print(f"Quantidade disponível de {nome}: {estoque[nome]}")
        else:
            print("Produto não encontrado no estoque.")

    elif opc == "3":
        print("\nEstoque atual:")
        for produto, quantidade in estoque.items():
            print(f"- {produto}: {quantidade}")

    elif opc == "4":
        print("Encerrando programa...")
        break

    else:
        print("Opção inválida! Tente novamente.")