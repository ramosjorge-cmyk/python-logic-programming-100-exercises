import os
import subprocess

"""Exercício 71
71) Faça um programa que preencha automaticamente um vetor numérico com 8 posições, conforme abaixo:
999 999 999 999 999 999 999 999
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
from typing import List

while True:
    cls()

    # Preencher o vetor com 999
    vetor = [999] * 8 # forma mais simples e pythonica

    # Exibir o vetor
    print(Fore.GREEN + Style.BRIGHT + "📦 Vetor preenchido automaticamente:")
    time.sleep(1) # Simula um processo de preenchimento

    vetor: List[int] = []  # vetor inicialmente vazio

    print(Fore.RED + "🛠️  Preenchendo vetor...\n")
    time.sleep(2) # Simula um processo de preenchimento
    
    # Preenchimento automático 
    vetor = [999] * 8

    # Exibir os elementos do vetor
    print(Fore.GREEN + "📋 Elementos do vetor:")

    # Exibir os elementos com animação
    for num in vetor:
        print(Fore.YELLOW + f"{num}", end=" ", flush=True)
        time.sleep(0.25)

    # Linha final
    print("\n")
    
        # Pergunta para nova simulação
    novo = (
        input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()
    )

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break
