# ============================================
# [02] Saudação personalizada / Personalized Greeting
# Tags: input, strings, print
#
# Descrição (PT):
#   O programa lê o nome do utilizador e exibe uma mensagem personalizada de boas‑vindas. Trabalha leitura de dados, manipulação simples de strings e saída formatada.
#
# Description (EN):
#   The program reads the user’s name and displays a personalized welcome message. It practices input handling, basic string manipulation, and formatted output.
# ============================================

import os
import subprocess

"""Exercício 2
2) Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas vindas para ela:
Ex:
Qual é o seu nome? João da Silva
Olá João da Silva, é um prazer te conhecer!
"""

# ============================================================
#  LIMPAR ECRÃ (Windows / Linux / macOS)
# ============================================================
def cls():
    """Limpa o terminal de forma compatível com vários sistemas operativos."""
    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run(comando, shell=True)


cls()
nome = input("Qual o seu nome?\n")
print(f"\nOlá {nome}, é um prazer conhecer-te!\n")