import os
import subprocess

"""Exercício 81
81) Crie um programa que leia a idade de 8 pessoas e guarde-as em um vetor. No  
final, mostre: 
a) Qual é a média de idade das pessoas cadastradas  
b) Em quais posições temos pessoas com mais de 25 anos  
c) Qual foi a maior idade digitada (podem haver repetições)  
d) Em que posições digitamos a maior idade
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

    # Lista para armazenar as idades
    idades: list[int] = []

    # Solicitar as idades de 8 pessoas
    for i in range(8):
        idade = int(input(Fore.CYAN + f"Digite a idade da  {i+1}ª pessoa: "))
        idades.append(idade)

    # Calcular a média das idades
    media = sum(idades) / len(idades)

    # Encontrar posições com mais de 25 anos
    posicoes_mais_de_25 = [i+1 for i, idade in enumerate(idades) if idade > 25]

    # Encontrar a maior idade e suas posições
    maior_idade = max(idades)
    posicoes_maior_idade = [i+1 for i, idade in enumerate(idades) if idade == maior_idade]

    # Exibir resultados
    print(Fore.GREEN + f"\nMédia das idades: {media:.2f}")
    print(Fore.GREEN + f"Posições com mais de 25 anos: {', '.join(map(str, posicoes_mais_de_25))}")
    print(Fore.GREEN + f"Maior idade: {maior_idade}")
    if len(posicoes_maior_idade) > 1:
        print(Fore.GREEN + f"Posições da maior idade: {', '.join(map(str, posicoes_maior_idade))}")
    elif len(posicoes_maior_idade) == 1:
        print (Fore.GREEN + f"Posição da maior idade: {posicoes_maior_idade[0]}")
    else:
        print(Fore.RED + "Nenhuma posição encontrada para a maior idade.")

    # Pergunta para nova simulação
    novo = (
        input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()
    )

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break
