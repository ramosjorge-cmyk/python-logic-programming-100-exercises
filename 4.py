import os
import subprocess

"""Exercício 4
4) Desenvolva um algoritmo que leia dois números inteiros e mostre o somatório entre eles.
Ex:
Digite um valor: 8
Digite outro valor: 5
A soma entre 8 e 5 é igual a 13.
"""

# ============================================================
#  LIMPAR ECRÃ (Windows / Linux / macOS)
# ============================================================
def cls():
    """Limpa o terminal de forma compatível com vários sistemas operativos."""
    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run(comando, shell=True)


cls()
print("Digite um número.")
nr1 = int(input())
print("Digite outro número.")
nr2 = int(input())
print(f"O primeiro número é {nr1} e o segundo número é {nr2}.")
print(f"A soma entre {nr1} e {nr2} é igual a {nr1 + nr2}.")