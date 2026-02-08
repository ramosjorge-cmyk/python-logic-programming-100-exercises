import os
import subprocess

"""Exercício 10
10) Faça um algoritmo que leia a largura e altura de uma parede, calcule e mostre a área a ser pintada e a quantidade de tinta necessária para o serviço, sabendo que cada litro de tinta pinta uma área de 2metros quadrados.
"""

# ============================================================
#  LIMPAR ECRÃ (Windows / Linux / macOS)
# ============================================================
def cls():
    """Limpa o terminal de forma compatível com vários sistemas operativos."""
    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run(comando, shell=True)


cls()
print("Digite a altura da parede (em metros).")
alt = float(input())
print("Digite a largura da parede (em metros).")
larg = float(input())
area = alt * larg
print(f"A área da parede é de {area:.2f} metros quadrados.")
print(f"Serão necessários {area/2:.2f} litros de tinta para pintar a parede.\n")