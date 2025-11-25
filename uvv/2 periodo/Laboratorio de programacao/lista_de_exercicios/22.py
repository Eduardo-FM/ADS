# Nome dos arquivos
arquivo_origem = "entrada.txt"
arquivo_destino = "saida.txt"

with open(arquivo_origem, "r", encoding="utf-8") as entrada, \
     open(arquivo_destino, "w", encoding="utf-8") as saida:

    for linha in entrada:
        saida.write(linha.upper())

print("Arquivo gerado com sucesso!")
