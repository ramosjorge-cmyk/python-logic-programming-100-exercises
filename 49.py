# ============================================
# [49] Contagem de pares e ímpares / Count Even and Odd Numbers
# Tags: while, modulo, input
#
# Descrição (PT):
#   O programa lê 6 números e conta quantos são pares e quantos são ímpares. Trabalha classificação numérica.
#
# Description (EN):
#   The program reads 6 numbers and counts how many are even and how many are odd. It practices numeric classification.
# ============================================

import os
import subprocess

"""Exercício 49
49) Crie um programa que leia 6 números inteiros e no final 
mostre quantos deles são pares e quantos são ímpares.
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
    num = []
    par = 0
    impar = 0
    
    print(Fore.CYAN + Style.BRIGHT + "🔢 Simulador de Números Pares e Ímpares\n")
    for i in range(6):
        while True:    
            try:
                numero = int(input(Fore.YELLOW + f"Digite o {i+1}º número inteiro: "))
                num.append(numero)
                break
            except ValueError:
                print(Fore.RED + "❌ Entrada inválida. Por favor, digite um número inteiro.")
    # Contagem de números pares e ímpares
    for n in num:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
    print(Fore.GREEN + f"✅ Números pares: {par}")
    print(Fore.GREEN + f"✅ Números ímpares: {impar}")
    
    # Pergunta para nova simulação
    novo = (
        input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()
    )

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break
