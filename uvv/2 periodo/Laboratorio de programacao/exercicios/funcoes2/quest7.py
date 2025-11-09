"""
7)  Crie funções para converter entre Celsius, Fahrenheit e Kelvin.

Funções:

c_para_f(c) ? retorna Fahrenheit

f_para_c(f) ? retorna Celsius

c_para_k(c) ? retorna Kelvin
Peça ao usuário uma temperatura e a unidade, e exiba as conversões.
"""

temperatura = float(input("Digite uma temperatura: "))
unidade = input("""
                    Digite a unidade de medida entre (celsius, fahrenheit, kelvin: 
                """)

def c_para_f(c):
    return (c * 1.8) + 32
def f_para_c(f):
    return (f - 32) * 5/9
def c_para_k(c):
    return temperatura + 273

match unidade.lower():
    case "celsius":
        f_para_c(temperatura)
    case "fahrenheit":
        c_para_f(temperatura)
    case "kelvin":
        c_para_k(temperatura)

