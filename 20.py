# ============================================
# [20] Par ou ímpar / Even or Odd
# Tags: int, modulo, conditions
#
# Descrição (PT):
#   O programa lê um número inteiro e determina se é par ou ímpar usando o operador módulo.
#
# Description (EN):
#   The program reads an integer and determines whether it is even or odd using the modulo operator.
# ============================================

import os
import subprocess

"""Exercício 20
20) Desenvolva um programa que leia um número inteiro e mostre se ele é PAR ou ÍMPAR.
"""

# ============================================================
#  LIMPAR ECRÃ (Windows / Linux / macOS)
# ============================================================
def cls():
    """Limpa o terminal de forma compatível com vários sistemas operativos."""
    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run(comando, shell=True)


cls()
print("Digite um número inteiro:")
numero = int(input())
if numero % 2 == 0:
    print(f"\nO número {numero} é PAR.\n")
else:
    print(f"\nO número {numero} é ÍMPAR.\n")