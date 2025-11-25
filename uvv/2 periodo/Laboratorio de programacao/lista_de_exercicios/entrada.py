def coletar_dados():
    nome = input("Nome do aluno: ")

    notas = []
    for i in range(1, 4):
        while True:
            try:
                nota = float(input(f"Nota {i}: "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("A nota deve estar entre 0 e 10.")
            except ValueError:
                print("Digite um valor numérico válido.")

    return nome, notas