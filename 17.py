import os
import subprocess

"""Exercício 18
18) Faça um programa que leia o ano de nascimento de uma pessoa, calcule a idade dela e depois mostre se ela pode ou não votar.
"""

# ============================================================
#  LIMPAR ECRÃ (Windows / Linux / macOS)
# ============================================================
def cls():
    """Limpa o terminal de forma compatível com vários sistemas operativos."""
    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run(comando, shell=True)


cls()
print("Qual o ano de nascimento?")
ano_nascimento = int(input())
idade = 2026 - ano_nascimento
if idade >= 18:
    print(f"\nA pessoa tem {idade} anos e pode votar.\n")
else:
    print(f"\nA pessoa tem {idade} anos e não pode votar.\n")