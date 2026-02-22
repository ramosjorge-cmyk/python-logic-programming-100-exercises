# ============================================
# [98] Função SuperSomador / Interval Sum Function
# Tags: function, loop
#
# Descrição (PT):
#   O exercício cria uma função que soma todos os valores no intervalo entre dois números. Trabalha laços e acumulação.
#
# Description (EN):
#   The exercise creates a function that sums all values in the interval between two numbers. It practices loops and accumulation.
# ============================================

import os
import subprocess

"""Exercício 98
98) Crie um programa que tenha uma função SuperSomador(), que vai receber dois  
números como parâmetro e depois vai retornar a soma de todos os valores no  
intervalo entre os valores recebidos.  
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

# ============================================================
#  FUNÇÃO SUPERSOMADOR
# ============================================================
# Regras:
# - recebe dois números inteiros (início e fim) e um passo
# - aceita intervalos crescentes e decrescentes
# - passo pode ser positivo ou negativo, mas nunca zero
# - devolve:
#   - a soma total
#   - a lista de números do intervalo
#   - a expressão textual da soma ("1 + 3 + 5")
#   - a lista dos passos parciais da soma
# ============================================================
def SuperSomador(inicio: int, fim: int, passo: int) -> tuple[int, list[int], str, list[int]]:
    """Retorna soma, lista de valores, expressão textual e somas parciais."""

    # garantir que o passo não é zero
    if passo == 0:
        raise ValueError("O passo não pode ser zero.")

    # ajustar o passo ao sentido do intervalo, se necessário
    if inicio < fim and passo < 0:
        passo = -passo  # torna positivo
    elif inicio > fim and passo > 0:
        passo = -passo  # torna negativo

    # criar lista de números no intervalo com o passo indicado
    numeros = list(range(inicio, fim + (1 if passo > 0 else -1), passo))

    # expressão textual: "1 + 3 + 5"
    expressao = " + ".join(str(n) for n in numeros)

    # somas parciais: [1, 1+3, 1+3+5, ...]
    somas_parciais: list[int] = []
    acumulador = 0
    for n in numeros:
        acumulador += n
        somas_parciais.append(acumulador)

    soma_total = somas_parciais[-1] if somas_parciais else 0

    return soma_total, numeros, expressao, somas_parciais


while True:
    cls()

    print(Fore.CYAN + Style.BRIGHT + "🔢 Super Somador 🔢\n")

    # ============================================================
    #  ENTRADA DE DADOS COM VALIDAÇÃO
    # ============================================================
    try:
        num1 = int(input(Fore.YELLOW + "Digite o primeiro número (início): "))
        num2 = int(input(Fore.YELLOW + "Digite o segundo número (fim): "))
        passo = int(input(Fore.YELLOW + "Digite o passo (≠ 0): "))
        if passo == 0:
            print(Fore.RED + "❌ O passo não pode ser zero.")
            input(Fore.MAGENTA + "Pressione Enter para tentar novamente...")
            continue
    except ValueError:
        print(Fore.RED + "❌ Por favor, insira números inteiros válidos!")
        input(Fore.MAGENTA + "Pressione Enter para tentar novamente...")
        continue

    # ============================================================
    #  PROCESSAMENTO (CHAMADA DA FUNÇÃO)
    # ============================================================
    try:
        soma, lista_numeros, expressao, somas_parciais = SuperSomador(num1, num2, passo)
    except ValueError as e:
        print(Fore.RED + f"❌ Erro: {e}")
        input(Fore.MAGENTA + "Pressione Enter para tentar novamente...")
        continue

    # ============================================================
    #  SAÍDA DE RESULTADOS
    # ============================================================
    # mostrar intervalo em forma de lista
    print(Fore.CYAN + Style.BRIGHT + "\n📌 Intervalo em forma de lista:")
    print(Fore.WHITE + Style.BRIGHT + str(lista_numeros))

    # mostrar expressão da soma
    print(Fore.CYAN + Style.BRIGHT + "\n📌 Expressão da soma:")
    print(Fore.WHITE + Style.BRIGHT + expressao)

    # mostrar passo a passo da soma
    print(Fore.CYAN + Style.BRIGHT + "\n📌 Passo a passo da soma:")
    for i, parcial in enumerate(somas_parciais, start=1):
        print(Fore.GREEN + f"Após {i} termo(s): {parcial}")

    # resultado final
    print(Fore.GREEN + Style.BRIGHT + f"\n✅ A soma de todos os valores entre {num1} e {num2} (passo {passo}) é: {soma}")

    # Pergunta para nova simulação
    novo = input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break