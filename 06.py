# ============================================
# [06] Antecessor e sucessor / Predecessor and Successor
# Tags: int, arithmetic
#
# Descrição (PT):
#   O programa lê um número inteiro e mostra o seu antecessor e sucessor. Trabalha operações simples com inteiros e lógica de valores adjacentes.
#
# Description (EN):
#   The program reads an integer and displays its predecessor and successor. It reinforces integer manipulation and simple arithmetic reasoning.
# ============================================

import os
import subprocess

"""Exercício 6
6) Faça um programa que leia um número inteiro e mostre o seu antecessor e seu sucessor.
Ex:
Digite um número: 9
O antecessor de 9 é 8
"""

# ============================================================
#  LIMPAR ECRÃ (Windows / Linux / macOS)
# ============================================================
def cls():
    """Limpa o terminal de forma compatível com vários sistemas operativos."""
    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run(comando, shell=True)


cls()
print("Digite um número.")
nr = int(input())
print(f"O antecessor de {nr} é {nr-1}.")
print(f"O sucessor de {nr} é {nr+1}.")