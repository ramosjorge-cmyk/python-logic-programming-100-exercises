# ============================================
# [53] Estatísticas de idade e sexo / Age and Gender Statistics
# Tags: input, loop, conditions
#
# Descrição (PT):
#   O programa lê idade e sexo de 5 pessoas e calcula estatísticas como número de homens, número de mulheres e médias. Trabalha agrupamento condicional.
#
# Description (EN):
#   The program reads age and gender of 5 people and computes statistics such as number of men, number of women, and averages. It practices conditional grouping.
# ============================================

import os
import subprocess

"""Exercício 53
53) Faça um programa que leia a idade e o sexo de 5 pessoas, mostrando no final: 
a) Quantos homens foram cadastrados
b) Quantas mulheres foram cadastradas
c) A média de idade do grupo
d) A média de idade dos homens
e) Quantas mulheres tem mais de 20 anos
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

    print(Fore.CYAN + Style.BRIGHT + "📊 Simulação de Dados de Pessoas")

    idade_total = 0
    homens = 0
    mulheres = 0
    idade_homens = 0
    mulheres_mais_20 = 0

    for i in range(5):
        print(Fore.YELLOW + Style.BRIGHT + f"\n{i + 1}º pessoa:")
        while True:        
            try:
                idade = int(input(Fore.CYAN + "Digite a idade: "))
                if idade < 0:
                    print(Fore.RED + "A idade não pode ser negativa.")
                    continue
                break
            except ValueError:
                print(Fore.RED + "Idade inválida. Por favor, digite um número inteiro.")

        sexo = input(Fore.CYAN + "Digite o sexo (M/F): ").strip().upper()
        idade_total += idade

        if sexo == "M":
            homens += 1
            idade_homens += idade
        elif sexo == "F":
            mulheres += 1
            if idade > 20:
                mulheres_mais_20 += 1

# Cálculo das médias
    media_idade = idade_total / 5
    media_idade_homens = idade_homens / homens if homens > 0 else 0

# Exibição dos resultados
    print(Fore.GREEN + Style.BRIGHT + "\nResultados:")
    print(Fore.GREEN + f"Total de homens registados: {homens}")
    print(Fore.GREEN + f"Total de mulheres registadas: {mulheres}")
    print(Fore.GREEN + f"Média de idade do grupo: {media_idade:.2f} anos")
    print(Fore.GREEN + f"Média de idade dos homens: {media_idade_homens:.2f} anos")
    print(Fore.GREEN + f"Quantidade de mulheres com mais de 20 anos: {mulheres_mais_20}")

    # Pergunta para nova simulação
    novo = (
        input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()
    )

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break