# ============================================
# [67] Contagem até valor digitado / Count Up to User Value
# Tags: for, loop
#
# Descrição (PT):
#   O programa lê um número inteiro positivo e exibe contagem de 0 até ele. Trabalha repetição controlada pelo utilizador.
#
# Description (EN):
#   The program reads a positive integer and counts from 0 up to it. It reinforces user‑driven loop limits.
# ============================================

import os
import subprocess

"""Exercício 67
67) Faça um programa usando a estrutura “para” que leia um número inteiro positivo 
e mostre na tela uma contagem de 0 até o valor digitado: Ex: Digite um valor: 9
Contagem: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, FIM!
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
    
    print(Fore.CYAN + Style.BRIGHT + "🔢 Contagem de 0 até um número inteiro positivo\n")

    # Solicita ao utilizador um número inteiro positivo
    try:
        num = int(input(Fore.YELLOW + "Digite um número inteiro positivo: "))
        if num < 0:
            print(Fore.RED + "❌ Por favor, insira um número inteiro positivo.")
            continue
        print(Fore.GREEN + f"\nContagem de 0 até {num}:")
        for i in range(0, num + 1):
            if i == num:
                print(Fore.WHITE + f"{i}, FIM!")
            else:
                print(Fore.WHITE + f"{i}, ", end="")
    except ValueError:
        print(Fore.RED + "❌ Por favor, insira um número inteiro válido.")

    # Pergunta para nova simulação
    novo = (
        input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()
    )

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break
