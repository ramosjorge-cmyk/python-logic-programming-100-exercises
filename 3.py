import os
import subprocess

"""Exercício 3
3) Crie um programa que leia o nome e o salário de um funcionário, mostrando no final uma mensagem.
Ex:
Nome do Funcionário: Maria do Carmo
Salário: 1850,45
O funcionário Maria do Carmo tem um salário de R$1850,45 em Junho.
"""

# ============================================================
#  LIMPAR ECRÃ (Windows / Linux / macOS)
# ============================================================
def cls():
    """Limpa o terminal de forma compatível com vários sistemas operativos."""
    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run(comando, shell=True)


cls()
print("Qual o seu nome?")
nome = input()
print("Qual o seu salário?")
salario = float(input())
print(f"O funcionário {nome} tem um salário de {int(salario)} euros em Junho.")
print(f"O funcionário {nome} tem um salário de {salario:.2f} euros em Junho.")
print(f"O funcionário {nome} tem um salário de {salario:.0f} euros em Junho.")