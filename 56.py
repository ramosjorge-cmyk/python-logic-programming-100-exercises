import os
import subprocess

"""Exercício 56
56) Crie um programa que leia vários números pelo teclado e mostre no final o somatório entre eles.
Obs: O programa será interrompido quando o número 1111 for digitado
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

# Variáveis de controlo
nr = 0
soma = 0

# ============================================================
#  LOOP PRINCIPAL — lê números até o utilizador digitar 1111
# ============================================================
while True:
    cls()

    print(Fore.CYAN + Style.BRIGHT + "\n=== 🧮 Somatório de Números ===\n")

    try:
        nr = int(input(Fore.YELLOW + "Digite um número (1111 para encerrar): "))

        # Condição de saída
        if nr == 1111:
            break

        # Acumula o valor digitado
        soma += nr

    except ValueError:
        print(Fore.RED + "❌ Entrada inválida. Digite um número inteiro.")
        input(Fore.MAGENTA + "\nPressione ENTER para continuar...")
        continue

# ============================================================
#  RESULTADO FINAL
# ============================================================
cls()
print(Fore.GREEN + Style.BRIGHT + "\n📌 Resultado Final:")
print(Fore.CYAN + f"\nO somatório dos números digitados é: {soma}\n")

print(Fore.CYAN + Style.BRIGHT + "👋 Obrigado por utilizar o programa! Até a próxima!\n")