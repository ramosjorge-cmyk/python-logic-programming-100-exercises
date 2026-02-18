import os
import subprocess

"""Exercício 47
47) Desenvolva um aplicativo que mostre na tela o resultado da expressão
500 + 450 + 400 + 350 + 300 + ... + 50 + 0
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
    print(Fore.CYAN + Style.BRIGHT + "🔢 Simulador de Soma de Expressão 🔢")
    soma = sum(range(500, -1, -50))  # Começa em 500, vai até 0 (inclusive), com passo de -50
    print(Fore.GREEN + Style.BRIGHT + f"Resultado da soma da expressão: {soma}")
    
    # Pergunta para nova simulação
    novo = (
        input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()
    )

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break
