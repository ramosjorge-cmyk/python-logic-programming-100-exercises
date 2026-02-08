import os
import subprocess

"""Exercício 28
28) Faça um programa que leia a largura e o comprimento de um terreno
retangular, calculando e mostrando a sua área em m². O programa também
devemostrar a classificação desse terreno, de acordo com a lista
abaixo: - Abaixo de 100m² = TERRENO POPULAR
- Entre 100m² e 500m² = TERRENO MASTER
- Acima de 500m² = TERRENO VIP
"""

# ============================================================
#  LIMPAR ECRÃ (Windows / Linux / macOS)
# ============================================================
def cls():
    """Limpa o terminal de forma compatível com vários sistemas operativos."""
    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run(comando, shell=True)


cls()
largura = float(input("Digite a largura do terreno (em metros): "))
comprimento = float(input("Digite o comprimento do terreno (em metros): "))

area = largura * comprimento
print(f"\nA área do terreno é: {area:.2f} m²")

if area < 100:
    print("Classificação: TERRENO POPULAR\n")
elif 100 <= area <= 500:
    print("Classificação: TERRENO MASTER\n")
else:
    print("Classificação: TERRENO VIP\n")