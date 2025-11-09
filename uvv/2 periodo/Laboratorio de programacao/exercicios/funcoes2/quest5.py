"""
5) Implemente um programa que gere senhas aleatórias de acordo com o tamanho informado pelo usuário.

Funções:

gerar_senha(tamanho) ? retorna uma senha aleatória contendo letras e números.

mostrar_senha(senha) ? exibe a senha formatada e a contagem de caracteres.

Use o módulo random.
"""

import random

letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"

def gerar_senha(tamanho: int) -> str:
    """
    :param tamanho: tamanho da senha a ser gerada
    :return: retorna uma senha aleatória contendo letras e números
    """
    senha = []
    for index in range(tamanho):
        senha.append(random.choice(letras + numeros))
    return "".join(senha)

def mostrar_senha(senha: str) -> None:
    """
    :param senha: senha para a contagem
    :return: exibe a senha formatada e a contagem de caracteres.
    """
    print(f"Senha: {senha}")
    print(f"Quantidade de caracteres: {len(senha)}")

senha:str = gerar_senha(10)
mostrar_senha(senha)