import os
import subprocess

"""Exercício 58
58) Faça um algoritmo que leia a idade de vários alunos de uma turma. 
O programa vai parar quando for digitada a idade 999. 
No final, mostre quantos alunos existem na turma e qual é a média de idade do grupo.
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

    print(Fore.CYAN + Style.BRIGHT + "📊 Simulador de Idades dos Alunos\n")
    
    idades: list[int] = []
    
    while True:
        try:
            idade = int(input(Fore.YELLOW + "Digite a idade do aluno (ou 999 para parar): "))
            if idade == 999:
                break
            elif idade < 1 or idade > 120:  # Considerando 120 anos como limite máximo para idade humana:
                print(Fore.RED + "❌ Idade inválida! Por favor, insira um número entre 1 e 120.")
            else:
                idades.append(idade)
        except ValueError:
            print(Fore.RED + "❌ Entrada inválida! Por favor, insira um número inteiro.")

    # Exibir resultados
    if idades:
        total_alunos = len(idades)
        media_idade = sum(idades) / total_alunos
        print(Fore.CYAN + f"📊 Total de alunos: {total_alunos}")
        print(Fore.CYAN + f"📊 Média de idade: {media_idade:.2f} anos")
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