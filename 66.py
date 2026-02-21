import os
import subprocess

"""Exercício 66
66) Escreva um programa que leia um número qualquer e 
mostre a tabuada desse número, usando a estrutura “para”.
Ex: Digite um valor: 5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15 ...
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

    print(Fore.CYAN + Style.BRIGHT + "🔢 Simulador de Tabuada\n")
    
    # Solicita ao utilizador um número para mostrar a tabuada
    try:
        num = int(input(Fore.YELLOW + "Digite um número para ver sua tabuada: "))
        print(Fore.GREEN + f"\nTabuada do {num}:\n")
        for i in range(1, 11): # Tabuada de 1 a 10
            print(Fore.WHITE + f"{num} x {i} = {num * i}")
    except ValueError: # Trata a exceção caso o utilizador insira um valor que não seja um número inteiro
        print(Fore.RED + "❌ Por favor, insira um número válido.")


    # Pergunta para nova simulação
    novo = (
        input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()
    )

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break