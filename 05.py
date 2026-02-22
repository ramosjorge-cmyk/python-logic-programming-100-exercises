# ============================================
# [05] Média de duas notas / Average of Two Grades
# Tags: input, float, arithmetic
#
# Descrição (PT):
#   O exercício lê duas notas de um aluno e calcula a média aritmética. Trabalha operações com números decimais e apresentação de resultados formatados.
#
# Description (EN):
#   The exercise reads two student grades and computes their average. It practices floating‑point arithmetic and formatted output.
# ============================================

import os
import subprocess

"""Exercício 5
5) Faça um programa que leia as duas notas de um aluno em uma matéria e mostre na tela a sua média na disciplina.
Ex:
Nota 1: 4.5
Nota 2: 8.5
A média entre 4.5 e 8.5 é igual a 6.5
"""

# ============================================================
#  LIMPAR ECRÃ (Windows / Linux / macOS)
# ============================================================
def cls():
    """Limpa o terminal de forma compatível com vários sistemas operativos."""
    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run(comando, shell=True)


cls()
print("Digite uma nota.")
nr1 = float(input())
print("Digite outra nota.")
nr2 = float(input())
print(f"A média entre {nr1} e {nr2}.")
print(f"A média entre {nr1} e {nr2} é igual a {(nr1 + nr2) / 2 }.")