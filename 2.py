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