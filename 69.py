import os
import subprocess

"""Exercício 69
69) [DESAFIO] Desenvolva um programa que leia o primeiro termo 
e a razão de uma PA (Progressão Aritmética), mostrando na tela 
os 10 primeiros elementos da PA e a soma entre todos os valores da sequência.
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
import time

while True:
    cls()

    # Título do programa
    print(Fore.CYAN + Style.BRIGHT + "🔢 Simulador de Progressão Aritmética (PA)")

    # ============================
    #  ENTRADA DE DADOS
    # ============================
    try:
        # Primeiro termo da PA (a1)
        primeiro_termo = float(input(Fore.YELLOW + "📌 Digite o primeiro termo da PA: "))

        # Razão da PA (r) → valor somado a cada termo
        razao = float(input(Fore.YELLOW + "📌 Digite a razão da PA: "))

        # Quantidade de termos que o utilizador quer ver
        quantidade = int(input(Fore.YELLOW + "📌 Quantos termos deseja ver? "))

    except ValueError:
        # Caso o utilizador digite algo que não seja número
        cls()
        print(Fore.RED + "❌ Entrada inválida. Por favor, digite números válidos.")
        time.sleep(1.5)
        continue

    # ============================
    #  CÁLCULO E EXIBIÇÃO DA PA
    # ============================
    print(Fore.GREEN + "\n📋 Elementos da PA:\n")

    soma = 0              # Acumulador para a soma dos termos
    termo = primeiro_termo  # Começa no primeiro termo da PA

    # Define cor base para os termos
    print(Fore.WHITE, end="")

    # Ciclo para gerar e mostrar os 'quantidade' termos da PA
    for i in range(quantidade):
        # Mostra o termo atual na mesma linha
        print(f"{termo: .2f}", end=" ", flush=True)

        # Soma o termo atual ao total
        soma += termo

        # Calcula o próximo termo da PA: termo seguinte = termo atual + razão
        termo += razao

        # Pequena pausa para criar efeito de animação
        time.sleep(0.3)

    # ============================
    #  RESULTADO FINAL
    # ============================
    print(Fore.GREEN + f"\n\n✅ Soma dos {quantidade} termos: {soma: .2f}")

    # Pergunta para nova simulação
    novo = (
        input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()
    )

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break
