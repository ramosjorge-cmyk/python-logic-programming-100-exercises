# ============================================
# [78] Vetor com 15 números e múltiplos de 10 / Vector and Multiples of 10
# Tags: list, modulo
#
# Descrição (PT):
#   O exercício lê 15 números e identifica quais são múltiplos de 10 e em que posições aparecem. Trabalha análise posicional e filtragem.
#
# Description (EN):
#   The exercise reads 15 numbers and identifies which are multiples of 10 and their positions. It practices positional analysis and conditional filtering.
# ============================================

import os
import subprocess

"""Exercício 78
78) Escreva um programa que leia 15 números e guarde-os em um vetor. 
No final, mostre o vetor inteiro na tela e em seguida mostre em que posições foram  
digitados valores que são múltiplos de 10.
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
import random

while True:
    cls()

    print(Fore.CYAN + Style.BRIGHT + "🔢 Simulador de vetor de números 🔢\n")
    # inicialização do vetor
    numeros: list[int] = [random.randint(1, 50) for _ in range(15)]  # vetor de 15 números aleatórios (substitua por [] para entrada manual)   

    # coleta de 15 números (Descomente o bloco abaixo para entrada manual)
    # numeros: list[int] = []  # vetor de 15 números aleatórios (substitua por [] para entrada manual)   
    # for i in range(15):
    #    while True:
    #        try:
    #           num = int(input(Fore.YELLOW + f"Digite o {i+1}º número: ")) # Adiciona o número ao vetor
    #           numeros.append(num) # acrescenta o número ao vetor
    #           break
    #       except ValueError: # trata a exceção caso o usuário digite algo que não seja um número inteiro
    #           print(Fore.RED + "⚠️  Entrada inválida. Digite um número inteiro.")

    # exibição do vetor completo
    print(Fore.GREEN + "📋 Vetor completo:")
    for i, num in enumerate(numeros):
        print(Fore.GREEN + f" Posição {i+1}: {num}")
        time.sleep(0.50)  # animação na exibição

    # exibição das posições dos múltiplos de 10
    multiplos = [i for i, num in enumerate(numeros) if num % 10 == 0]

    if multiplos:
        print(Fore.BLUE + "\n🔢 Posições dos múltiplos de 10:")
        time.sleep(0.50)  # animação na exibição
        for pos in multiplos:
            print(Fore.BLUE + f" Posição {pos+1}")
            time.sleep(0.50)  # animação na exibição
    else:
        print(Fore.RED + "\n❌ Nenhum múltiplo de 10 encontrado.")

    # Pergunta para nova simulação
    novo = (
        input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()
    )

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break
