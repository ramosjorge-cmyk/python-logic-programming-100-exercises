import os
import subprocess

"""Exercício 32
32) [DESAFIO] Crie um jogo onde o computador vai sortear um número entre 1 e 5 o
jogador vai tentar descobrir qual foi o valor sorteado.
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



# Loop principal do jogo
while True:
# Imprimir mensagem de boas-vindas
    print(Style.BRIGHT + Fore.CYAN + "\n=== 🎲 Bem-vindo ao jogo de advinhar 0s números! ===\n")    
    
    # Solicitar ao jogador que insira um número entre 1 e 5
    nr = int(input(Fore.YELLOW + "🎯 Tente adivinhar o número sorteado (entre 1 e 5): "))
    
    # Verificar se a entrada do jogador é válida
    if nr < 1 or nr > 5:
        print(Fore.RED + Style.BRIGHT + "❌ Número inválido. Por favor, escolha um número entre 1 e 5.")
        continue
    
    # Gerar um número aleatório entre 1 e 5
    sorteado = random.randint(1, 5)
    
    # Verificar se o jogador acertou o número sorteado
    if nr == sorteado:
        
        # Informar o jogador sobre o acerto e parabenizá-lo
        print(Fore.GREEN + Style.BRIGHT + "\n🎉 Parabéns! Você acertou o número sorteado!")
    else:
        
        # Informar o jogador sobre o número sorteado e incentivá-lo a tentar novamente
        print(Fore.RED + Style.BRIGHT + f"\n😢 Que pena! O número sorteado era {sorteado}. Tente novamente!")
        
    # Pergunta para novo jogo
    novo = input(Fore.MAGENTA + "\n🔁 Deseja jogar novamente? (s/n): ").strip().lower()
    
    # Limpa o ecrã entre jogos para melhorar a experiência do jogador
    cls()
            
    if novo != "s":
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por jogar! Até a próxima!\n")
        break
