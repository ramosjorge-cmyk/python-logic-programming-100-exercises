# ============================================
# [79] Vetor com pares e posições / Even Numbers and Positions
# Tags: list, modulo
#
# Descrição (PT):
#   O programa lê 10 números e mostra quais são pares e em que posições estão. Trabalha classificação numérica e indexação.
#
# Description (EN):
#   The program reads 10 numbers and displays which are even and their positions. It reinforces numeric classification and indexing.
# ============================================

import os
import subprocess

"""Exercício 79
79) Desenvolva um programa que leia 10 números inteiros e guarde-os em um vetor.  
No final, mostre quais são os números pares que foram digitados e em que  
posições eles estão armazenados.
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

    print(Fore.CYAN + Style.BRIGHT + "🔢 Simulador de Números Pares\n")
    print(Fore.YELLOW + "Digite 10 números inteiros para descobrir quais são pares e suas posições.")

    # Inicialização do vetor
    numeros: list[int] = []

    # guarda de 10 números inteiros
    for i in range(10):
        while True:
            try:
                num = int(input(Fore.GREEN + f"Digite o {i+1}º número: "))
                numeros.append(num) # adiciona o número ao vetor
                break
            except ValueError: # trata entrada inválida
                print(Fore.RED + "⚠️  Entrada inválida. Digite um número inteiro.")

    # exibição dos números pares e suas posições
    pares: list[tuple[int, int]] = [] # lista para armazenar tuplas de (posição, número)
    for i, num in enumerate(numeros): # percorrer o vetor com índice e valor
        if num % 2 == 0:
            pares.append((i, num))

    if pares:
        print(Fore.BLUE + "\n🔢 Números pares e suas posições:")
        for pos, num in pares:
            print(Fore.BLUE + f" Posição {pos+1}: {num}")
    else:
        print(Fore.RED + "\n❌ Nenhum número par foi digitado.")

    # Pergunta para nova simulação
    novo = (
        input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()
    )

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break
