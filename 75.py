import os
import subprocess

"""Exercício 75
75) Crie um programa que preencha automaticamente (usando lógica, não apenas  
atribuindo diretamente) um vetor numérico com 15 posições com os primeiros  
elementos da sequência de Fibonacci:  
1   1   2   3   5   8   13  21  34  55  89  144  233  377  610  987
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
    print(Fore.CYAN + Style.BRIGHT + "🔢 Sequência de Fibonacci - Vetor automático 🔢\n")

    #  criação do vetor usando lógica (fibonacci)
    # A sequência de Fibonacci começa com 1 e 1.
    # Cada termo seguinte é a soma dos dois anteriores.
    vetor: list[int] = []

    a, b = 1, 1  # primeiros dois termos da sequência

    # Gerar os primeiros 15 termos
    for i in range(15):
        vetor.append(a)      # adiciona o termo atual ao vetor
        a, b = b, a + b      # atualiza os termos (lógica de Fibonacci)

    #  exibição do vetor (animada)
    print(Fore.GREEN + Style.BRIGHT + "Primeiros 15 elementos da sequência:")

    # Exibir cada elemento com espaçamento e animação
    for num in vetor:
        print(Fore.YELLOW + f"{num}", end="  ", flush=True)
        time.sleep(0.50)  # animação na exibição

    print()  # linha final
    time.sleep(2)# aguarda um momento antes de perguntar para nova simulação
    
    # Pergunta para nova simulação
    novo = (
        input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()
    )

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break
