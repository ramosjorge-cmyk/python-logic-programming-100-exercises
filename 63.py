# ============================================
# [63] Números com faça‑enquanto e análises / Numbers with Do‑While and Analysis
# Tags: do-while, input, arithmetic
#
# Descrição (PT):
#   O programa lê vários números e mostra soma, menor valor, média e quantidade de pares. Trabalha análise numérica.
#
# Description (EN):
#   The program reads several numbers and displays the sum, smallest value, average, and count of even numbers. It reinforces numeric analysis.
# ============================================

import os
import subprocess

"""Exercício 63
63) Crie um programa usando a estrutura “faça enquanto” que leia vários números. A cada laço, pergunte se o usuário quer continuar ou não. No final, mostre na tela:
a) O somatório entre todos os valores
b) Qual foi o menor valor digitado
c) A média entre todos os valores
d) Quantos valores são pares
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

    print(Fore.CYAN + Style.BRIGHT + "📊 Simulador de Números\n")

    numeros: list[float] = []

    while True:
        try:
            num = float(input(Fore.YELLOW + "Digite um número: "))
            numeros.append(num)
        except ValueError:
            print(Fore.RED + "⚠️ Entrada inválida. Por favor, digite um número válido.")
            continue

        cont = input(Fore.MAGENTA + "Deseja continuar? (s/n): ").strip().lower()
        if cont != "s":
            break

    # Cálculos
    total = sum(numeros)
    menor = min(numeros) if numeros else 0
    media = total / len(numeros) if numeros else 0
    pares = sum(1 for n in numeros if n % 2 == 0)

    # Exibição dos resultados
    print(Fore.GREEN + Style.BRIGHT + f"\n📊 Resultados:")
    print(Fore.GREEN + f"   Somatório: {total}")
    print(Fore.GREEN + f"   Menor valor: {menor}")
    print(Fore.GREEN + f"   Média: {media:.2f}")
    print(Fore.GREEN + f"   Números pares: {pares}")


    # Pergunta para nova simulação
    novo = (
        input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()
    )

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break
