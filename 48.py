# ============================================
# [48] Soma de 7 números / Sum of 7 Integers
# Tags: while, input, arithmetic
#
# Descrição (PT):
#   O exercício lê 7 números inteiros e calcula o somatório total. Trabalha repetição fixa.
#
# Description (EN):
#   The exercise reads 7 integers and computes their total sum. It reinforces fixed‑length loops.
# ============================================

import os
import subprocess

"""Exercício 48
48) Faça um programa que leia 7 números inteiros e no final mostre o somatório entre eles
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
    print (Fore.CYAN + Style.BRIGHT + "🔢 Simulador de Soma de Números Inteiros\n")
    
# Coletar 7 números inteiros
    numeros = []
    for i in range(7):
        while True:
            try:
                num = int(input(Fore.YELLOW + f"Digite o {i+1}º número inteiro: "))
                numeros.append(num)
                break
            except ValueError:
                print(Fore.RED + Style.BRIGHT + "❌ Por favor, insira um número inteiro válido.")

    # Calcular a soma dos números
    soma = sum(numeros)
    print(Fore.GREEN + Style.BRIGHT + f"✅ A soma dos números é: {soma}")

    # Pergunta para nova simulação
    novo = (
        input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()
    )

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break
