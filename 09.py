# ============================================
# [09] Conversão de reais para dólares / Currency Conversion (BRL → USD)
# Tags: float, arithmetic
#
# Descrição (PT):
#   O exercício lê quanto dinheiro a pessoa tem em reais e calcula quantos dólares pode comprar, usando a taxa fixa indicada.
#
# Description (EN):
#   The exercise reads an amount in BRL and converts it to USD using the fixed exchange rate provided. It practices arithmetic and financial reasoning.
# ============================================

import os
import subprocess

"""Exercício 9
9) Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$)
e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,45.
"""

# ============================================================
#  LIMPAR ECRÃ (Windows / Linux / macOS)
# ============================================================
def cls():
    """Limpa o terminal de forma compatível com vários sistemas operativos."""
    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run(comando, shell=True)


cls()
print("Digite quanto dinheiro você tem na carteira (em €).")
d = float(input())
print(f"Pode comprar US$ {d/3.45:.2f}\n")    

print("\n")