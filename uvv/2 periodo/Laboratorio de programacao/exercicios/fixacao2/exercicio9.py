"""
Peça ao usuário para adivinhar um número entre 1 e 100 que o computador sorteou (use random). O jogo continua até acertar, dando dicas se o palpite é maior ou menor que o número secreto.
"""

import random

numero_secreto = random.randint(1, 100)

print("Tente adivinhar o número entre 1 e 100!")

tentativas = 0
palpite = None

while palpite != numero_secreto:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1

    if palpite < numero_secreto:
        print("O número secreto é MAIOR!")
    elif palpite > numero_secreto:
        print("O número secreto é MENOR!")
    else:
        print(f"Parabéns! Você acertou em {tentativas} tentativas. O número era {numero_secreto}.")