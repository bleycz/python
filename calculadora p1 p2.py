import math

def equacao_primeiro_grau(a, b):
    if a == 0:
        if b == 0:
            return "Infinitas soluções"
        else:
            return "Sem solução"
    else:
        x = -b/a
        return x

def equacao_segundo_grau(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return "Sem solução real"
    elif delta == 0:
        x = -b/(2*a)
        return x
    else:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        return x1, x2

print("Selecione o tipo de equação.")
print("1. Equação de primeiro grau (ax + b = 0)")
print("2. Equação de segundo grau (ax^2 + bx + c = 0)")

escolha = input("Digite sua escolha (1/2): ")

if escolha == '1':
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    print(f"A solução é x = {equacao_primeiro_grau(a, b)}")

elif escolha == '2':
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    print(f"As soluções são x1 = {equacao_segundo_grau(a, b, c)[0]} e x2 = {equacao_segundo_grau(a, b, c)[1]}")

else:
    print("Escolha inválida")
