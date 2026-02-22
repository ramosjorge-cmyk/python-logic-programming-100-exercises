# ============================================
# [08] Conversão de metros / Meter Unit Conversion
# Tags: float, arithmetic, conversion
#
# Descrição (PT):
#   O programa lê uma distância em metros e converte para múltiplas unidades métricas. Trabalha conversões proporcionais e cálculos simples.
#
# Description (EN):
#   The program reads a distance in meters and converts it into multiple metric units. It reinforces proportional calculations and unit conversion.
# ============================================

import os
import subprocess

"""Exercício 8
8) Desenvolva um programa que leia uma distância em metros e mostre os valores relativos em outras medidas.
Ex:
Digite uma distância em metros: 185.72
A distância de 85.7m corresponde a:
0.18572Km 1.8572Hm 18.572Dam
"""

# ============================================================
#  LIMPAR ECRÃ (Windows / Linux / macOS)
# ============================================================
def cls():
    """Limpa o terminal de forma compatível com vários sistemas operativos."""
    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run(comando, shell=True)


cls()
print("Digite uma distância em metros.")
d = float(input())
print(f"A distância de {d}m corresponde a:")
print(f"{d/1000:.5f}Km")
print(f"{d/100:.2f}Hm")
print(f"{d/10:.1f}Dam")
print(f"{d*10:.0f}dm")
print(f"{d*100:.0f}cm")
print(f"{d*1000:.0f}mm\n")