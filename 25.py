import os
import subprocess

"""Exercício 25
25) [DESAFIO] Crie um programa que leia o tamanho de três segmentos de reta. 
Analise seus comprimentos e diga se é possível formar um triângulo com essas retas. 
Matematicamente, para três segmentos formarem um triângulo, o comprimento de cada 
lado deve ser menor que a soma dos outros dois.
"""

# ============================================================
#  LIMPAR ECRÃ (Windows / Linux / macOS)
# ============================================================
def cls():
    """Limpa o terminal de forma compatível com vários sistemas operativos."""
    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run(comando, shell=True)


cls()
distancia = float(input("Digite o tamanho de um segmento de reta: "))
distancia2 = float(input("Digite o tamanho de outro segmento de reta: "))
distancia3 = float(input("Digite o tamanho de outro segmento de reta: "))

if (distancia < distancia2 + distancia3) and (distancia2 < distancia + distancia3) and (distancia3 < distancia + distancia2):
    print("\nÉ possível formar um triângulo com essas retas.\n")
else:
    print("\nNão é possível formar um triângulo com essas retas.\n")