import os
import subprocess

"""Exercício 52
52) Crie um algoritmo que leia a idade de 10 pessoas, 
mostrando no final: a) Qual é a média de idade do grupo
b) Quantas pessoas tem mais de 18 anos
c) Quantas pessoas tem menos de 5 anos
d) Qual foi a maior idade lida
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
    print(Fore.CYAN + Style.BRIGHT + "📊 Simulador de Idades\n")
    idades = []
    for i in range(1, 11):
        while True:
            try:
                idade = int(input(Fore.YELLOW + f"Digite a idade da {i}ª pessoa: "))
                if idade < 0:
                    print(Fore.RED + "Idade não pode ser negativa. Tente novamente.")
                    continue
                idades.append(idade)
                break
            except ValueError:
                print(Fore.RED + "Entrada inválida. Por favor, digite um número inteiro.")

    media_idade = sum(idades) / len(idades)
    maiores_18 = sum(1 for idade in idades if idade > 18)
    menores_5 = sum(1 for idade in idades if idade < 5)
    maior_idade = max(idades)

    print(Fore.CYAN + f"\n📊 Resultados da Simulação:")
    print(Fore.GREEN + f"✅ Média de idade: {media_idade:.2f}")
    print(Fore.GREEN + f"✅ Pessoas com mais de 18 anos: {maiores_18}")
    print(Fore.GREEN + f"✅ Pessoas com menos de 5 anos: {menores_5}")
    print(Fore.GREEN + f"✅ Maior idade registrada: {maior_idade}")

    # Pergunta para nova simulação
    novo = (
        input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()
    )

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break
