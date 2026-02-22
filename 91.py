import os
import subprocess

"""Exercício 91
91) Desenvolva um algoritmo que leia dois valores pelo teclado e passe esses  
valores para um procedimento Maior() que vai verificar qual deles é o maior e  
mostrá-lo no ecrã. Caso os dois valores sejam iguais, mostrar uma mensagem  
informando essa característica.
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
    print(Fore.CYAN + Style.BRIGHT + "🔢 Simulador de Maior Valor")

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

        # ============================================================
        #  PROCEDIMENTO PARA VERIFICAR O MAIOR VALOR
        # ============================================================
    def maior(v1: int, v2: int) -> None: # definição do procedimento maior com os parâmetros v1 e v2 do tipo inteiro
        """Função que verifica qual dos dois valores é o maior e mostra no ecrã."""
        if v1 > v2: # verifica se v1 é maior que v2
            print(Fore.GREEN + Style.BRIGHT + f"\n✅ O maior valor entre {v1} e {v2} é: {v1}")
        elif v2 > v1: # verifica se v2 é maior que v1
            print(Fore.GREEN + Style.BRIGHT + f"\n✅ O maior valor entre {v1} e {v2} é: {v2}")
        else: # caso os valores sejam iguais
            print(Fore.BLUE + Style.BRIGHT + f"\n⚠️ Os valores são iguais: {v1}")

    maior(valor1, valor2) # chamada do procedimento maior com os valores digitados pelo usuário

    # Pergunta para nova simulação
    novo = (
        input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()
    )

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break
