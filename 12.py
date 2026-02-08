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