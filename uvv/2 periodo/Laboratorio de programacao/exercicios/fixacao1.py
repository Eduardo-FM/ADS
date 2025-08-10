"""
1. Cálculo de Desconto: Uma loja está oferecendo desconto de 10% para
pagamentos à vista.
Atividade:
● Solicite ao usuário o valor da compra.
● Calcule o valor final com desconto e exiba o resultado.
"""

valor: float = float(input("Digite o valor da compra: "))
desconto: float = valor * 0.1
print(f"Valor final com desconto: {valor - desconto}")


"""
2. Conversor de Temperatura: Um meteorologista precisa converter temperaturas de
Celsius para Fahrenheit.
Atividade:
● Peça ao usuário a temperatura em graus Celsius.
● Converta para Fahrenheit usando a fórmula: F = (C * 9/5) + 32.
● Mostre o resultado formatado.
"""

temperatura: float = float(input("Digite a temperatura em graus Celsius: "))
fahrenheit: float = (temperatura * 9/5) + 32
print(f"Temperatura em fahrenheit: {fahrenheit:.2f}")

"""
3. Troca de Valores: Em um algoritmo de controle, dois valores foram digitados
incorretamente e precisam ser trocados.
Atividade:
● Leia dois números inteiros do usuário.
● Troque os valores entre as variáveis sem usar uma variável auxiliar.
● Exiba os valores após a troca.
"""

inteiro1: int = int(print("Digite o primeiro número inteiro: "))
inteiro2: int = int(print("Digite o segundo número inteiro: "))

inteiro1, inteiro2 = inteiro2, inteiro1
print(f"Primeiro número: {inteiro1}. Segundo número: {inteiro2}")
"""
4. Calculadora de IMC: Uma clínica médica quer calcular o IMC dos pacientes.
Atividade:
● Solicite peso (kg) e altura (m).
● Calcule o IMC: IMC = peso / (altura ** 2).
● Mostre o resultado com duas casas decimais.
"""

peso: float = float(input("Informe seu peso: "))
altura: float = float(input("Informe sua altura: "))
imc: float = peso / (altura ** 2)
print(f"O seu imc é: {imc:.2f}")

"""
5. Operações com Strings: Um formulário pede nome completo do usuário.
Atividade:
● Solicite o nome completo do usuário.
● Mostre:
1. O nome em letras maiúsculas.
2. O nome em letras minúsculas.
3. Quantos caracteres possui sem contar espaços.
"""

nome: str = input("Digite seu nome completo: ")
print(f"Seu nome em letras maiúsculas: {nome.upper()}")
print(f"Seu nome em letras minusculas: {nome.lower()}")
print(f"Quantidade de caracteres: {len(nome.replace(' ', ''))}")

"""
6. Calculadora Simples Um sistema simples precisa realizar operações matemáticas
básicas.
Atividade:
● Peça dois números ao usuário.
● Mostre soma, subtração, multiplicação e divisão.
● Exiba os resultados formatados.
"""
num1:float = print("Digite o primeiro número: ")
num2:float = print("Digite o segundo número: ")
print(f"Soma: {num1 + num2}")
print(f"Subtração: {num1 - num2}")
print(f"Multiplicação:  {num1 * num2}")
print(f"Divisão: {num1 / num2}")
"""
7. Analisando Entrada: Um sistema precisa validar o que o usuário digita.
Atividade:
● Peça ao usuário que digite algo.
● Mostre na tela:
○ Se é numérico
○ Se é alfabético
○ Se está em maiúsculo ou minúsculo
Dica: Explorar métodos de string: .isnumeric(), .isalpha(), .islower(), .isupper().
"""
entrada: str = input("Digite algo: ")

print(f"É numérico? {entrada.isnumeric()}")
print(f"É alfabético? {entrada.isalpha()}")
print(f"Está em maiúsculo? {entrada.isupper()}")
print(f"Está em minúsculo? {entrada.islower()}")

"""
8. Conversão Monetária: Um usuário precisa converter valores de dólar para real.
Atividade:
● Peça o valor em dólar e a cotação atual.
● Calcule e mostre o valor em reais.
"""
dolar: float = float(input("Digite o valor em dólar: "))
cotacao: float = float(input("Digite a cotação atual do dólar: "))

reais: float = dolar * cotacao

print(f"O valor em reais é: R$ {reais:.2f}")

"""
9. Questão Conceitual - Responda as seguintes perguntas abaixo:
A. Explique a diferença entre variável e constante.
B. Por que em Python não existe uma palavra reservada para declarar
constantes?
C. Como os programadores indicam que um valor não deve ser alterado?
D. Explique por que em Python não é necessário declarar o tipo de uma variável
antes de utilizá-la.
E. Dê um exemplo de como o tipo pode mudar dependendo do valor atribuído.
"""

"""
A) 
Variável é um espaço de memória que pode armazenar um valor que pode mudar durante a execução do programa. Ja constante é um valor que não deve mudar após ser definido.
B)
Porque o Python não implementa constantes de forma nativa. A linguagem é dinamicamente tipada e flexível, então não há um mecanismo que obrigue um valor a permanecer imutável.
C) 
Usam convenção de nomenclatura, escrevem o nome da constante todo em maiúsculas e, se necessário, com _ separando palavras.
D)
Porque Python é uma linguagem de tipagem dinâmica, o tipo é atribuído automaticamente de acordo com o valor informado.
x = 10       # int
x = "Python" # String
"""


