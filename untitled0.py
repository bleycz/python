# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 12:54:42 2023

@author: enrico.cezar
"""

import math

def equacao_primeiro_grau(a, b):
    """
    Resolve uma equação de primeiro grau (ax + b = 0).
    Retorna a solução da equação ou uma mensagem de erro se a equação não tiver solução.
    """
    if a == 0:
        if b == 0:
            return "Infinitas soluções"
        else:
            return "Sem solução"
    else:
        x = -b/a
        return x

def equacao_segundo_grau(a, b, c):
    """
    Resolve uma equação de segundo grau (ax^2 + bx + c = 0).
    Retorna uma tupla com as soluções da equação ou uma mensagem de erro se a equação não tiver solução real.
    """
    if a == 0:
        return "Não é uma equação de segundo grau"
    
    delta = b**2 - 4*a*c
    if delta < 0:
        return "Sem solução real"
    else:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        return (x1, x2)

# Exibe o menu de opções
print("Selecione o tipo de equação.")
print("1. Equação de primeiro grau (ax + b = 0)")
print("2. Equação de segundo grau (ax^2 + bx + c = 0)")

# Lê a escolha do usuário
escolha = input("Digite sua escolha (1/2): ")

# Verifica a escolha do usuário e resolve a equação correspondente
if escolha == "1":
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    solucao = equacao_primeiro_grau(a, b)
    print(f"A solução é x = {solucao}")
elif escolha == "2":
    a = float(input("Digite o valor de a: "))
    if a == 0:
        print("Valor inválido para a (a deve ser diferente de zero)")
    else:
        b = float(input("Digite o valor de b: "))
        c = float(input("Digite o valor de c: "))
        solucoes = equacao_segundo_grau(a, b, c)
        if type(solucoes) == str:
            print(solucoes)
        else:
            print(f"As soluções são x1 = {solucoes[
