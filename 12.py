# ============================================
# [12] Preço com desconto / Discounted Price
# Tags: float, arithmetic, percentage
#
# Descrição (PT):
#   O programa lê o preço de um produto e aplica um desconto de 5%, exibindo o valor final. Trabalha porcentagens e cálculos comerciais simples.
#
# Description (EN):
#   The program reads a product price and applies a 5% discount. It reinforces percentage calculations and basic commercial logic.
# ============================================

import os
import subprocess

"""Exercício 12
12) Crie um programa que leia o preço de um produto, calcule e mostre o seu PREÇO PROMOCIONAL, com 5% de desconto.
"""

# ============================================================
#  LIMPAR ECRÃ (Windows / Linux / macOS)
# ============================================================
def cls():
    """Limpa o terminal de forma compatível com vários sistemas operativos."""
    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run(comando, shell=True)


cls()
print("Digite o preço do produto.")
preco = float(input())
preco_promocional = preco * 0.95
print(f"\nO preço promocional é {preco_promocional:.2f}€.\n")