a = 1

def somar(a, b):
    print("a da funcao, ", a)
    print("a de fora", globals()['a'])
    return a + b

somar(2, 3)