import os
import subprocess

"""Exercício 1
1) Escreva um programa que mostre na tela a mensagem "Olá, Mundo!"
"""

# ============================================================
#  LIMPAR ECRÃ (Windows / Linux / macOS)
# ============================================================
def cls():
    """Limpa o terminal de forma compatível com vários sistemas operativos."""
    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run(comando, shell=True)


cls()
print("Olá, Mundo!")
print("\n")