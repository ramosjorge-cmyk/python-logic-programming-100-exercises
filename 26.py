import os
import subprocess

"""Exercício 26
26) Escreva um algoritmo que leia dois números inteiros e compare-os, 
mostrando na tela uma das mensagens abaixo:
- O primeiro valor é o maior
- O segundo valor é o maior
- Não existe valor maior, os dois são iguais
"""

# ============================================================
#  LIMPAR ECRÃ (Windows / Linux / macOS)
# ============================================================
def cls():
    """Limpa o terminal de forma compatível com vários sistemas operativos."""
    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run(comando, shell=True)


cls()
valor1 = int(input("Digite o primeiro número inteiro; "))
valor2 = int(input("Digite o segundo número inteiro; "))

if valor1 > valor2:
    print("\nO primeiro valor é o maior.")
elif valor2 > valor1:
    print("\nO segundo valor é o maior.")
else:
    print("\nNão existe valor maior, os dois são iguais.")