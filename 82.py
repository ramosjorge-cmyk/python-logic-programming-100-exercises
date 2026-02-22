# ============================================
# [82] Estatísticas de notas / Grade Statistics
# Tags: list, arithmetic
#
# Descrição (PT):
#   O exercício lê 10 notas e calcula média, quantidade acima da média, maior nota e suas posições. Trabalha análise de desempenho.
#
# Description (EN):
#   The exercise reads 10 grades and computes class average, number above average, highest grade, and its positions. It practices performance analysis.
# ============================================

import os
import subprocess

"""Exercício 82 
82) Faça um algoritmo que leia a nota de 10 alunos de uma turma e 
guarde-as num vetor. 
No final, mostre:   
a) Qual é a média da turma  
b) Quantos alunos estão acima da média da turma  
c) Qual foi a maior nota digitada  
d) Em que posições a maior nota aparece
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

    print(Fore.CYAN + Style.BRIGHT + "📊 Simulador de Notas de Alunos\n"
+ Fore.YELLOW + "Digite as notas dos alunos (0 a 10):")

    # Lista para armazenar as notas
    notas: list[float] = []

    # Solicitar as notas de 10 alunos
    for i in range(10):
        while True:
            try: # Validação para garantir que a nota seja um número entre 0 e 10
                nota = float(input(Fore.CYAN + f"Digite a nota do {i+1}º aluno: "))
                if 0 <= nota <= 10: # Se a nota for válida, adiciona à lista e sai do loop
                    notas.append(nota)
                    break
                else: # Se a nota for inválida, exibe uma mensagem de erro e solicita novamente
                    print(Fore.RED + "Nota inválida! Digite uma nota entre 0 e 10.")
            except ValueError: # Se a entrada não for um número, exibe uma mensagem de erro e solicita novamente
                print(Fore.RED + "Entrada inválida! Digite um número.")

    # Calcular a média das notas
    media = sum(notas) / len(notas)

    # Contar alunos acima da média
    alunos_acima_media = sum(1 for nota in notas if nota > media)

    # Encontrar a maior nota e suas posições
    maior_nota = max(notas) # Encontrar a maior nota usando a função max()
    posicoes_maior_nota = [i+1 for i, nota in enumerate(notas) if nota == maior_nota] # Encontrar as posições da maior nota usando list comprehension e enumerate()

    # Exibir resultados
    print(Fore.GREEN + f"\nMédia da turma: {media:.2f}") # Exibir a média formatada com 2 casas decimais
    print(Fore.GREEN + f"Alunos acima da média: {alunos_acima_media}") # Exibir a quantidade de alunos acima da média"
    print(Fore.GREEN + f"Maior nota: {maior_nota}") # Exibir a maior nota
    if len(posicoes_maior_nota) > 1: # Verificar se há mais de uma posição para a maior nota e exibir as posições
        print(Fore.GREEN + f"Posições da maior nota: {', '.join(map(str, posicoes_maior_nota))}")
    elif len(posicoes_maior_nota) == 1: # Se houver apenas uma posição, exibir essa posição
        print (Fore.GREEN + f"Posição da maior nota: {posicoes_maior_nota[0]}")
    else: # Se não houver posições (o que é improvável, mas possível), exibir uma mensagem indicando que nenhuma posição foi encontrada
        print(Fore.RED + "Nenhuma posição encontrada para a maior nota.") # Exibir mensagem de erro caso não haja posições encontradas para a maior nota

    # Pergunta para nova simulação
    novo = (
        input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()
    )

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break
