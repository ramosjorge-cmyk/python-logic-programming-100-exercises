# ============================================
# [74] Vetor alternado 5 e 3 / Alternating Vector 5 and 3
# Tags: list, pattern
#
# Descrição (PT):
#   O exercício preenche um vetor alternando 5 e 3. Trabalha padrões repetitivos.
#
# Description (EN):
#   The exercise fills an array alternating between 5 and 3. It practices repetitive patterns.
# ============================================

import os
import subprocess

"""Exercício 74
74) Crie um programa que preencha automaticamente (usando lógica, não apenas atribuindo diretamente) um vetor numérico com 10 posições, conforme abaixo:
5 3 5 3 5 3 5 3 5 3
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
    print(Fore.CYAN + Style.BRIGHT + "🔢 Simulador de Vetor Numérico 🔢\n")

    # Criar o vetor usando lógica
    # O exercício pede um padrão alternado: 5, 3, 5, 3, ...
    # Em Python, podemos usar o índice para decidir qual valor colocar:
    # - índices pares → 5
    # - índices ímpares → 3

    vetor: list[int] = []
    for i in range(10):
        if i % 2 == 0:
            vetor.append(5)  # Posições pares recebem 5
        else:
            vetor.append(3)  # Posições ímpares recebem 3

    # Exibir o vetor
    print(Fore.GREEN + Style.BRIGHT + "Vetor gerado:")

    # Aqui mostra cada elemento com animação
    # e com um espaçamento entre eles para ficar mais legível
    for num in vetor:
        print(Fore.YELLOW + f"{num}", end="   ", flush=True)
        time.sleep(1) # Pausa de 1 segundo entre cada número

        

    print()  # Linha em branco final
    time.sleep(2)  # Pausa para o usuário ver o resultado
    
    # Pergunta para nova simulação
    novo = (
        input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()
    )

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break
