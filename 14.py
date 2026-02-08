import os
import subprocess

"""Exercício 14
14) A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar, sabendo que o carro custa R$90 por dia e R$0,20 por Km rodado.
"""

# ============================================================
#  LIMPAR ECRÃ (Windows / Linux / macOS)
# ============================================================
def cls():
    """Limpa o terminal de forma compatível com vários sistemas operativos."""
    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run(comando, shell=True)


cls()
print("Quantos Km foram percorridos?")
km = float(input())
print("Quantos dias o carro foi alugado?")
dias = int(input())
preco_total = (dias * 90) + (km * 0.20)
print(f"\nO preço total a pagar é {preco_total:.2f} euros.\n")