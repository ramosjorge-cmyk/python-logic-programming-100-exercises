# ============================================
# [68] Estatísticas de sexo e peso / Gender and Weight Statistics
# Tags: for, conditions
#
# Descrição (PT):
#   O exercício lê sexo e peso de 8 pessoas e calcula várias estatísticas. Trabalha análise condicional em vetores.
#
# Description (EN):
#   The exercise reads gender and weight of 8 people and computes several statistics. It practices conditional analysis in loops.
# ============================================

import os
import subprocess

"""Exercício 68
68) Crie um programa que leia sexo e peso de 8 pessoas, usando a estrutura “para”. 
No final, mostre na tela:
a) Quantas mulheres foram cadastradas
b) Quantos homens pesam mais de 100Kg
c) A média de peso entre as mulheres
d) O maior peso entre os homens
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

    # Apresentação do programa
    print(Fore.CYAN + Style.BRIGHT + "📊 Simulador de Cadastro de Pessoas\n")

    # Variáveis para armazenar os resultados
    mulheres_cadastradas = 0
    homens_pesam_mais_100kg = 0
    soma_peso_mulheres = 0
    quantidade_mulheres = 0
    maior_peso_homens = 0

    # Leitura dos dados das pessoas
    for i in range(1, 9):
        print(Fore.YELLOW + f"{i}ª Pessoa:")

        # Leitura do sexo
        while True:
            sexo = input(Fore.MAGENTA + "  🚻 Sexo (M/F): ").strip().upper()
            if sexo in ["M", "F"]:
                break
            print(Fore.RED + "  ❌ Entrada inválida. Por favor, digite 'M' para masculino ou 'F' para feminino.")

        # Leitura do peso
        while True:
            try:
                peso = float(input(Fore.MAGENTA + "  ⚖️  Peso (kg): ").strip())
                if peso > 0:
                    break
                print(Fore.RED + "  ❌ O peso deve ser um número positivo.")
            except ValueError:
                print(Fore.RED + "  ❌ Entrada inválida. Por favor, digite um número para o peso.")
                continue
        
        # Pergunta para mostrar resultados parciais
        continuar = input(Fore.MAGENTA + "Mostrar resultados? (s/n): ").strip().lower()
        if continuar != "s":
            break


        # Processamento dos dados
        if sexo == "F":
            mulheres_cadastradas += 1
            soma_peso_mulheres += peso
            quantidade_mulheres += 1
        else:  # sexo == "M"
            if peso > 100:
                homens_pesam_mais_100kg += 1
            if peso > maior_peso_homens:
                maior_peso_homens = peso

    # Exibição dos resultados
    cls()
    print(Fore.CYAN + Style.BRIGHT + "📋 Resultados da Simulação\n")

    print(Fore.GREEN + f"✅ Mulheres cadastradas: {mulheres_cadastradas}")
    print(Fore.GREEN + f"✅ Homens que pesam mais de 100 kg: {homens_pesam_mais_100kg}")
    if quantidade_mulheres > 0:
        media_peso_mulheres = soma_peso_mulheres / quantidade_mulheres
        print(Fore.GREEN + f"✅ Média de peso entre as mulheres: {media_peso_mulheres:.2f} kg")
    else:
        print(Fore.RED + "❌ Nenhuma mulher foi cadastrada.")
    print(Fore.GREEN + f"✅ Maior peso entre os homens: {maior_peso_homens} kg")

    # Pergunta para nova simulação
    novo = (
        input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()
    )

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break
