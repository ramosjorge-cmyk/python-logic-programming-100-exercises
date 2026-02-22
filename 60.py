# ============================================
# [60] Estatísticas completas de pessoas / Full People Statistics
# Tags: while, conditions
#
# Descrição (PT):
#   O programa lê nome, idade e sexo e determina pessoa mais velha, mulher mais jovem, média geral e outras contagens. Trabalha múltiplos critérios.
#
# Description (EN):
#   The program reads name, age, and gender and determines the oldest person, youngest woman, overall average, and other counts. It reinforces multi‑criteria evaluation.
# ============================================

import os
import subprocess

"""Exercício 60
60) Desenvolva um algoritmo que leia o nome, a idade e o sexo de várias pessoas. 
O programa vai perguntar se o usuário quer ou não continuar. 
No final, mostre: 
a) O nome da pessoa mais velha
b) O nome da mulher mais jovem
c) A média de idade do grupo
d) Quantos homens tem mais de 30 anos
e) Quantas mulheres tem menos de 18 anos
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

from typing import List, Dict, Any

while True:
    cls()
    print(Fore.CYAN + Style.BRIGHT + "📊 Simulador de registo de pessoas\n")

    # Variáveis para armazenar os dados
    pessoas: List[Dict[str, Any]] = [] # intervalo de pessoas
    
    while True:
        nome = input(Fore.YELLOW + "👤 Nome: ").strip()
        if not nome or any(char.isdigit() for char in nome) or len(nome) < 2:  # Verificar se o nome é vazio, contém números ou é muito curto
            print(Fore.RED + "❌ Nome inválido! Por favor, insira um nome válido.")
            continue # Verificar se o nome é válido antes de adicionar a pessoa à lista
        
        idade = int(input(Fore.YELLOW + "🎂 Idade: ").strip())
        if idade < 1 or idade > 120:  # Considerando 120 anos como limite máximo para idade humana:
            print(Fore.RED + "❌ Idade inválida! Por favor, insira um número entre 1 e 120.")
            continue # Verificar se a idade é válida antes de adicionar a pessoa à lista
        
        sexo = input(Fore.YELLOW + "🚻 Sexo (M/F): ").strip().upper()
        if sexo not in ['M', 'F']:
            print(Fore.RED + "❌ Sexo inválido! Por favor, insira 'M' para masculino ou 'F' para feminino.")
            continue # Verificar se o sexo é válido antes de adicionar a pessoa à lista
        
        pessoas.append({"nome": nome, "idade": idade, "sexo": sexo})
        
        continuar = (
            input(Fore.MAGENTA + "\n🔁 Deseja adicionar outra pessoa? (s/n): ")
            .strip().lower()
        )
        cls()
        if continuar != "s":
            break
    
    # Processar os dados
    if pessoas:
        pessoa_mais_velha = max(pessoas, key=lambda x: x["idade"])
        mulheres = [p for p in pessoas if p["sexo"] == "F"]
        mulher_mais_jovem = min(mulheres, key=lambda x: x["idade"], default=None)
        media_idade = sum(p["idade"] for p in pessoas) / len(pessoas)
        homens_mais_30 = sum(1 for p in pessoas if p["sexo"] == "M" and p["idade"] > 30)
        mulheres_menos_18 = sum(1 for p in pessoas if p["sexo"] == "F" and p["idade"] < 18)

        cls()
        print(Fore.CYAN + Style.BRIGHT + f"\n📋 Lista de pessoas registradas: {len(pessoas)}")
        for p in pessoas:
            print(f"👤 {p['nome']}, {p['idade']} anos, sexo: {p['sexo']}")

        # Exibir os resultados
        print(Fore.GREEN + Style.BRIGHT + "\n📋 Resultados:")
        print(f"👴 Pessoa mais velha: {pessoa_mais_velha['nome']} ({pessoa_mais_velha['idade']} anos)")
        if mulher_mais_jovem:
            print(f"👩 Mulher mais jovem: {mulher_mais_jovem['nome']} ({mulher_mais_jovem['idade']} anos)")
        else:
            print("👩 Não há mulheres registradas.")
        print(f"📊 Média de idade do grupo: {media_idade:.2f} anos")
        print(f"👨 Homens com mais de 30 anos: {homens_mais_30}")
        print(f"👩 Mulheres com menos de 18 anos: {mulheres_menos_18}")

    # Pergunta para nova simulação
    novo = (
        input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()
    )

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break
