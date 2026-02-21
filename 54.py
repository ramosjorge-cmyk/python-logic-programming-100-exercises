import os
import subprocess

"""Exercício 54
54) Desenvolva um aplicativo que leia o peso e a altura de 7 pessoas, mostrando no final:
a) Qual foi a média de altura do grupo
b) Quantas pessoas pesam mais de 90Kg
c) Quantas pessoas que pesam menos de 50Kg tem menos de 1.60m 
d) Quantas pessoas que medem mais de 1.90m pesam mais de 100Kg.
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

    print (Fore.CYAN + Style.BRIGHT + "📊 Simulação de Altura e Peso")

    total_altura = 0
    mais_90kg = 0
    menos_50kg_menos_160m = 0
    mais_190m_mais_100kg = 0

    for i in range(7):
        print(Fore.YELLOW + Style.BRIGHT + f"\n{i + 1}ª pessoa:")
        while True:
            try:
                altura = float(input(Fore.CYAN + "Digite a altura (em metros): "))
                if altura <= 0:
                    print(Fore.RED + "A altura deve ser positiva.")
                    continue
                break
            except ValueError:
                print(Fore.RED + "Altura inválida. Por favor, digite um número.")

        while True:
            try:
                peso = float(input(Fore.CYAN + "Digite o peso (em kg): "))
                if peso <= 0:
                    print(Fore.RED + "O peso deve ser positivo.")
                    continue
                break
            except ValueError:
                print(Fore.RED + "Peso inválido. Por favor, digite um número.")

        total_altura += altura

        if peso > 90:
            mais_90kg += 1

        if peso < 50 and altura < 1.60:
            menos_50kg_menos_160m += 1

        if altura > 1.90 and peso > 100:
            mais_190m_mais_100kg += 1

    media_altura = total_altura / 7

    print(Fore.GREEN + Style.BRIGHT + "\nResultados:")
    print(Fore.GREEN + f"Média de altura do grupo: {media_altura:.2f} metros")
    print(Fore.GREEN + f"Pessoas que pesam mais de 90Kg: {mais_90kg}")
    print(Fore.GREEN + f"Pessoas que pesam menos de 50Kg e medem menos de 1.6m: {menos_50kg_menos_160m}")
    print(Fore.GREEN + f"Pessoas que medem mais de 1.9m e pesam mais de 100Kg: {mais_190m_mais_100kg}")

    novo = (
        input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()
    )

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break
