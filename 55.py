import os
import subprocess

"""Exercício 55
55) [DESAFIO] Vamos melhorar o jogo que fizemos no exercício 32.
A partir de agora, o computador vai sortear um número entre 1 e 10 
e o jogador vai ter 4 tentativas para tentar acertar.
"""

# ============================================================
#  LIMPAR ECRÃ (Windows / Linux / macOS)
# ============================================================
def cls():
    """Limpa o terminal de forma compatível com vários sistemas operativos."""
    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run(comando, shell=True)

import random
from colorama import init, Fore, Style

# Inicializar o Colorama
init(autoreset=True)

# ============================================================
#  LOOP PRINCIPAL DO JOGO
# ============================================================
while True:
    cls()

    # Imprimir mensagem de boas-vindas
    print(Style.BRIGHT + Fore.CYAN + "\n=== 🎲 Bem-vindo ao jogo de adivinhar os números! ===\n")

    # Gerar um número aleatório entre 1 e 10
    sorteado = random.randint(1, 10)

    # Contador de tentativas
    tentativas = 1

    # ============================================================
    #  PRIMEIRA TENTATIVA (com validação)
    # ============================================================
    while True:
        try:
            nr = int(input(Fore.YELLOW + "🎯 Tente adivinhar o número sorteado (entre 1 e 10), tem 4 tentativas: "))
            if 1 <= nr <= 10:
                break
            print(Fore.RED + "❌ Número inválido. Por favor, escolha um número entre 1 e 10.")
        except ValueError:
            print(Fore.RED + "❌ Entrada inválida. Digite um número inteiro.")

    # ============================================================
    #  CICLO DAS TENTATIVAS (até acertar ou esgotar as 4 tentativas)
    # ============================================================
    while nr != sorteado and tentativas < 4:
        print(Fore.RED + Style.BRIGHT + f"❌ Errado! Você tem {4 - tentativas} tentativas restantes.")

        tentativas += 1

        # Nova tentativa com validação
        while True:
            try:
                nr = int(input(Fore.YELLOW + "🎯 Tente novamente: "))
                if 1 <= nr <= 10:
                    break
                print(Fore.RED + "❌ Número inválido. Digite entre 1 e 10.")
            except ValueError:
                print(Fore.RED + "❌ Entrada inválida. Digite um número inteiro.")

    # ============================================================
    #  RESULTADO FINAL
    # ============================================================
    if nr == sorteado:
        # Informar o jogador sobre o acerto e parabenizá-lo
        print(Fore.GREEN + Style.BRIGHT + "\n🎉 Parabéns! Você acertou no número sorteado!")
    else:
        # Informar o jogador sobre o número sorteado e incentivá-lo a tentar novamente
        print(Fore.RED + Style.BRIGHT + f"\n😢 Que pena! O número sorteado era {sorteado}. Tente novamente!")

    # ============================================================
    #  PERGUNTA PARA NOVO JOGO
    # ============================================================
    novo = input(Fore.MAGENTA + "\n🔁 Deseja jogar novamente? (s/n): ").strip().lower()

    # Limpa o ecrã entre jogos para melhorar a experiência do jogador
    cls()

    if novo != "s":
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por jogar! Até a próxima!\n")
        break