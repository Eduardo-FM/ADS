from typing import List

def procura_todos(tokens: List[str], required: List[str]) -> bool:
  # Tokens é a frase tokenizada, ou seja, uma lista de palavras
  # required é a lista das palavras procuradas

  ## todas as palavras tem que ser encontradas

    ## SET transforma a lista de tokens em um conjunto (set)
      # tokens = ["eu", "estou", "muito", "triste", "hoje"]
      # vira
      # tset = {"eu", "estou", "muito", "triste", "hoje"}
    tset = set(tokens)

    return all(w in tset for w in required)

    ## equivale a
    #for w in required:
    #if w not in tset:
    #    return False

    #return True

def procura_sequencia(tokens: List[str], seq: List[str]) -> bool:
    """Caso 3: a sequência aparece exatamente, consecutiva (ordem + adjacência)."""

    #n = quantidade de tokens na frase
    #m = quantidade de tokens procurados (sequência)

    n, m = len(tokens), len(seq)
    if m == 0:
        return True
    if m > n:
        return False

   ## testa a sequencia comecando pelo tokeu zero até a posicao

   ## Em quantas posições diferentes uma sequência de tamanho m
   ## pode começar dentro de uma lista de tamanho n?

   #tokens = ["hoje", "eu", "estou", "muito", "triste"]
   #seq    = ["eu", "estou", "muito"]

    for i in range(len(tokens) - len(seq) + 1):

        # pega um pedçao da lista, por exemplo [0:3] = ["hoje", "eu", "estou"] e vai comparar
        # com a sequencia procurada ["eu", "estou", "muito"]

        # depois faz [1:4] = ["eu", "estou", "muito"] e compara novamente com
        # a sequencia procurada
        if tokens[i:i+m] == seq:
            return True
    return False



###***********************
## REGEX ###
###***********************

"""
Regex (Python)
Símbolos cobertos: .  .*  .+  \b  ^  $  ( )  group(0)/group(1)
"""

import re

def demo(pattern: str, text: str, flags: int = 0) -> None:
    m = re.search(pattern, text, flags)
    print("=" * 90)
    print(f"PADRÃO : {pattern}")
    print(f"TEXTO  : {text}")
    if not m:
        print("RESULT : ? NÃO CASOU (m = None)")
        return
    print("RESULT : ? CASOU")
    print(f"  group(0) (match inteiro) : {m.group(0)!r}")
    # imprime grupos capturados, se existirem
    if m.re.groups:
        for i in range(1, m.re.groups + 1):
            print(f"  group({i}) (captura {i})      : {m.group(i)!r}")
    else:
        print("  (sem grupos capturados)")
    print(f"  span (posição no texto)   : {m.span()}")

# ----------------------------------------------------------------------
# 1) . (ponto) — qualquer caractere (1 caractere)
demo(r"c.t", "Hoje eu vi um gato: cat; e também vi cot, mas não vi ctt.")
demo(r"c.t", "Eu só escrevi 'ct' aqui.")  # não casa

# ----------------------------------------------------------------------
# 2) .* — qualquer caractere, qualquer tamanho (inclusive vazio) (guloso)
demo(r"eu.*triste", "eu estou triste, mas amanhã estarei feliz e decidido.")
demo(r"eu.*triste", "eu estou tristemente chateado com a situação.")  # 'triste' dentro de 'tristemente' (substring)
demo(r"eu.*triste", "eu estou feliz, apesar do cansaço.")  # não casa (faltou 'triste')

# Mostrando efeito guloso com múltiplos "triste"
demo(r"eu.*triste", "eu estou triste, muito triste, enormemente triste; e ainda assim sigo.")

# ----------------------------------------------------------------------
# 3) .+ — um ou mais caracteres (não aceita vazio)
demo(r"^eu quero (.+)$", "eu quero um novo emprego que ganhe mais")
demo(r"^eu quero (.+)$", "eu quero")  # não casa (.+ exige algo)

# Comparando com (.*) só para você ver a diferença (mesmo que não seja o foco)
demo(r"^eu quero (.*)$", "eu quero")  # casa, mas captura vazio

# ----------------------------------------------------------------------
# 4) \b — limite de palavra (palavra inteira vs substring)
demo(r"\beu\b", "eu realmente acredito que isso vai dar certo.")
demo(r"\beu\b", "meu plano é simples e direto.")  # não casa (eu dentro de 'meu')
demo(r"triste", "eu estou tristemente chateado com o atraso.")  # casa (substring)
demo(r"\btriste\b", "eu estou tristemente chateado com o atraso.")  # não casa (quer palavra inteira)
demo(r"\btriste\b", "eu estou triste com a demora e com a incerteza.")  # casa

# ----------------------------------------------------------------------
# 5) ^ e $ — início e fim da string (frase inteira)
demo(r"^oi$", "oi")
demo(r"^oi$", "oi, tudo bem?")  # não casa (tem mais coisas)
demo(r"\boi\b", "oi, tudo bem?")  # casa (oi como palavra dentro da frase)

# ----------------------------------------------------------------------
# 6) ( ) — grupos de captura e group(0) vs group(1), group(2)...
demo(r"^eu quero (.+)$", "eu quero ser aprovado na prova final de algoritmos")
demo(r"quero (.+)$", "hoje, com muita convicção, eu quero ser aprovado")  # sem ^: não pega o 'hoje,... eu'

# Dois grupos
demo(r"^eu (.+) porque (.+)$", "eu estudo com disciplina porque quero mudar de vida")

# ----------------------------------------------------------------------
# 7) Espaço literal no padrão (diferença entre "eu.*triste" e "eu .* triste")
demo(r"eu.*triste", "eutriste")       # casa (.* pode ser vazio)
demo(r"eu .* triste", "eutriste")     # não casa (exige espaços literais)
demo(r"eu .* triste", "eu estou triste")  # casa (tem espaços)

# ----------------------------------------------------------------------
print("\nFIM — Ajuste os textos/padrões à vontade e observe group(0)/groups.\n")




# Exemplos
tokens = ["hoje", "eu", "estou", "muito", "triste"]

print(procura_todos(tokens, ["eu", "muito"]))          # True  (caso 2)
print(procura_sequencia(tokens, ["eu", "muuito"]))    # False (caso 3)