# ============================================
# [43] Contagem regressiva marcando divisíveis por 4 / Countdown Marking Multiples of 4
# Tags: while, modulo, loop
#
# Descrição (PT):
#   O programa faz contagem regressiva de 30 a 1 destacando números divisíveis por 4. Trabalha uso do operador módulo.
#
# Description (EN):
#   The program performs a countdown from 30 to 1 marking numbers divisible by 4. It practices modulo operations.
# ============================================

import os
import subprocess

"""Exercício 43
43) Desenvolva um algoritmo que mostre uma contagem regressiva de 30 até 1,
marcando os números que forem divisíveis por 4, exatamente como mostrado
abaixo: 30 29 [28] 27 26 25 [24] 23 22 21 [20] 19 18 17 [16]...
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
import time


cls()
print(Fore.CYAN + Style.BRIGHT + "🔢 Contagem Regressiva de 30 até 1\n")
for i in range(30, 0, -1):
        if i % 4 == 0:
            print(Fore.RED + Style.BRIGHT + f"[{i}]", end=" ", flush=True)
            time.sleep(0.5)
        else:
            print(Fore.WHITE + str(i), end=" ", flush=True)
            time.sleep(0.5)

print("\n\n" + Fore.GREEN + "Pressione Enter para sair...")
input()
