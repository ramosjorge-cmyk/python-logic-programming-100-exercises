# ============================================
# [19] Média e aproveitamento / Grade Average and Evaluation
# Tags: float, conditions
#
# Descrição (PT):
#   O exercício calcula a média de duas notas e avalia se o aluno teve bom aproveitamento.
#
# Description (EN):
#   The exercise computes the average of two grades and evaluates performance based on the result.
# ============================================

import os
import subprocess

"""Exercício 19
19) Crie um algoritmo que leia o nome e as duas notas de um aluno, calcule a sua média e mostre na tela. No final, analise a média e mostre se o aluno teve ou não um bom aproveitamento (se ficou acima da média 7.0).
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
    nome = input("Qual o seu nome?\n")
    if nome.replace(" ", "").isalpha():
        break
    else:
        print("Erro: só são permitidas letras.")

print("Qual a sua primeira nota?")
nota1 = float(input())
print("Qual a sua segunda nota?")
nota2 = float(input())
media = (nota1 + nota2) / 2
print(f"\nO aluno {nome} tem média {media:.2f}")
if media >= 7.0:
    print("O aluno teve um bom aproveitamento.\n")
else:
    print("O aluno não teve um bom aproveitamento.\n")