# ============================================
# [64] Contagem 0 a 40 de 5 em 5 / Count 0 to 40 by 5
# Tags: for, loop
#
# Descrição (PT):
#   O exercício exibe uma contagem de 0 a 40 avançando de 5 em 5 usando para. Trabalha incrementos fixos.
#
# Description (EN):
#   The exercise displays a count from 0 to 40 stepping by 5 using a for loop. It practices fixed‑step repetition.
# ============================================

import os
import subprocess

"""Exercício 64
64) Desenvolva um programa usando a estrutura “para” que mostre na tela a seguinte contagem:
0 5 10 15 20 25 30 35 40 Acabou!
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

while True:
    cls()

    print(Fore.CYAN + Style.BRIGHT + "Contagem de 0 a 40 (incremento de 5):\n")
    
    for i in range(0, 41, 5):
        print(Fore.YELLOW + f"{i}", end=" ")
        time.sleep(0.4)  # atraso de 0.3 segundos entre cada número

    print(Fore.GREEN + "\nAcabou!")

    time.sleep(1)  # pausa para o utilizador ver o resultado antes de perguntar sobre nova simulação
    
    # Pergunta para nova simulação
    novo = (
        input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()
    )

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break
