contador = 0

arquivo = open("funcionarios.txt", "at")

while True:
    nome = input("Digite o nome do funcionário (ou Enter para sair): ")

    if nome == "":
        break

    cargo = input("Digite o cargo do funcionário: ")


    arquivo.write(f"{nome} - {cargo}\n")

    contador += 1

print(f"\nTotal de funcionários cadastrados: {contador}")
