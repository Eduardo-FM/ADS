
arquivo_origem = input("Digite o nome do arquivo de origem: ").strip()

if "." in arquivo_origem:
    nome, ext = arquivo_origem.rsplit(".", 1)
    arquivo_backup = f"{nome}_backup.{ext}"
else:
    arquivo_backup = arquivo_origem + "_backup"

try:
    with open(arquivo_origem, "r", encoding="utf-8") as origem, \
         open(arquivo_backup, "w", encoding="utf-8") as destino:

        for linha in origem:
            destino.write(linha)

    print(f"Backup criado com sucesso: {arquivo_backup}")

except FileNotFoundError:
    print("Arquivo de origem não encontrado.")
