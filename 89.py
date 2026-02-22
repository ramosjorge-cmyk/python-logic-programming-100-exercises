import os
import subprocess

"""Exercício 89
89) Crie um programa que melhore o procedimento Gerador() da questão anterior  
para que o programador possa escolher uma entre três bordas:  
+-------=======------+ Borda 1  
~~~~~~~~:::::::~~~~~~~ Borda 2  
<<<<<<<<------->>>>>>> Borda 3 

[mensagem; número de repetições; tipo de borda]

Ex: Uma chamada válida seria Gerador("Portugol Studio", 3, 2)  
~~~~~~~~:::::::~~~~~~~  
Portugol Studio  
Portugol Studio  
Portugol Studio  
~~~~~~~~:::::::~~~~~~~
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

# Entrada de dados
    print(Fore.CYAN + Style.BRIGHT + "🔹 Gerador de Mensagens")

    # ============================================================
    #  VALIDAÇÃO DA MENSAGEM
    # ============================================================
    while True:
        mensagem = input(Fore.YELLOW + "📝 Digite a mensagem: ").strip()  # mensagem a ser apresentada

        if mensagem == "": # verifica se a mensagem é vazia ou apenas espaços
            print(Fore.RED + "❌ A mensagem não pode ser vazia. Tente novamente.")
            continue

        break  # mensagem válida

    # ============================================================
    #  VALIDAÇÃO DO NÚMERO DE REPETIÇÕES
    # ============================================================
    while True:
        repeticoes_str = input(Fore.YELLOW + "🔁 Quantas repetições deseja? ").strip()  # quantidade de repetições

        if not repeticoes_str.isdigit():  # verifica se é um número inteiro positivo
            print(Fore.RED + "❌ Digite apenas números inteiros positivos.")
            continue

        repeticoes = int(repeticoes_str) # converte para inteiro

        if repeticoes <= 0: # verifica se é maior que zero
            print(Fore.RED + "❌ O número de repetições deve ser maior que zero.")
            continue

        break  # número de repetições válido

    # ============================================================
    #  VALIDAÇÃO DO TIPO DE BORDA
    # ============================================================
    while True:
        borda = input(Fore.YELLOW + "🔢 Escolha o tipo de borda (1, 2 ou 3): ").strip()  # tipo de borda

        if borda not in ["1", "2", "3"]:  # verifica se é um tipo de borda válido
            print(Fore.RED + "❌ Escolha uma borda válida (1, 2 ou 3).")
            continue

        break  # tipo de borda válido

    bordas = { # dicionário para mapear o número da borda para a string correspondente
        "1": "+-------=======------+",
        "2": "~~~~~~~~:::::::~~~~~~~",
        "3": "<<<<<<------->>>>>>>"
    }
    
    print ()  # linha em branco para separar a entrada da saída
    
    print(Fore.GREEN + Style.BRIGHT + bordas[borda]) # imprime a borda escolhida
    for i in range(repeticoes): # imprime a mensagem o número de vezes escolhido
        print(Fore.WHITE + Style.NORMAL + f"  {mensagem}") # imprime a mensagem com um pouco de indentação para ficar mais bonito
    print(Fore.GREEN + Style.BRIGHT + bordas[borda]) # imprime a borda novamente para fechar o bloco de mensagens

    # Pergunta para nova simulação
    novo = (
        input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()
    )

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break
