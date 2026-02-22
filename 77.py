import os
import subprocess

"""Exercício 77
77) Faça um programa que leia 7 nomes de pessoas e guarde-os em um vetor. No  
final, mostre uma listagem com todos os nomes informados, na ordem inversa  
daquela em que eles foram informados. 
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

    print(Fore.CYAN + Style.BRIGHT + "📋 Simulador de Nomes - Ordem Inversa\n")
    # Coleta de nomes
    nomes: list[str] = []
    
    while len(nomes) < 7:  # loop para garantir que sejam coletados exatamente 7 nomes
        i = len(nomes) + 1  # contador para exibir a posição do nome sendo solicitado
        nome = input(Fore.YELLOW + f"Digite o nome da {i}ª pessoa: ").strip()

        # ============================================================
        #  VALIDAÇÃO DO NOME
        # ============================================================
        # Regras:
        # - não pode ser vazio
        # - deve ter pelo menos 2 caracteres
        # - deve conter apenas letras (com ou sem espaços)
        # - não pode conter números
        # ============================================================
        if (
            nome == "" or                                       # nome vazio
            len(nome) < 2 or                                    # nome muito curto
            any(c.isdigit() for c in nome) or                   # contém números
            not all(c.isalpha() or                              # contém símbolos inválidos
            c.isspace() for c in nome)                          # somente letras e espaços
        ):
            print(Fore.RED + "⚠️  Nome inválido. Use apenas letras e espaços, com pelo menos 2 caracteres.")
            continue  # volta ao início do loop

        nomes.append(nome)  # nome válido → adiciona ao vetor

    # Exibição dos nomes na ordem inversa
    print(Fore.GREEN + "\n🔄 Nomes na ordem inversa:")
    for nome in reversed(nomes):
        print(Fore.GREEN + f"  - {nome}")
        time.sleep(0.50)  # animação na exibição

    print()
    time.sleep(2)# aguarda um momento antes de perguntar para nova simulação

    # Pergunta para nova simulação
    novo = (
        input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()
    )

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break
