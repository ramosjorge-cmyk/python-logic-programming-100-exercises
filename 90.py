import os
import subprocess

"""Exercício 90
90) Desenvolva um algoritmo que leia dois valores pelo teclado e passe esses  
valores para um procedimento Somador() que vai calcular e mostrar a soma entre  
eles. 
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

# Entrada de dados
    print(Fore.CYAN + Style.BRIGHT + "🔢 Simulador de Soma de Valores")

    # ============================================================
    #  VALIDAÇÃO DO PRIMEIRO VALOR
    # ============================================================
    while True:
        valor1_str = input(Fore.YELLOW + "🔢 Digite o primeiro valor: ").strip()  # primeiro valor

        if not valor1_str.isdigit():  # verifica se é um número inteiro positivo
            print(Fore.RED + "❌ Digite apenas números inteiros positivos.")
            continue

        valor1 = int(valor1_str) # converte para inteiro
        break  # primeiro valor válido

    # ============================================================
    #  VALIDAÇÃO DO SEGUNDO VALOR
    # ============================================================
    while True:
        valor2_str = input(Fore.YELLOW + "🔢 Digite o segundo valor: ").strip()  # segundo valor

        if not valor2_str.isdigit():  # verifica se é um número inteiro positivo
            print(Fore.RED + "❌ Digite apenas números inteiros positivos.")
            continue

        valor2 = int(valor2_str) # converte para inteiro
        break  # segundo valor válido

    def somador(v1: int, v2: int) -> None: # definição do procedimento somador com os parâmetros v1 e v2 do tipo inteiro
        """Função que calcula e mostra a soma entre dois valores."""
        soma = v1 + v2 # cálculo da soma dos valores
        print(Fore.GREEN + Style.BRIGHT + f"\n10✅ A soma entre {v1} e {v2} é: {soma}") # exibição do resultado da soma

    somador(valor1, valor2) # chamada do procedimento somador com os valores digitados pelo usuário

    # Pergunta para nova simulação
    novo = (
        input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()
    )

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break
