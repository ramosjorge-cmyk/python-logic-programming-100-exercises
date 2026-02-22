# ============================================
# [62] Idades com faça‑enquanto e estatísticas / Ages with Do‑While and Statistics
# Tags: do-while, input
#
# Descrição (PT):
#   O exercício lê idades até o utilizador parar e calcula quantidade, média e quantos têm 21 anos ou mais. Trabalha repetição controlada.
#
# Description (EN):
#   The exercise reads ages until the user stops and computes count, average, and how many are 21 or older. It practices user‑controlled loops.
# ============================================

import os
import subprocess

"""Exercício 62
62) Faça um programa usando a estrutura “faça enquanto” que leia a idade de várias pessoas. A cada laço, você deverá perguntar para o usuário se ele quer ou não continuar a digitar dados. No final, quando o usuário decidir parar, mostre na tela:
a) Quantas idades foram digitadas
b) Qual é a média entre as idades digitadas
c) Quantas pessoas tem 21 anos ou mais.
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

    print(Fore.CYAN + Style.BRIGHT + "Registro de Idades:\n")

    idades: list[int] = []
    while True:
        try:
            idade = int(input(Fore.YELLOW + "Digite a idade: "))
            idades.append(idade)
        except ValueError:
            print(Fore.RED + "Por favor, digite um número válido para a idade.")
        
        continuar = input(Fore.MAGENTA + "Deseja continuar a adicionar idades? (s/n): ").strip().lower()
        if continuar != "s":
            break

    # Cálculos
    total_idades = len(idades)
    media_idades = sum(idades) / total_idades if total_idades > 0 else 0
    pessoas_21_mais = sum(1 for idade in idades if idade >= 21)

    # Exibição dos resultados
    print(Fore.GREEN + Style.BRIGHT + f"\n📊 Resultados:")
    print(Fore.GREEN + f"   Total de idades registradas: {total_idades}")
    print(Fore.GREEN + f"   Média das idades: {media_idades:.2f}")
    print(Fore.GREEN + f"   Pessoas com 21 anos ou mais: {pessoas_21_mais}")



    # Pergunta para nova simulação
    novo = (
        input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()
    )

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break