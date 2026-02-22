# ============================================
# [50] Sorteio de 20 números e análises / Random Numbers Analysis
# Tags: random, list, loop
#
# Descrição (PT):
#   O exercício sorteia 20 números e exibe quantos são maiores que 5 e quantos são divisíveis por 3. Trabalha listas e análise de dados.
#
# Description (EN):
#   The exercise draws 20 random numbers and shows how many are above 5 and how many are divisible by 3. It reinforces lists and data analysis.
# ============================================

import os
import subprocess
from random import randint

"""Exercício 50
50) Desenvolva um programa que faça o sorteio de 20 números entre 0 e 10 e mostre na tela:
a) Quais foram os números sorteados
b) Quantos números estão acima de 5
c) Quantos números são divisíveis por 3
"""

# ============================================================
#  LIMPAR ECRÃ (Windows / Linux / macOS)
# ============================================================
def cls():
    """Limpa o terminal de forma compatível com vários sistemas operativos."""
    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run(comando, shell=True)

from colorama import Fore, Style, init
init(autoreset=True)

while True:
    cls()

    # Sorteio de 20 números entre 0 e 10
    numeros_sorteados = [randint(0, 10) for _ in range(20)]

    # Mostrar os números sorteados
    print(Fore.CYAN + Style.BRIGHT + f"🔢 Números sorteados: {numeros_sorteados}")

    # Contar números acima de 5
    acima_de_5 = sum(1 for n in numeros_sorteados if n > 5)
    print(Fore.GREEN + f"✅ Números acima de 5: {acima_de_5}")

    # Contar números divisíveis por 3
    divisiveis_por_3 = sum(1 for n in numeros_sorteados if n % 3 == 0)
    print(Fore.GREEN + f"✅ Números divisíveis por 3: {divisiveis_por_3}")

    # Pergunta para nova simulação
    novo = (
        input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()
    )

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break
