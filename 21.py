# ============================================
# [21] Ano bissexto / Leap Year Check
# Tags: int, conditions
#
# Descrição (PT):
#   O exercício verifica se um ano é bissexto com base nas regras matemáticas apropriadas.
#
# Description (EN):
#   The exercise checks whether a given year is a leap year using standard mathematical rules.
# ============================================

import os
import subprocess

"""Exercício 21
21) Faça um algoritmo que leia um determinado ano e mostre se ele é ou não BISSEXTO.
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
    ano = input("Digite um ano:\n")

    if not ano.isdigit():
        print("Erro: só são permitidos números.")
        continue

    ano = int(ano)

    if ano <= 0:
        print("Erro: o ano deve ser maior que zero.")
    else:
        break

if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print(f"\nO ano {ano} é BISSEXTO.\n")
else:
    print(f"\nO ano {ano} não é BISSEXTO.\n")

proximo = ano + 1
while not (proximo % 4 == 0 and (proximo % 100 != 0 or proximo % 400 == 0)):
    proximo += 1

print(f"O próximo ano bissexto será {proximo}.\n")
