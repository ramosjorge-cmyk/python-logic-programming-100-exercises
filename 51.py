# ============================================
# [51] Maior e menor preço / Highest and Lowest Price
# Tags: input, float, comparison
#
# Descrição (PT):
#   O programa lê o preço de 8 produtos e identifica o maior e o menor valor digitado. Trabalha comparação contínua e análise de dados numéricos.
#
# Description (EN):
#   The program reads the prices of 8 products and identifies the highest and lowest values. It practices continuous comparison and numeric analysis.
# ============================================

import os
import subprocess

"""Exercício 51
51) Faça um aplicativo que leia o preço de 8 produtos. 
No final, mostre na tela qual foi o maior e qual foi o menor preço digitados.
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
    produtos = []
    
    for i in range(8):
        while True:
            try:
                preco = float(input(Fore.YELLOW + f"Digite o preço do produto {i+1}: "))
                produtos.append(preco)
                break
            except ValueError:
                print(Fore.RED + "❌ Entrada inválida. Por favor, digite um número válido.")
    
    print(Fore.CYAN + f"\n📋 Produtos: {produtos}")
    print(Fore.CYAN + "\n📊 Analisando os preços...")

    maior_preco = max(produtos)
    menor_preco = min(produtos)

    print(Fore.GREEN + f"✅ Maior preço: {maior_preco:.2f}€")
    print(Fore.GREEN + f"✅ Menor preço: {menor_preco:.2f}€")

    # Pergunta para nova simulação
    novo = (
        input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()
    )

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break
