# ============================================
# [24] Preço da passagem / Travel Fare Calculation
# Tags: float, conditions
#
# Descrição (PT):
#   O programa calcula o preço da passagem com base na distância, aplicando tarifas diferentes conforme o limite.
#
# Description (EN):
#   The program computes travel fare based on distance, using different per‑kilometer rates depending on thresholds.
# ============================================

import os
import subprocess

"""Exercício 24
24) Faça um algoritmo que pergunte a distância 
que um passageiro deseja percorrer em Km. 
Calcule o preço da passagem, cobrando R$0.50 por Km 
para viagens até 200Km e R$0.45 para viagens mais longas.
"""

# ============================================================
#  LIMPAR ECRÃ (Windows / Linux / macOS)
# ============================================================
def cls():
    """Limpa o terminal de forma compatível com vários sistemas operativos."""
    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run(comando, shell=True)


cls()
distancia = float(input("Digite a distância a percorrer (em Km): "))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print("O preço da passagem é: {:.2f} €".format(preco))