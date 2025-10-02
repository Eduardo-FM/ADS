"""
11) Ler do teclado a idade e o sexo de 10 pessoas, calcule e imprima:

idade média das mulheres
idade média dos homens
idade média do grupo
"""

pessoas = []

# Ler dados das 10 pessoas
for i in range(10):
    idade = int(input(f"Digite a idade da {i+1}ª pessoa: "))
    sexo = input("Digite o sexo (M/F): ").strip().upper()
    pessoas.append((idade, sexo))  # cada pessoa é uma tupla

# Variáveis de soma e contagem
soma_homens = soma_mulheres = soma_total = 0
qtd_homens = qtd_mulheres = qtd_total = 0

# Processar os dados
for idade, sexo in pessoas:
    soma_total += idade
    qtd_total += 1

    if sexo == "M":
        soma_homens += idade
        qtd_homens += 1
    elif sexo == "F":
        soma_mulheres += idade
        qtd_mulheres += 1

# Cálculo das médias
media_homens = soma_homens / qtd_homens if qtd_homens > 0 else 0
media_mulheres = soma_mulheres / qtd_mulheres if qtd_mulheres > 0 else 0
media_total = soma_total / qtd_total if qtd_total > 0 else 0

# Saída
print(f"Idade média das mulheres: {media_mulheres:.2f}")
print(f"Idade média dos homens: {media_homens:.2f}")
print(f"Idade média do grupo: {media_total:.2f}")
