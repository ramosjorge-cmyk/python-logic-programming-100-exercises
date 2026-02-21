import os
import subprocess

"""Exercício 72
72) Crie um programa que preencha automaticamente (usando lógica, não apenas atribuindo diretamente) um vetor numérico com 10 posições, conforme abaixo:
5 10 15 20 25 30 35 40 45 50
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

    print(Fore.CYAN + Style.BRIGHT + "🔢 Simulador de vetor numérico\n")

    # Preencher o vetor com valores sequenciais
    vetor = []

    # Preenchimento automático: começa em 5 
    # e soma 5 a cada passo
    for i in range(1, 11):
        vetor.append(i * 5) # gera 5, 10, 15, 20...

    # Exibir o vetor
    print(Fore.GREEN + "📋 Elementos do vetor:")
    vetor: list[int] = vetor
    for num in vetor:
        print(Fore.YELLOW + f"{num}", end=" ", flush=True)
        time.sleep(0.50)
    
    print("\n")

    # Pergunta para nova simulação
    novo = (
        input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()
    )

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break
