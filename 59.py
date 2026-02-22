# ============================================
# [59] Estatísticas de idade e sexo / Age and Gender Statistics
# Tags: while, conditions
#
# Descrição (PT):
#   O exercício lê idade e sexo de várias pessoas e calcula maior idade, número de homens, mulher mais jovem e média dos homens.
#
# Description (EN):
#   The exercise reads age and gender of multiple people and computes highest age, number of men, youngest woman, and men’s average age.
# ============================================

import os
import subprocess

"""Exercício 59
59) Crie um programa que leia o sexo e a idade de várias pessoas. 
O programa vai perguntar se o usuário quer continuar ou não a cada pessoa. 
No final, mostre: 
a) qual é a maior idade lida
b) quantos homens foram cadastrados
c) qual é a idade da mulher mais jovem
d) qual é a média de idade entre os homens
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
    print(Fore.CYAN + Style.BRIGHT + "📊 Simulador de idades e sexos dos alunos\n")

    idades: list[int] = []
    sexos: list[str] = []

    while True:
        try:
            sexo = input(Fore.YELLOW + "Digite o sexo do aluno (M/F) ou '999' para parar: ").strip().upper()
            if sexo == '999':
                break
            elif sexo not in ['M', 'F']:
                print(Fore.RED + "❌ Sexo inválido! Por favor, insira 'M' para masculino ou 'F' para feminino.")
                continue

            idade = int(input(Fore.YELLOW + "Digite a idade do aluno: "))
            if idade < 1 or idade > 120:  # Considerando 120 anos como limite máximo para idade humana:
                print(Fore.RED + "❌ Idade inválida! Por favor, insira um número entre 1 e 120.")
                continue

            sexos.append(sexo)
            idades.append(idade)

        except ValueError:
            print(Fore.RED + "❌ Entrada inválida! Por favor, insira um número inteiro para a idade.")

    # Exibir resultados
    if idades:
        maior_idade = max(idades) # a) Encontrar a maior idade lida
        
        total_homens = sum(1 for s in sexos if s == 'M') # b) Contar quantos homens foram cadastrados
        
        mulheres = [idades[i] for i in range(len(sexos)) if sexos[i] == 'F']  # c) Listar idades das mulheres para encontrar a mais jovem
        idade_mulher_mais_jovem = min(mulheres) if mulheres else None # c) Encontrar a idade da mulher mais jovem, se houver mulheres cadastradas
        
        soma_idades_homens = sum(idades[i] for i in range(len(sexos)) if sexos[i] == 'M') # d) Somar apenas as idades dos homens
        media_idade_homens = soma_idades_homens / total_homens if total_homens > 0 else 0 # d) Calcular a média, evitando divisão por zero
        
        print(Fore.CYAN + f"📊 Maior idade lida: {maior_idade}")                            # a
        print(Fore.CYAN + f"📊 Total de homens cadastrados: {total_homens}")                # b
        print(Fore.CYAN + f"📊 Idade da mulher mais jovem: {idade_mulher_mais_jovem}")      # c
        print(Fore.CYAN + f"📊 Média de idade entre os homens: {media_idade_homens:.2f}")   # d
    else:
        print(Fore.RED + "❌ Nenhuma idade válida foi registrada.")

    # Pergunta para nova simulação
    novo = (
        input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()
    )

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break
