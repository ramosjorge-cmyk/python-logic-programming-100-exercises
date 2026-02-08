import os
import subprocess

"""Exercício 16
16) [DESAFIO] Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dias e quantos anos ele já fumou. Considere que um fumante perde 10 min de vida a cada cigarro. Calcule quantos dias de vida um fumante perderá e exiba o total em dias.
"""

# ============================================================
#  LIMPAR ECRÃ (Windows / Linux / macOS)
# ============================================================
def cls():
    """Limpa o terminal de forma compatível com vários sistemas operativos."""
    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run(comando, shell=True)


cls()
print("Quantos cigarros fuma por dia?")
cigarros = int(input())
print("Quantos anos já fumou?")
anos = int(input())
minutos_perdidos = cigarros * 10 * 365 * anos
dias_perdidos = minutos_perdidos / (24 * 60)
print(f"\nO fumante perdeu {dias_perdidos:.0f} dias de vida.\n")