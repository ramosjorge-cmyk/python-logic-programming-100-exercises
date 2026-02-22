# ============================================
# [83] Vetor aleatório e ordenação / Random Vector and Sorting
# Tags: list, sort
#
# Descrição (PT):
#   O programa gera 20 números aleatórios, exibe a lista original e depois a lista ordenada. Trabalha ordenação crescente.
#
# Description (EN):
#   The program generates 20 random numbers, displays the original list, and then the sorted list. It reinforces sorting and array manipulation.
# ============================================

import os
import subprocess

"""Exercício 83
83) [DESAFIO] Crie uma lógica que preencha um vetor de 20 posições 
com números aleatórios (entre 0 e 99) gerados pelo computador. 
Logo em seguida, mostre os números gerados e depois coloque o vetor 
em ordem crescente, mostrando no final os valores ordenados.
"""

# limpar ecrã (windows / linux / macos)
def cls():
    """limpa o terminal de forma compatível com vários sistemas operativos."""
    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run(comando, shell=True)

from colorama import Fore, Style, init
init(autoreset=True)
import random
import time

while True:
    cls()

    print(Fore.YELLOW + Style.BRIGHT + "Gerador de vetor de números aleatórios...\n")

    # gerar vetor com 20 números aleatórios entre 0 e 99
    vetor = [random.randint(0, 99) for _ in range(20)]

    # exibir o vetor gerado na mesma linha, com colchetes e vírgulas
    print(Fore.CYAN + Style.BRIGHT + "Vetor gerado: [", end="", flush=True)

    # cada número é mostrado com um pequeno atraso para criar um efeito visual
    for i, num in enumerate(vetor): # enumerate para obter o índice e o número
        print(Fore.CYAN + f"{num}", end="", flush=True) # exibe o número atual sem pular linha e força a atualização imediata
        if i < len(vetor) - 1: # se não for o último número, adiciona uma vírgula
            print(Fore.CYAN + ", ", end="", flush=True) # exibe a vírgula sem pular linha e força a atualização imediata
        time.sleep(0.40) # pausa de 0.40 segundos para melhor visualização

    print(Fore.CYAN + "]\n")  # fecha o vetor e salta linha

    # ordenar o vetor em ordem crescente
    vetor.sort() 

    # exibir o vetor ordenado com o mesmo estilo do vetor gerado
    print(Fore.GREEN + Style.BRIGHT + "Vetor ordenado: [", end="", flush=True) # exibe o início do vetor ordenado sem pular linha e força a atualização imediata

    for i, num in enumerate(vetor): # enumerate para obter o índice e o número
        print(Fore.GREEN + f"{num}", end="", flush=True) # exibe o número atual sem pular linha e força a atualização imediata
        if i < len(vetor) - 1: # se não for o último número, adiciona uma vírgula
            print(Fore.GREEN + ", ", end="", flush=True) # exibe a vírgula sem pular linha e força a atualização imediata
        time.sleep(0.40) # pausa de 0.40 segundos para melhor visualização

    print(Fore.GREEN + "]\n")  # fecha o vetor e salta linha

    # perguntar ao utilizador se deseja repetir a simulação
    novo = input(Fore.MAGENTA + "🔁 deseja simular novamente? (s/n): ").strip().lower()

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 obrigado por simular! até a próxima!\n")
        break