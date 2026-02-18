import os
import subprocess

"""Exercício 30
30) [DESAFIO] Refaça o algoritmo 25, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais
- ESCALENO: todos os lados diferentes
"""

# ============================================================
#  LIMPAR ECRÃ (Windows / Linux / macOS)
# ============================================================
def cls():
    """Limpa o terminal de forma compatível com vários sistemas operativos."""
    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run(comando, shell=True)


cls()
# Loop infinito para garantir que o utilizador insere valores numéricos válidos
while True:
    try:
        # Solicita ao utilizador o tamanho dos três segmentos de reta
        distancia = float(input("Digite o tamanho de um segmento de reta: "))
        distancia2 = float(input("Digite o tamanho de outro segmento de reta: "))
        distancia3 = float(input("Digite o tamanho de outro segmento de reta: "))
        break  # Sai do loop se tudo foi inserido corretamente
    # Caso o utilizador insira algo que não seja número, mostra aviso e repete
    except ValueError:
        print("\nPor favor, digite um número válido.\n")

# Verifica se os três segmentos podem formar um triângulo
# Regra: cada lado deve ser menor que a soma dos outros dois
if (
    (distancia < distancia2 + distancia3)
    and (distancia2 < distancia + distancia3)
    and (distancia3 < distancia + distancia2)
):
    print("\nÉ possível formar um triângulo com essas retas.\n")

    # Verifica se todos os lados são iguais → triângulo equilátero
    if distancia == distancia2 == distancia3:
        print("O triângulo formado é EQUILÁTERO: todos os lados iguais.")
    # Verifica se pelo menos dois lados são iguais → triângulo isósceles
    elif distancia == distancia2 or distancia == distancia3 or distancia2 == distancia3:
        print("O triângulo formado é ISÓSCELES: dois lados iguais.")
    # Se não for equilátero nem isósceles, então é escaleno → todos os lados diferentes
    else:
        print("O triângulo formado é ESCALENO: todos os lados diferentes.")

# Se a condição para formar um triângulo não for satisfeita, informa o utilizador
else:
    print("\nNão é possível formar um triângulo com essas retas.\n")
