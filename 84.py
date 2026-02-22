import os
import subprocess

"""Exercício 84
84) Crie um programa que leia o nome e a idade de 9 pessoas 
e guarde esses valores em dois vetores, em posições relacionadas. 
No final, mostre uma listagem contendo apenas os dados das pessoas 
menores de idade. 
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
from typing import List

while True:
    cls()

    print(  # mensagem de introdução
        Fore.CYAN + Style.BRIGHT + "📋 Simulação de Idades\n"
        + Fore.YELLOW + "Digite o nome e a idade de 9 pessoas.\n"
        + Fore.GREEN + "Vamos descobrir quem são os menores de idade! 🚸\n"
        + Fore.WHITE + "Observação: A idade máxima para ser considerado menor de idade é 17 anos.\n"
        + Fore.MAGENTA + "---------------------------------------------"
    )

    nomes: List[str] = []  # vetor para armazenar os nomes
    idades: List[int] = []  # vetor para armazenar as idades

    for i in range(9):  # loop para coletar os dados de 9 pessoas

        # ============================================================
        #  VALIDAÇÃO DO NOME
        # ============================================================
        # Regras:
        # - não pode ser vazio
        # - deve ter pelo menos 2 caracteres
        # - deve conter apenas letras (com ou sem espaços)
        # - não pode conter números
        # ============================================================
        while True:  # loop para garantir que o nome seja válido
            nome = input(Fore.YELLOW + f"👤 {i + 1}ª pessoa - Nome: ").strip()

            if (
                nome == "" or                                       # nome vazio
                len(nome) < 2 or                                    # nome muito curto
                any(c.isdigit() for c in nome) or                   # contém números
                not all(c.isalpha() or c.isspace() for c in nome)   # contém símbolos inválidos
            ):
                print(Fore.RED + "⚠️  Nome inválido. Use apenas letras e espaços, com pelo menos 2 caracteres.")
                continue  # repete o pedido do mesmo nome

            break  # nome válido → sai do loop

        # ============================================================
        #  VALIDAÇÃO DA IDADE
        # ============================================================
        # Regras:
        # - deve ter pelo menos 1 caractere e no máximo 3 caracteres (para idades de 0 a 120)
        # - deve conter apenas números inteiros
        # - deve ser um número positivo
        # - não pode ser maior que 120 (limite de idade humana)
        # ============================================================
        while True: # loop para garantir que a idade seja válida
            idade_str = input(Fore.GREEN + f"🎂 {i + 1}ª pessoa - Idade: ").strip() # pede a idade

            # verificar número de caracteres
            if len(idade_str) == 0 or len(idade_str) > 3: # idade vazia ou muito longa
                print(Fore.RED + "❌ Idade deve ter entre 1 e 3 dígitos.")
                continue

            # verificar se contém apenas números
            if not idade_str.isdigit(): # idade contém caracteres não numéricos
                print(Fore.RED + "❌ Idade deve conter apenas números inteiros.")
                continue

            idade = int(idade_str)

            # verificar se é positiva
            if idade < 0: # idade não pode ser negativa
                print(Fore.RED + "❌ Idade não pode ser negativa.")
                continue

            # verificar limite máximo
            if idade > 120: # idade é muito alta e não é realista
                print(Fore.RED + "❌ Idade muito alta (+120). Tente novamente.")
                continue

            break  # idade válida → sai do loop

        # guardar os dados validados
        nomes.append(nome)
        idades.append(idade)

    # ============================================================
    #  EXIBIR APENAS MENORES DE IDADE
    # ============================================================
    print(
        Fore.MAGENTA + "\n🔍 Pessoas menores de idade:"
        + Fore.YELLOW + "\n---------------------------------------------"
    )

    menores = False  # flag para saber se existe algum menor

    for nome, idade in zip(nomes, idades): # percorre os vetores de nomes e idades simultaneamente
        if idade < 17: # verifica se a pessoa é menor de idade (idade < 17)
            print(Fore.CYAN + f"👤 {nome} - {idade} anos") #  mostra os nomes e idades dos menores
            menores = True

    if not menores:
        print(
            Fore.RED + "🚫 Nenhuma pessoa é menor de idade." # mensagem de erro se não houver menores
            + Fore.YELLOW + "\n---------------------------------------------"
        )

    # Pergunta para nova simulação
    novo = input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break