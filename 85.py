# ============================================
# [85] Funcionárias com salário > 5k / Female Employees Earning > 5k
# Tags: list, conditions
#
# Descrição (PT):
#   O programa lê nome, sexo e salário de 5 funcionários e exibe apenas as mulheres que ganham mais de 5 mil. Trabalha filtragem condicional.
#
# Description (EN):
#   The program reads name, gender, and salary of 5 employees and displays only the women earning more than 5k. It reinforces conditional filtering.
# ============================================

import os
import subprocess

"""Exercício 85
85) Faça um algoritmo que leia o nome, o sexo e o salário de 5 funcionários(as) e  
guarde esses dados em três vetores. No final, mostre uma listagem contendo  
apenas os dados das funcionárias mulheres que ganham mais de 5 mil euros.
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

    # título do exercício
    print(Fore.CYAN + Style.BRIGHT + "📊 Simulação de funcionários\n")

    # listas para armazenar os dados dos funcionários
    nomes: list[str] = []
    sexos: list[str] = []
    salarios: list[float] = []
    
    # coleta de dados dos funcionários
    for i in range(5):  # loop para ler os dados de 5 funcionários
        print(Fore.YELLOW + f"Funcionário {i + 1}:")  # exibe o número do funcionário atual

        # ============================================================
        #  VALIDAÇÃO DO NOME
        # ============================================================
        # regras:
        # - não pode ser vazio
        # - não pode ser só espaços
        # - deve ter pelo menos 2 caracteres
        # - deve conter apenas letras e espaços
        # ============================================================
        while True:
            nome = input("Nome: ").strip()

            if (
                nome == "" or 
                len(nome) < 2 or
                not all(c.isalpha() or c.isspace() for c in nome)
            ):
                print(Fore.RED + "❌ Nome inválido. Use apenas letras e espaços, com pelo menos 2 caracteres.")
                continue

            break  # nome válido

        # ============================================================
        #  VALIDAÇÃO DO SEXO
        # ============================================================
        # regras:
        # - deve ser M ou F
        # - não pode ser vazio
        # - aceita minúsculas, mas converte para maiúsculas
        # ============================================================
        while True:
            sexo = input("Sexo (M/F): ").strip().upper()

            if sexo not in ("M", "F"):
                print(Fore.RED + "❌ Sexo inválido. Digite apenas M ou F.")
                continue

            break  # sexo válido

        # ============================================================
        #  VALIDAÇÃO DO SALÁRIO
        # ============================================================
        # regras:
        # - não pode ser vazio
        # - deve ser número inteiro ou decimal
        # - deve ser positivo
        # - aceita vírgula ou ponto
        # ============================================================
        while True:
            salario_str = input("Salário (€): ").strip().replace(",", ".")

            if salario_str == "":
                print(Fore.RED + "❌ Salário não pode ser vazio.")
                continue

            try:
                salario = float(salario_str)
                if salario <= 0:
                    print(Fore.RED + "❌ Salário deve ser maior que zero.")
                    continue
                break
            except ValueError:
                print(Fore.RED + "❌ Salário inválido. Digite apenas números.")
                continue

        # guardar os dados validados
        nomes.append(nome)
        sexos.append(sexo)
        salarios.append(salario)

    # ============================================================
    #  EXIBIR FUNCIONÁRIAS MULHERES COM SALÁRIO > 5000€
    # ============================================================
    print(Fore.GREEN + Style.BRIGHT + "\n👩‍💼 Funcionárias mulheres com salário acima de 5000€:")

    encontrou = False # flag para verificar se encontrou alguma funcionária que atende aos critérios
    for i in range(5): # loop para verificar os dados dos funcionários
        if sexos[i] == "F" and salarios[i] > 5000: # verifica se é mulher e se o salário é maior que 5000
            print(Fore.LIGHTGREEN_EX + f"Nome: {nomes[i]}, Salário: {salarios[i]:.2f}€") # exibe o nome e salário formatado com 2 casas decimais
            encontrou = True # marca que encontrou pelo menos uma funcionária que atende aos critérios

    if not encontrou: # se não encontrou nenhuma funcionária que atende aos critérios, exibe uma mensagem
        print(Fore.RED + "🚫 Nenhuma funcionária atende aos critérios.") # imforma nenhuma funcionária encontrada com os critérios definidos

    ###########################################################################
    # EXIBIR LISTA COMPLETA DE FUNCIONÁRIOS PARA REFERÊNCIA - OPÇÃO EXTRA
    ###########################################################################
    # exibe a lista completa de funcionários para referência
    print(Fore.CYAN + Style.BRIGHT + "\nFuncionários registados (OPÇÂO EXTRA):\n") # exibe o título da lista de funcionários registados
    print(Fore.CYAN + Style.BRIGHT + "[nomes, sexos, salários]:") # exibe o título da lista de dados dos funcionários
    print(Fore.CYAN + Style.BRIGHT + str(list(zip(nomes, sexos, salarios)))) # exibe a lista de tuplas com os dados dos funcionários

    print()
    # outra forma de exibir os dados dos funcionários usando um loop para formatar melhor a saída
    dados = list(zip(nomes, sexos, salarios))  # cria lista de tuplas
    print(Fore.CYAN + Style.BRIGHT + "[nomes, sexos, salários]:") # exibe o título da lista de dados dos funcionários
    for nome, sexo, salario in dados:
        print(
        "[" +
        Fore.YELLOW + nome + Fore.RESET + ", " +
        Fore.MAGENTA + sexo + Fore.RESET + ", " +
        Fore.GREEN + f"{salario:.2f}€" + Fore.RESET +
        "]"
    )

    # pergunta para nova simulação
    novo = input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break