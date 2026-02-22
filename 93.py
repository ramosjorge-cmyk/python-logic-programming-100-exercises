# ============================================
# [93] Procedimento Contador / Counter Procedure
# Tags: procedure, loop
#
# Descrição (PT):
#   O programa recebe início, fim e incremento e exibe a contagem correspondente. Trabalha parametrização de laços.
#
# Description (EN):
#   The program receives start, end, and step values and displays the corresponding count. It reinforces loop parameterization.
# ============================================

import os
import subprocess

"""Exercício 93
93) Faça um programa que tenha um procedimento chamado Contador() que recebe  
três valores como parâmetro: o início, o fim e o incremento de uma contagem. 
O programa principal deve solicitar a digitação desses valores e passá-los ao  
procedimento, que vai mostrar a contagem na tela.  
Ex: Para os valores de início (4), fim (20) e incremento(3) teremos 
Contador(4, 20, 3) vai mostrar na tela 4 >> 7 >> 10 >> 13 >> 16 >> 19 >> 
FIM
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

    print(Fore.CYAN + Style.BRIGHT + "🔢 Contador Personalizado 🔢\n")
    # Solicitar os valores de início, fim e incremento
    
    try: # Verificar se os valores são inteiros
        inicio = int(input(Fore.YELLOW + "🚀 Digite o valor de início: ")) 
        fim = int(input(Fore.YELLOW + "🏁 Digite o valor de fim: ")) 
        incremento = int(input(Fore.YELLOW + "➕ Digite o valor de incremento: "))
    except ValueError: # Se o utilizador digitar algo que não seja um número inteiro, exibir mensagem de erro
        print(Fore.RED + "❌ Por favor, digite apenas números inteiros.")
        input(Fore.MAGENTA + "Pressione Enter para tentar novamente...")
        continue

    # Verificar se o incremento é válido
    if incremento <= 0: # O incremento deve ser um número positivo
        print(Fore.RED + "❌ O incremento deve ser um número positivo.")
        input(Fore.MAGENTA + "Pressione Enter para tentar novamente...")
        continue

    # Contador
    print(Fore.GREEN + Style.BRIGHT + "\nContagem:") # Exibe a contagem personalizada com os valores fornecidos
    for i in range(inicio, fim + 1, incremento): # O fim é incrementado em 1 para incluir o valor final na contagem, caso seja alcançado
        print(Fore.BLUE + f"{i} >> ", end="") # O end="" é usado para evitar a quebra de linha após cada número, permitindo que a contagem seja exibida na mesma linha
    print(Fore.GREEN + "FIM") # Após a contagem, exibe "FIM" para indicar o término da contagem

    # Pergunta para nova simulação
    novo = (
        input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()
    )

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break
