from entrada import coletar_dados
from calculo import calcular_media, situacao

def main():
    nome, notas = coletar_dados()
    media = calcular_media(notas)
    status = situacao(media)

    print("\n--- Resultado Final ---")
    print(f"Aluno: {nome}")
    print(f"Notas: {notas}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {status}")

main()