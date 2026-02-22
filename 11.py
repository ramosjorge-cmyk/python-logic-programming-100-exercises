# ============================================
# [11] Cálculo do Delta / Delta Calculation
# Tags: math, float, arithmetic
#
# Descrição (PT):
#   O exercício lê os coeficientes de uma equação do 2.º grau e calcula o valor de delta. Trabalha fórmulas matemáticas e manipulação de floats.
#
# Description (EN):
#   The exercise reads the coefficients of a quadratic equation and computes the discriminant (delta). It practices formula application and numeric handling.
# ============================================

import os
import subprocess

"""Exercício 11
11) Desenvolva uma lógica que leia os valores de A, B e C de uma equação do segundo grau e mostre o valor de Delta.
"""

# ============================================================
#  LIMPAR ECRÃ (Windows / Linux / macOS)
# ============================================================
def cls():
    """Limpa o terminal de forma compatível com vários sistemas operativos."""
    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run(comando, shell=True)


cls()
print("Digite o valor de A.")
a = float(input())
print("Digite o valor de B.")
b = float(input())
print("Digite o valor de C.")
c = float(input())
delta = b**2 - 4*a*c
print(f"\nO valor de Delta é {delta}.\n")

# Análise das raízes
if delta < 0:
    print("A equação não tem raízes reais.\n")
elif delta == 0:
    print("A equação tem uma raiz real.\n")
else:
    print("A equação tem duas raízes reais.\n")