# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 11:51:25 2023

@author: enrico.cezar
"""

import sympy

def calculadora_limite(expressao, x, valor):
    resultado = sympy.limit(expressao, x, valor)
    return resultado

def calculadora_derivada(expressao):
    derivada = sympy.diff(expressao)
    return derivada

print("Selecione o tipo de operação.")
print("1. Cálculo de limite")
print("2. Cálculo de derivada")

escolha = input("Digite sua escolha (1/2): ")

if escolha == '1':
    expressao = sympy.sympify(input("Digite a expressão: "))
    x = sympy.Symbol('x')
    valor = float(input("Digite o valor de x para o qual o limite será calculado: "))
    print(f"O limite da expressão {expressao} quando x se aproxima de {valor} é: {calculadora_limite(expressao, x, valor)}")

elif escolha == '2':
    expressao = sympy.sympify(input("Digite a expressão: "))
    print(f"A derivada da expressão {expressao} é: {calculadora_derivada(expressao)}")

else:
    print("Escolha inválida")
