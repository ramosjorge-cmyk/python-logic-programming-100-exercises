# ============================================
# [18] Pode votar? / Voting Eligibility
# Tags: int, conditions
#
# Descrição (PT):
#   O programa calcula a idade do utilizador e determina se ele pode votar. Trabalha condições simples.
#
# Description (EN):
#   The program computes the user’s age and determines whether they are eligible to vote.
# ============================================

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
while True:
    ano_nascimento = input("Qual ano de nascimento?\n")
    if ano_nascimento.replace(" ", "").isdigit():
        break
    else:
        print("Erro: só são permitidos números.")

idade = 2026 - int(ano_nascimento)

print(f"\nA pessoa tem {idade} anos.")
if idade >= 18:
    print("A pessoa pode votar.\n")
else:
    print("A pessoa não pode votar.\n")