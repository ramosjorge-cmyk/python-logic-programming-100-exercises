# ============================================
# [29] Reajuste salarial por tempo / Salary Adjustment by Years
# Tags: float, conditions, percentage
#
# Descrição (PT):
#   O exercício aplica um aumento salarial baseado nos anos de empresa. Trabalha condições encadeadas e cálculos percentuais.
#
# Description (EN):
#   The exercise applies a salary raise based on years of employment. It reinforces chained conditions and percentage calculations.
# ============================================

import os
import subprocess

"""Exercício 29
29) Desenvolva um programa que leia o nome de um funcionário, seu salário,
quantos anos ele trabalha na empresa e mostre seu novo salário, reajustado de
acordo com a tabela a seguir:
- Até 3 anos de empresa: aumento de 3%
- entre 3 e 10 anos: aumento de 12.5%
- 10 anos ou mais: aumento de 20%
"""

# ============================================================
#  LIMPAR ECRÃ (Windows / Linux / macOS)
# ============================================================
def cls():
    """Limpa o terminal de forma compatível com vários sistemas operativos."""
    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run(comando, shell=True)


cls()
nome = input("Digite o nome do funcionário: ")
salario = float(input("Digite o salário do funcionário: "))
anos_trabalho = int(input("Digite há quantos anos o funcionário trabalha na empresa: "))

if anos_trabalho <= 3:
    aumento = salario * 0.03
elif 3 < anos_trabalho < 10:
    aumento = salario * 0.125
else: aumento = salario * 0.20

novo_salario = salario + aumento
print(f"\nO novo salário do funcionário {nome} é: {novo_salario:.2f}€.\n")