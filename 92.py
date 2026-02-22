import os
import subprocess

"""Exercício 92
92) Crie uma lógica que leia um número inteiro e passe para um 
procedimento ParOuImpar() que vai verificar e mostrar na tela se o valor 
passado como  parâmetro é PAR ou ÍMPAR. 
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

    print(Fore.RED + Style.BRIGHT + "🔢 Simulador de Par ou Ímpar\n")

# Entrada de dados
    try:
        numero = int(input(Fore.CYAN + Style.BRIGHT + "Digite um número inteiro: "))
    except ValueError:
        print(Fore.RED + "❌ Entrada inválida! Por favor, digite um número inteiro.")
        input("Pressione Enter para tentar novamente...")
        continue

    # Procedimento para verificar se é par ou ímpar
    def ParOuImpar(n: int):
        if n % 2 == 0:
            print(Fore.GREEN + f"✅ O número {n} é PAR.")
        else:
            print(Fore.YELLOW + f"⚠️ O número {n} é ÍMPAR.")

    ParOuImpar(numero)

    # Pergunta para nova simulação
    novo = (
        input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()
    )

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break
