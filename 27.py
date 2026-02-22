# ============================================
# [27] Média com classificação / Average with Classification
# Tags: float, conditions
#
# Descrição (PT):
#   O exercício calcula a média de duas notas e classifica o aluno conforme as faixas definidas. Trabalha condições compostas e interpretação de resultados.
#
# Description (EN):
#   The exercise computes the average of two grades and classifies the student according to defined ranges. It reinforces compound conditions and result interpretation.
# ============================================

import os
import subprocess

"""Exercício 27
27) Crie um programa que leia duas notas de um aluno e calcule a sua média,
mostrando uma mensagem no final, de acordo com a média atingida: - Média
até 4.9: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
"""

# ============================================================
#  LIMPAR ECRÃ (Windows / Linux / macOS)
# ============================================================
def cls():
    """Limpa o terminal de forma compatível com vários sistemas operativos."""
    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run(comando, shell=True)


cls()
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media < 5.0:
    print(f"Média: {media:.1f} - REPROVADO")
elif media < 7.0:
    print(f"Média: {media:.1f} - RECUPERAÇÃO")
else:
    print(f"Média: {media:.1f} - APROVADO")