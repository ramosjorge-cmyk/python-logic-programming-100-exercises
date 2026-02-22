# ============================================
# [38] Contagem de 6 a 11 / Counting 6 to 11
# Tags: while, loop, int
#
# Descrição (PT):
#   O exercício exibe uma contagem crescente de 6 a 11 usando um laço enquanto. Trabalha repetição simples.
#
# Description (EN):
#   The exercise displays a count from 6 to 11 using a while loop. It reinforces simple repetition.
# ============================================

# ============================================
# [39] Contagem regressiva de 10 a 3 / Countdown 10 to 3
# Tags: while, loop
#
# Descrição (PT):
#   O programa mostra uma contagem regressiva de 10 até 3. Trabalha decremento em laços.
#
# Description (EN):
#   The program displays a countdown from 10 to 3. It practices decrement loops.
# ============================================

# ============================================
# [40] Contagem de 0 a 18 de 3 em 3 / Count 0 to 18 by 3
# Tags: while, loop, step
#
# Descrição (PT):
#   O exercício exibe uma contagem de 0 a 18 avançando de 3 em 3. Trabalha incrementos personalizados.
#
# Description (EN):
#   The exercise displays a count from 0 to 18 stepping by 3. It reinforces custom step control.
# ============================================

# ============================================
# [41] Contagem de 100 a 0 de 5 em 5 / Count 100 to 0 by 5
# Tags: while, loop, step
#
# Descrição (PT):
#   O programa mostra uma contagem regressiva de 100 a 0 diminuindo de 5 em 5. Trabalha decrementos personalizados.
#
# Description (EN):
#   The program displays a countdown from 100 to 0 decreasing by 5. It practices custom decrement loops.
# ============================================

import os
import subprocess

"""Exercício 38 + 39 + 40 + 41
38) Escreva um programa que mostre na tela a seguinte contagem:
6 7 8 9 10 11 Acabou!
39) Faça um algoritmo que mostre na tela a seguinte contagem:
10 9 8 7 6 5 4 3 Acabou!
40) Crie um aplicativo que mostre na tela a seguinte
contagem: 0 3 6 9 12 15 18 Acabou!
41) Desenvolva um programa que mostre na tela a seguinte
contagem: 100 95 90 85 80 ... 0 Acabou!
"""

# ============================================================
#  LIMPAR ECRÃ (Windows / Linux / macOS)
# ============================================================
def cls():
    """Limpa o terminal de forma compatível com vários sistemas operativos."""
    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run(comando, shell=True)

import time
from colorama import Fore, Style, init
init(autoreset=True)

while True:
    cls()
    print(Fore.CYAN + Style.BRIGHT + "🔢 Contagens")

    # ============================
    #  CONTAGEM 38
    # ============================
    print(Fore.MAGENTA + Style.BRIGHT + "\n📌 Contagem 38: 6 a 11")
    for i in range(6, 12):
        print(Fore.GREEN + str(i), end=" ", flush=True)
        time.sleep(0.5)
    print(Fore.YELLOW + "\nAcabou!")

    # ============================
    #  CONTAGEM 39
    # ============================
    print(Fore.MAGENTA + Style.BRIGHT + "\n📌 Contagem 39: 10 até 3 (decrescente)")
    for i in range(10, 2, -1):
        print(Fore.GREEN + str(i), end=" ", flush=True)
        time.sleep(0.5)
    print(Fore.YELLOW + "\nAcabou!")

    # ============================
    #  CONTAGEM 40
    # ============================
    print(Fore.MAGENTA + Style.BRIGHT + "\n📌 Contagem 40: múltiplos de 3 até 18")
    for i in range(0, 19, 3):
        print(Fore.GREEN + str(i), end=" ", flush=True)
        time.sleep(0.5)
    print(Fore.YELLOW + "\nAcabou!")

    # ============================
    #  CONTAGEM 41
    # ============================
    print(Fore.MAGENTA + Style.BRIGHT + "\n📌 Contagem 41: de 100 até 0 (de 5 em 5)")
    for i in range(100, -1, -5):
        print(Fore.GREEN + str(i), end=" ", flush=True)
        time.sleep(0.5)
    print(Fore.YELLOW + "\nAcabou!\n")

    # Pergunta para nova simulação
    novo = input(Fore.MAGENTA + "🔁 Deseja simular novamente? (s/n): ").strip().lower()

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break
