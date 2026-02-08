import os
import subprocess
from time import time

"""Exercício 42
42) Faça um algoritmo que pergunte ao usuário um número inteiro e positivo
qualquer e mostre uma contagem até esse valor:
Ex: Digite um valor: 35
Contagem: 1 2 3 4 5 6 7 ... 33 34 35 Acabou!
"""

# ============================================================
#  LIMPAR ECRÃ (Windows / Linux / macOS)
# ============================================================
def cls():
    """Limpa o terminal de forma compatível com vários sistemas operativos."""
    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run(comando, shell=True)

import time
from colorama import Fore, Style, init
init(autoreset=True)

while True:
    cls()
    print(Fore.CYAN + Style.BRIGHT + "🔢 Contagem até ao valor indicado\n")

    # Pedir número válido
    while True:
        try:
            valor = int(input(Fore.YELLOW + "✏️ Digite um número inteiro e positivo: "))
            if valor <= 0:
                print(Fore.RED + "❌ O número deve ser inteiro e positivo.")
            else:
                break
        except ValueError:
            print(Fore.RED + "❌ Valor inválido. Digite um número inteiro.")

    # Contagem
    print(Fore.MAGENTA + Style.BRIGHT + "\nContagem:", end=" ")
    for i in range(1, valor + 1):
        print(Fore.GREEN + str(i), end=" ", flush=True)
        time.sleep(0.5)
    print(Fore.YELLOW + Style.BRIGHT + "\nAcabou!")

    # Pergunta para nova simulação
    novo = (
        input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()
    )

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break
