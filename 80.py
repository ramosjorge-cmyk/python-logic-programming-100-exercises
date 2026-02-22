import os
import subprocess

"""Exercício 80
80) Faça um algoritmo que preencha um vetor de 30 posições com números entre 1 e  
15 sorteados pelo computador. Depois disso, peça para o usuário digitar um  
número (chave) e seu programa deve mostrar em que posições essa chave foi  
encontrada. Mostre também quantas vezes a chave foi sorteada.  
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
import random
import time

while True:
    cls()

    numeros = [random.randint(1, 15) for _ in range(30)] # gerar vetor de 30 números entre 1 e 15
    print(Fore.YELLOW + "Números sorteados:") # exibir os números sorteados
    for num in numeros:
        print(Fore.CYAN + str(num), end=" ") # exibir cada número com cor diferente
        time.sleep(0.50) # pausa para melhor visualização
    
    chave = int(input(Fore.MAGENTA + "\n\nDigite um número (chave) para procurar: ")) # solicitar a chave ao usuário
    posicoes = [i+1 for i, num in enumerate(numeros) if num == chave] # encontrar as posições da chave no vetor
    if posicoes:
        print(Fore.GREEN + f"\nA chave {chave} foi encontrada nas posições: {', '.join(map(str, posicoes))}") # exibir as posições onde a chave foi encontrada
        print(Fore.GREEN + f"A chave {chave} foi sorteada {len(posicoes)} vezes.") # exibir quantas vezes a chave foi sorteada
    else:
        print(Fore.RED + f"\nA chave {chave} não foi encontrada no vetor.") # exibir mensagem caso a chave não seja encontrada

    # Pergunta para nova simulação
    novo = (
        input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()
    )

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break
