# ============================================
# [01] Olá, Mundo! / Hello World
# Tags: print, básico
#
# Descrição (PT):
#   Primeiro exercício introdutório. O objetivo é exibir uma mensagem simples no ecrã, praticando a execução básica de um programa Python e o uso do comando print.
#
# Description (EN):
#   First introductory exercise. The goal is to display a simple message on the screen, practicing basic Python execution and the use of the print command.
# ============================================

import os
import subprocess

"""Exercício 1
1) Escreva um programa que mostre na tela a mensagem "Olá, Mundo!"
"""

# ============================================================
#  LIMPAR ECRÃ (Windows / Linux / macOS)
# ============================================================
def cls():
    """Limpa o terminal de forma compatível com vários sistemas operativos."""
    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run(comando, shell=True)


cls()
print("Olá, Mundo!")
print("\n")