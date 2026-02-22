import os
import subprocess

"""Exercício 76
76) Crie um programa que preencha automaticamente um vetor numérico com 7 
números gerados aleatoriamente pelo computador e depois mostre os valores  
gerados na tela.
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
import time

while True:
    cls()

    # Gerar vetor com 7 números aleatórios
    vetor = [random.randint(1, 100) for _ in range(7)]
    print(Fore.GREEN + Style.BRIGHT + "Vetor com 7 números aleatórios:")
    for num in vetor:
        print(Fore.YELLOW + f"{num}", end="  ", flush=True)
        time.sleep(0.50)  # animação na exibição

    print()
    time.sleep(2)# aguarda um momento antes de perguntar para nova simulação

    # Pergunta para nova simulação
    novo = (
        input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()
    )

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break
