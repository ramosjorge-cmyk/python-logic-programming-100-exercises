# ============================================
# [46] Soma de pares de 6 a 100 / Sum of Even Numbers 6–100
# Tags: while, arithmetic, loop
#
# Descrição (PT):
#   O exercício soma todos os números pares entre 6 e 100. Trabalha filtragem por condição e acumulação.
#
# Description (EN):
#   The exercise sums all even numbers between 6 and 100. It reinforces conditional filtering and accumulation.
# ============================================

import os
import subprocess

"""Exercício 46
46) Crie um programa que calcule e mostre na tela o resultado da soma entre 6 + 8 + 10 + 12 + 14 + ... + 98 + 100.
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
    print (Fore.CYAN + Style.BRIGHT + "🔢 Simulador de Soma de Expressão 🔢")
    soma = sum(range(6, 101, 2))  # Começa em 6, vai até 100 (inclusive), com passo de 2
    print(Fore.GREEN + Style.BRIGHT + f"Resultado da soma dos números pares de 6 a 100: {soma}")
    
    # Pergunta para nova simulação
    novo = (
        input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()
    )

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break
