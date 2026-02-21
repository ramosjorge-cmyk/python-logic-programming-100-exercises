import os
import subprocess

"""Exercício 
73) Crie um programa que preencha automaticamente (usando lógica, não apenas atribuindo diretamente) um vetor numérico com 10 posições, conforme abaixo:
9 8 7 6 5 4 3 2 1 0
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
import time

while True:
    cls()

    # Preencher o vetor com valores decrescentes de 9 a 0
    vetor: list[int] = []
    for i in range(9, -1, -1):
        vetor.append(i)

    # Exibir o vetor
    print(Fore.GREEN + "📋 Elementos do vetor:")
    for num in vetor:
        print(Fore.YELLOW + f" {num}", end=" ", flush=True)
        time.sleep(0.25)

    print()  # Nova linha após exibir o vetor

    # Pergunta para nova simulação
    novo = (
        input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()
    )

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break
