"""
6 - Dada uma lista com várias palavras: palavras = ["inteligência", "artificial", "dados", "machine", "learning", "rede", "neural"]. Desenvolva um programa que: Crie uma nova lista com as palavras que têm mais de 7 letras; Ordene a lista em ordem decrescente de tamanho; Exiba quantas palavras contêm a letra “a”.
"""

palavras = ["inteligência", "artificial", "dados", "machine", "learning", "rede", "neural"]

palavras_grandes = [p for p in palavras if len(p) > 7]
print("Palavras com mais de 7 letras:", palavras_grandes)

ordenadas = sorted(palavras_grandes, key=len, reverse=True)
print("Ordenadas por tamanho (decrescente):", ordenadas)

quant_a = sum(1 for p in palavras if "a" in p.lower())
print(f"Quantidade de palavras que contêm a letra 'a': {quant_a}")
