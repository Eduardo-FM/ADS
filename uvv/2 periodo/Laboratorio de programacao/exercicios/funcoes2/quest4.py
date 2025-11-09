"""
4) Dada uma lista de números informada pelo usuário, crie as funções:

maior_valor(lista)

menor_valor(lista)

media_valores(lista)

quantidade_pares(lista)
 Retorne todos os resultados organizados e formatados na tela.

"""
notas: list[float] = [7.5, 8.0, 6.0, 9.5, 5.5]

def maior_valor(lista: list[float]) -> float:
    """
    :param lista: Lista de floats
    :return: Retorna o maior valor da lista
    """
    return print(max(lista))

def menor_valor(lista: list[float]) -> float:
    """
    :param lista: Lista de floats
    :return: Retorna o maior valor da lista
    """
    return print(min(lista))
def media_valores(lista: list[float]) -> float:
    """
    :param lista: Lista de floats
    :return: Retorna a média dos valores
    """
    return print(sum(lista) / len(lista))

def quantidade_pares(lista: list[float]) -> float:
    """
    :param lista: Lista de floats
    :return: Retorna a quantidade de números pares
    """
    return print([num for num in lista if num % 2 ==0])

quantidade_pares(notas)

