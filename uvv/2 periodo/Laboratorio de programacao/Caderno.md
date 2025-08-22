## Python

Principais caracteristicas é a legibilidade dos programas escritos.

Em outras linguagem é muito comum o uso excessivo de marcacoes(ponto ou ponto e vírcula), de marcadores(chaves, colchetes ou parenteses) e de palavra especiais(begin/end), o que torna mais dificil a leitura e compreesao dos programas.

Ja em python, o uso desses recursos é reduzido, deixando a linguagem mais simples

Em python destaca-se a simplicidade da linguagem, que facilita o aprendizado da programacao.

Tambem possui uma portabilidade muito grande para diversas plataformas diferentes, alem de ser possivel utilizar trechos de codigos em outras linguagens. 

Python é uma linguagem de programacao interpretada, POO, de alto nível e com semantica dinamica.

Reduz a manutencao de um programa, suporta modulos e pacotes, que encoraja a programacao modularizada e reuso de codigos. 

#### Variaveis

Pequenos espacos de memória, utilizados para armazenar e manipular dados. 

Os tipos de dados basicos sao: 
- inteiro(armazena numero inteiros)
- float (numeros em formato decimal)
- string (um conjunto de caracteres)

Cada variavel pode armazenar apenas um tipo de dado a cada instante 

Os nomes das variaveis desem ser iniciadas com uma letra, moas podem possuir outros tipos de caracteres, como numeros ou .==...==

```python
inteiro5: int = 5

flutuante: float = 3.5

string: str = "string"

tipo_boeleano: bool = True
```


#### tipos de dados basicos

- int, long
- float
- complex
- bool
- string

#### Input()

sempre vai retornar uma string.

Para retornar dados do tipo inteiro ou float, é preciso converter o tipo inteiro ou float

==...==

# aula 11/08

## numeros de ponto flutuante 

==...==

## numeros complexos

Representandos como dois numeros de ponto flutuante. ==...==

## ## Strings 

Metodos

String possuem os metodos
- lower
- upper
- capitalize split,
- strip
- ==...==

``` python

# Como evitar a quebra de linha? 

print(""C:\\direito\\arquivo")
``` 

- STRINGS sao imutaveis

Ou troco o valor da STRING todo, ou nao troco. Nao consigo atribuir apenas uma variável

``` python
s = "Hellor"

s[0] = 'j'

Traceback (most recent call last):
  File "/home/eduardo/Documents/18/08/18-08.py", line 2, in <module>
    s[0] = 'j'
    ~^^^
TypeError: 'str' object does not support item assignment
``` 


O operador '+' nao converte automaticamente numeros ou outros tipos em strings. A funcao str() converte valores para sua representacao em string.

``` python

pi = 3.14

text = "o valor de pi é= " + pi


File "/home/eduardo/Documents/18/08/18-08.py", line 2, in <module>
    text = "o valor de pi é= " + pi
           ~~~~~~~~~~~~~~~~~~~~^~~~
TypeError: can only concatenate str (not "float") to str


pi = 3.14

text = "o valor de pi é= " + str(pi)

# o valor de pi é = 3.14

```


#### Acesso a conteúdo das String

Acesso sequencial, em fatias ou direto (indice)

Slice: s[start:end]

``` python
s = "Hello"

  

print(s[0])

print(s[1:])

print(s[1:4])

print(s[:])

print(s[1:100])

### 
H
ello
ell
Hello
ello

```


#### String metodos


#### capitalize

```python

s = "hello"

print(s.capitalize())

###
Hello
```


##### Split

```python 
s = "PYTHON IS POWERFUL"

print(s.split())

### 
['PYTHON', 'IS', 'POWERFUL']
```

##### Count

```python
s = "PYTHON IS POWERFUL"

print(s.count("TH"))

###
1
```


##### Join

```Python
s = "PYTHON IS POWERFUL"

print(s.split())
  
print("/".join(s.split()))

### 
['PYTHON', 'IS', 'POWERFUL']
PYTHON/IS/POWERFUL
```

#### Find

``` Python
text = "Hello, welcome to my world"

print(text.find("welcome"))

# 7
```

#### Startswith

```Python
text = "Hello, welcome to my world"

  

print(text.startswith("Hello"))

# True
```


#### Replace

```Python 3
txt = "I like bananas"
x = txt.replaced("bananas", "apples")

print(x)

# "I like apples"
```


#### Strip

```Python
txt = " banana "

x = txt.strip() 

print("of all fruits", x, "is my favorite") 

###
of all fruits banana is my favorite

```


### Listas e Tuplas

- Estruturas de mapas nativas: list, tuple
- ==...==

#### Tuplas

Uma tuplas é uma colecao de objetos separados por virgula

Para uma tupla com 1 elemento apenas é preciso

pode ter ou nao parenteses para delimitar a tupla

Tupla aninhada

Heterogenea 


### Listas

``` Python
a = [0, 1, 2, 3, 4]

print(a)

a.append(5)

print(a)

a.insert(2,42)

print(a)

a.reverse()

print(a)

a.sort()

print(a)

l = (6, 7, 8, 9)

a.extend(l)

print(a)

a.remove(42)

print(a)

print(a.index(9))

print(a.count(3))

### 
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4, 5]
[0, 1, 42, 2, 3, 4, 5]
[5, 4, 3, 2, 42, 1, 0]
[0, 1, 2, 3, 4, 5, 42]
[0, 1, 2, 3, 4, 5, 42, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
9
1
```

As listas contem ponteiros para objetos que residem em algum lugar na memoria 

```Python
original = ['H', 'He', 'Li']

temp = ['Be']

final = original + temp

print(final)

### 
['H', 'He', 'Li', 'Be']
```

