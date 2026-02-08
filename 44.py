import os
import subprocess

"""Exercício 44
44) Crie um algoritmo que leia o valor inicial da contagem, o valor final e o
incremento, mostrando em seguida todos os valores no intervalo: Ex: Digite o
primeiro Valor: 3
Digite o último Valor: 10
Digite o incremento: 2
Contagem: 3 5 7 9 Acabou!
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
    print (Fore.CYAN + Style.BRIGHT + "\n🔢 Simulador de Contagem Personalizada\n")

    ninicio = int(input(Fore.YELLOW + "✏️  Digite o valor inicial da contagem: "))
    nfim = int(input(Fore.YELLOW + "✏️  Digite o valor final da contagem: "))
    incremento = int(input(Fore.YELLOW + "✏️  Digite o incremento: "))

    print(Fore.GREEN + Style.BRIGHT + "\nContagem:", end=" ")
    for i in range(ninicio, nfim + 1, incremento):
        print(i, end=" ", flush=True)
        time.sleep(0.5)
    print(Fore.GREEN + Style.BRIGHT + "\nAcabou!")

    # Pergunta para nova simulação
    novo = (
        input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()
    )

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break