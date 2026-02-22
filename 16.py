# ============================================
# [16] Redução do tempo de vida do fumante / Smoker Life Reduction
# Tags: arithmetic, health, conversion
#
# Descrição (PT):
#   O programa calcula quantos dias de vida um fumante perde com base nos cigarros fumados e anos de hábito.
#
# Description (EN):
#   The program estimates how many days of life a smoker loses based on cigarettes per day and years smoked.
# ============================================

import os
import subprocess

"""Exercício 17
17) Escreva um programa que pergunte a velocidade de um carro. Caso ultrapasse 80Km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$5 por cada Km acima da velocidade permitida.
"""

# ============================================================
#  LIMPAR ECRÃ (Windows / Linux / macOS)
# ============================================================
def cls():
    """Limpa o terminal de forma compatível com vários sistemas operativos."""
    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run(comando, shell=True)


cls()
print("Qual a velocidade do carro?")
velocidade = int(input())
if velocidade > 80:
    km_acima = velocidade - 80
    multa = km_acima * 5
    print(f"\nO carro foi multado por excesso de velocidade. O valor da multa é {int(multa)} euros.\n")
else:
    print("\nO carro está dentro do limite de velocidade.\n")