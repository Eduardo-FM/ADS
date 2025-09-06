"""
1) Verificação de idade para votar
Peça ao usuário para digitar sua idade e exiba:
"Voto obrigatório" se a idade for entre 18 e 70 anos;
"Voto facultativo" se for entre 16 e 17 anos ou acima de 70;
"Não pode votar" se for menor de 16 anos.
"""
print("1)")

# idade: int = int(input("Digite a sua idade: "))
#
# if idade >= 18 and idade <= 70:
#     print("Voto obrigatório")
# elif idade >= 16 and idade <= 17 or idade > 70:
#     print("Voto facultativo")
# elif idade <16:
#     print("Não pode votar")
"""
2) Maior de três números
Peça três números inteiros ao usuário e use condicionais para exibir qual é o maior número.
"""
print("2)")
# num1: int = int(input("Digite o primeiro número inteiro: "))
# num2: int = int(input("Digite o segundo número inteiro: "))
# num3: int = int(input("Digite o terceiro número inteiro: "))
#
# if num1 > num2 and num1 > num3:
#     print("O primeiro número é o maior")
# elif num2 > num1 and num2 > num3:
#     print("O segundo número é o maior")
# elif num3 > num1 and num3 > num2:
#     print("O terceiro número é o maior")
"""
3) Cálculo de média escolar
Solicite ao usuário 3 notas.
Se a média for maior ou igual a 7, mostre "Aprovado";
Se for entre 5 e 6.9, mostre "Recuperação";
Se for menor que 5, mostre "Reprovado".
"""
print("3)")
# nota1: int = int(input("Digite o primeiro nota: "))
# nota2: int = int(input("Digite o segundo nota: "))
# nota3: int = int(input("Digite o terceiro nota: "))
#
# media: float = (nota1 + nota2 + nota3) / 3
# print(f"Média: {media}")
# if media >= 7:
#     print("Aprovado")
# elif 5 <= media <= 6.9:
#     print("Recuperação")
# elif media < 5:
#     print("Reprovado")
"""
4) Classificação de número
Peça um número inteiro e diga se ele é:
Positivo
Negativo
Zero
"""
#
# print("4)")
# num = int(input("Digite um número inteiro: "))
#
# if num == 0:
#     print("Zero")
# elif num > 0:
#     print("Positivo")
# elif num < 0:
#     print("Negativo")
"""
5) Calculadora simples
Solicite ao usuário dois números e uma operação (+, -, *, /).
 Use condicionais para realizar a operação escolhida e mostrar o resultado.
 Se a operação não for válida, mostre uma mensagem de erro.
"""
# print("5")
# num1: int = int(input("Digite o primeiro número: "))
# num2: int = int(input("Digite o segundo número: "))
# operacao: str = input("Digite a operacao: ")
#
# if operacao.strip() == "+":
#    print(num2 + num1)
# elif operacao.strip() == "-":
#     print(num1 - num2)
# elif operacao.strip() == "*":
#     print(num2 * num1)
# elif operacao.strip() == "/":
#     print(num1 / num2)
# else:
#     print("Operação não é válida")


"""
6) Calcule a tabuada do 13.
"""
print("6")

# index: int = 1
# while index <= 10:
#     print(f"13 * {index} = ", 13 * index )
#     index += 1
"""
7) Ler do teclado uma lista com 5 inteiros e imprimir o menor valor.
"""
print("7")

#
# entrada = input("Digite 5 inteiros separados por espaço: ")
# lista = list(map(int, entrada.split()))
#
# print("Menor número: ", min(lista))
"""
8) Ler do teclado uma lista com 5 inteiros e imprimir True se a lista estiver ordenada de forma crescente ou False caso contrário.
"""
# print("8")
#
# entrada = input("Digite uma lista com 5 inteiros separados por espaço: ")
# lista = list(map(int, entrada.split()))
#
# if sorted(lista):
#     print(True)
# else:
#     print(False)
"""
9) Exiba em ordem decrescente todos os números de 500 até 10.
"""

print("9")
# for num in list(range(500 , 9, -1)):
#     print(f"Número: {num}")
"""
10) Ler do teclado 10 números e imprima a quantidade de números entre 10 e 50.
"""
# print("10")
#
# entrada = input("Digite 10 números separados por espaço: ")
# numeros = list(map(int, entrada.split()))
#
# qtd = sum(1 for n in numeros if 10 <= n <= 50)
# print("Quantidade de números entre 10 e 50:", qtd)

"""
11) Ler do teclado a idade e o sexo de 10 pessoas, calcule e imprima:

idade média das mulheres
idade média dos homens
idade média do grupo
"""
print("11")
idades_homens = []
idades_mulheres = []
idades_todas = []

for i in range(1, 11):
    print(f"\nPessoa {i}:")
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo (M/F): ").strip().upper()

    idades_todas.append(idade)

    if sexo == "M":
        idades_homens.append(idade)
    elif sexo == "F":
        idades_mulheres.append(idade)
    else:
        print("Sexo inválido, ignorando...")

# calcula médias (evita divisão por zero)
media_mulheres = sum(idades_mulheres) / len(idades_mulheres) if idades_mulheres else 0
media_homens = sum(idades_homens) / len(idades_homens) if idades_homens else 0
media_grupo = sum(idades_todas) / len(idades_todas) if idades_todas else 0

print("\n--- Resultados ---")
print(f"Idade média das mulheres: {media_mulheres:.2f}")
print(f"Idade média dos homens: {media_homens:.2f}")
print(f"Idade média do grupo: {media_grupo:.2f}")

"""
12) Calcule o somatório dos números de 1 a 100 e imprima o resultado.
"""
print("12")
total = 0
for num in range(1, 101):
    total += num

print(f"Total da soma: {total}")