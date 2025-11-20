temperatura = float(input("Digite uma temperatura em celsius: "))

def c_para_f(c):
    return (c * 1.8) + 32

def c_para_k(c):
    return temperatura + 273

print(f"Temperatura em celsius: {temperatura}")
print(f"Temperatura em Fahrenheit: {c_para_f(temperatura)}")
print(f"Temperatura em Kelvin: {c_para_k(temperatura)}")