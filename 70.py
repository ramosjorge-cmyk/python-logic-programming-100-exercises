import os
import subprocess

"""Exercício 70
70) [DESAFIO] Faça um programa que mostre os 10 primeiros 
elementos da Sequência de Fibonacci:
1 1 2 3 5 8 13 21...
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

    print(Fore.CYAN + Style.BRIGHT + "🔢 Sequência de Fibonacci\n")

    try:
        # Quantidade de termos que o utilizador deseja ver
        quantidade = int(input(Fore.YELLOW + "📌 Quantos termos deseja ver? "))

        # Garante que a quantidade é um inteiro positivo
        if quantidade <= 0:
            raise ValueError

    except ValueError:
        # Caso o utilizador digite algo inválido (não inteiro ou <= 0)
        print(Fore.RED + "❌ Digite um número inteiro positivo.")
        time.sleep(1.5)
        continue

    # Gerar e mostrar os 10 primeiros elementos da Sequência de Fibonacci
    print(Fore.WHITE + "\nElementos da Sequência de Fibonacci:")
    
    a, b = 1, 1
    soma = 0  # Acumulador para a soma dos termos gerados
    
        # Ciclo para gerar 'quantidade' termos
    for i in range(quantidade):
        # Mostra o termo atual na mesma linha
        print(Fore.WHITE + f"{a}", end=" ", flush=True)

        # Soma o termo atual ao total
        soma += a

        # Atualiza os termos:
        # - o próximo 'a' passa a ser o 'b'
        # - o próximo 'b' passa a ser a soma dos dois anteriores
        a, b = b, a + b

        # Pequena pausa para criar efeito de animação na sequência
        time.sleep(0.5)
    
    print()  # ← ESTA LINHA CRIA A LINHA APÓS A SEQUÊNCIA
    
    print(Fore.GREEN + f"\n✅ Soma total dos termos gerados: {soma}")
    
    print()  # ← ESTA LINHA CRIA A LINHA APÓS A SEQUÊNCIA

    # Pergunta para nova simulação
    novo = (
        input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()
    )

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break
