# ============================================
# [65] Contagem regressiva 100 a 0 / Countdown 100 to 0
# Tags: for, loop
#
# Descrição (PT):
#   O programa mostra uma contagem regressiva de 100 até 0 usando para. Trabalha decremento controlado.
#
# Description (EN):
#   The program displays a countdown from 100 to 0 using a for loop. It reinforces controlled decrement.
# ============================================

import os
import subprocess

"""Exercício 65
65) Desenvolva um programa usando a estrutura “para” que mostre na tela a seguinte contagem:
100 90 80 70 60 50 40 30 20 10 0 Acabou!
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

    print(Fore.CYAN + Style.BRIGHT + "Contagem regressiva de 100 a 0 (decremento de 10):\n")
    
    for i in range(100, -1, -10):
        print(Fore.YELLOW + f"{i}", end=" ")
        time.sleep(0.4)  # atraso de 0.3 segundos entre cada número

    print(Fore.GREEN + "\nAcabou!")

    time.sleep(3)  # pausa para o utilizador ver o resultado antes de perguntar sobre nova simulação
    
    # Pergunta para nova simulação
    novo = (
        input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()
    )

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break
