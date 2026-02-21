import os
import subprocess

"""Exercício 61
61) Crie um programa que mostre na tela a seguinte contagem, usando a estrutura “faça enquanto”
0 3 6 9 12 15 18 21 24 27 30 Acabou!
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

    print(Fore.CYAN + Style.BRIGHT + "Contagem de 0 a 30 (de 3 em 3):\n")
    # Contagem usando estrutura "faça enquanto"
    
    numero = 0

    while numero <= 30:
        print(numero, end=" ", flush=True)
        time.sleep(0.3)   # atraso de 0.3 segundos entre cada número
        numero += 3

    print("\nAcabou!")

    # Pergunta para nova simulação
    novo = (
        input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()
    )

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break
