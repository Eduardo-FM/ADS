with open("notas.txt", "r", encoding="utf-8") as entrada, \
     open("resultado.txt", "w", encoding="utf-8") as saida:

    for linha in entrada:
        linha = linha.strip()

        if linha == "":
            continue

        partes = linha.split(",")

        nome = partes[0].strip()
        n1 = float(partes[1])
        n2 = float(partes[2])
        n3 = float(partes[3])

        media = (n1 + n2 + n3) / 3

        situacao = "Aprovado" if media >= 7 else "Reprovado"

        saida.write(f"{nome} - Média: {media:.2f} - {situacao}\n")

print("Arquivo resultado.txt gerado com sucesso!")
