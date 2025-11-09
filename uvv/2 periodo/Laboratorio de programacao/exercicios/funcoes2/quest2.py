"""
2) Uma escola armazena as notas dos alunos em uma lista.
 Exemplo: notas = [7.5, 8.0, 6.0, 9.5, 5.5].

Implemente as funções:

media(notas) ? calcula e retorna a média.

maior_nota(notas) ? retorna a maior nota.

menor_nota(notas) ? retorna a menor nota.
 Mostre o resultado formatado na tela.

"""

notas: list[float] = [7.5, 8.0, 6.0, 9.5, 5.5]

def media(notas: list[float]) -> float:
    """
    :param notas: Lista de floats
    :return: Cálculo da média das notas na lista
    """
    return sum(notas) / len(notas)


def maior_notas(notas: list[float]) -> float:
    """
    :param notas: Lista de floats
    :return:  retorna a maior nota
    """
    return max(notas)

def menor_nota(notas)-> float:
    """
    :param notas: Lista de floats
    :return:  retorna a menor nota
    """
    return min(notas)

print(media(notas))
print(maior_notas(notas))
print(menor_nota(notas))
