import os
import subprocess

"""Exercício 36
36) Um programa de vida saudável quer dar pontos atividades físicas que podem ser trocados por dinheiro.
O sistema funciona assim:
- Cada hora de atividade física no mês vale pontos
- até 10h de atividade no mês: ganha 2 pontos por hora
- de 10h até 20h de atividade no mês: ganha 5 pontos por hora
- acima de 20h de atividade no mês: ganha 10 pontos por hora
A cada ponto ganho, o cliente fatura 0,05€ (5 cêntimos).
Faça um programa que leia quantas horas de atividade uma pessoa teve por mês, calcule e
mostre quantos pontos ela teve e quanto dinheiro ela conseguiu ganhar.
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

cls()
print(Fore.YELLOW + Style.BRIGHT + "\n🏃‍♂️  Programa de Vida Saudável - Simulador de Pontos e Recompensas 🏆\n")

while True:
    atividade = float(input(Fore.CYAN + Style.BRIGHT + "⏱️  Quantas horas de atividade física você teve no mês? "))
    if atividade < 10:
        pontos = 2 * atividade
    elif 10 <= atividade < 20:
        pontos = 5 * atividade
    else:
        pontos = 10 * atividade

    dinheiro = pontos * 0.05
    print(Fore.GREEN + Style.BRIGHT + f"\n🏆 Você ganhou {pontos:.2f} pontos e faturou €{dinheiro:.2f}!\n")

    # Pergunta para nova simulação
    novo = input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()

    # Limpa o ecrã entre simulações para melhorar a experiência do utilizador
    cls()

    if novo != "s":
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break