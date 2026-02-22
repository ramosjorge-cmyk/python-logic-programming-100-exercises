# ============================================
# [13] Novo salário com aumento / Salary Increase
# Tags: float, percentage
#
# Descrição (PT):
#   O exercício lê o salário atual e calcula o novo salário com aumento de 15%. Trabalha porcentagens e atualização de valores financeiros.
#
# Description (EN):
#   The exercise reads the current salary and applies a 15% raise. It practices percentage manipulation and financial computation.
# ============================================

import os
import subprocess

"""Exercício 13
13) Faça um algoritmo que leia o salário de um funcionário, calcule e mostre o seu novo salário, com 15% de aumento.
"""

# ============================================================
#  LIMPAR ECRÃ (Windows / Linux / macOS)
# ============================================================
def cls():
    """Limpa o terminal de forma compatível com vários sistemas operativos."""
    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run(comando, shell=True)


cls()
print("Qual o seu salário?")
salario = float(input())
novo_salario = salario * 1.15
print(f"\nO funcionário tem um salário de {int(salario)} euros.")
print(f"O funcionário tem um salário de {salario:.2f} euros.")
print(f"O funcionário tem um salário de {salario:.0f} euros.")
print(f"Com o aumento de 15%, o novo salário é {novo_salario:.2f} euros.\n")