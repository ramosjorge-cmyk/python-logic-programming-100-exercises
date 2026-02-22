# ============================================
# [99] Função Potência / Power Function
# Tags: function, arithmetic
#
# Descrição (PT):
#   O programa cria uma função que calcula a exponenciação com base e expoente. Trabalha operações matemáticas.
#
# Description (EN):
#   The program creates a function that calculates exponentiation using base and exponent. It reinforces mathematical operations.
# ============================================

import os
import subprocess

"""Exercício 99
99) Faça um programa que possua uma função chamada Potencia(), que vai receber  
dois parâmetros numéricos (base e expoente) e vai calcular o resultado da  
exponenciação.  
Ex: Potencia(5,2) vai calcular 52 = 25  
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

    print(Fore.CYAN + Style.BRIGHT + "🔢 Simulador de Potência\n"
        + Fore.YELLOW + "📐 Potencia(base, expoente) - Calcula a potência de um número\n ")
    
    # Entrada de dados
    try:
        base = float(input(Fore.YELLOW + "📐 Digite a base: "))
        expoente = float(input(Fore.YELLOW + "📏 Digite o expoente: "))
    except ValueError:
        print(Fore.RED + "❌ Entrada inválida! Por favor, insira números válidos.")
        input(Fore.MAGENTA + "Pressione Enter para tentar novamente...")
        continue

    # Cálculo da potência
    resultado = base ** expoente # Utiliza o operador de exponenciação para calcular o resultado

    # Exibição do resultado
    print(Fore.GREEN + Style.BRIGHT + f"\n✅ O resultado de {base} elevado a {expoente} é: {resultado}")
    
        # Pergunta para nova simulação
    novo = (
        input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()
    )

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break
