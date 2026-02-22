import os
from random import random
import subprocess

"""Exercício 88
88) Crie um programa que melhore o procedimento Gerador() da questão anterior  
para que mostre uma mensagem vário  
Ex: Ao chamar Gerador("Aprendendo Portugol", 4) aparece:  
+-------=======------+  
Aprendendo Portugol  
Aprendendo Portugol  
Aprendendo Portugol  
Aprendendo Portugol  
+-------=======------+
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
import random

while True:
    cls()

    # Entrada de dados
    print(Fore.CYAN + Style.BRIGHT + "🔢 Gerador de Mensagens")

    # ============================================================
    #  VALIDAÇÃO DA MENSAGEM
    # ============================================================
    # regras:
    # - não pode ser vazia
    # - não pode ser apenas espaços
    # ============================================================
    while True:
        mensagem = input(Fore.YELLOW + "📝 Digite a mensagem: ").strip()  # mensagem a ser apresentada

        if mensagem == "": # verifica se a mensagem é vazia ou apenas espaços
            print(Fore.RED + "❌ A mensagem não pode ser vazia. Tente novamente.")
            continue

        break  # mensagem válida

    # ============================================================
    #  VALIDAÇÃO DO NÚMERO DE REPETIÇÕES
    # ============================================================
    # regras:
    # - deve ser um número inteiro
    # - deve ser maior que zero
    # ============================================================
    while True:
        repeticoes_str = input(Fore.YELLOW + "🔁 Quantas repetições deseja? ").strip()  # quantidade de repetições

        if not repeticoes_str.isdigit():  # verifica se é um número inteiro positivo
            print(Fore.RED + "❌ Digite apenas números inteiros positivos.")
            continue

        repeticoes = int(repeticoes_str) # converte para inteiro

        if repeticoes <= 0: # verifica se é maior que zero
            print(Fore.RED + "❌ O número de repetições deve ser maior que zero.")
            continue

        break  # número de repetições válido

    # Gerador de mensagens
    print(Fore.GREEN + Style.BRIGHT + "+-------=======------+")
    for i in range(repeticoes):
        print(Fore.WHITE + Style.NORMAL + f"  {mensagem}")
    print(Fore.GREEN + Style.BRIGHT + "+-------=======------+")

    # Gerador de mensagens (versão extra com cores aleatórias)
    print(Fore.GREEN + Style.BRIGHT + "\n+-------=======------+")

    # lista de cores possíveis para cada repetição
    cores = [Fore.RED, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]

    for i in range(repeticoes):
        cor_aleatoria = random.choice(cores)  # escolhe uma cor aleatória
        print(cor_aleatoria + Style.NORMAL + f"  {mensagem}")  # imprime a mensagem com a cor escolhida

    print(Fore.GREEN + Style.BRIGHT + "+-------=======------+")

    # Pergunta para nova simulação
    novo = (
        input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()
    )

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break