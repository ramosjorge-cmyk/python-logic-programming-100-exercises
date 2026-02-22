# ============================================
# [35] Aluguel de carro (popular/luxo) / Car Rental (Popular/Luxury)
# Tags: float, conditions
#
# Descrição (PT):
#   O programa calcula o custo do aluguel considerando tipo de carro, dias e quilometragem. Trabalha condições complexas e cálculos combinados.
#
# Description (EN):
#   The program computes rental cost based on car type, rental days, and kilometers driven. It practices complex conditions and combined calculations.
# ============================================

import os
import subprocess

"""Exercício 35
35) Uma empresa de aluguer de carros precisa cobrar pelos seus serviços. O
aluguer de um carro custa 90€ por dia para carro popular e 150€ por dia para
carro de luxo. Além disso, o cliente paga por Km percorrido. Faça um programa
que leia o tipo de carro alugado (popular ou luxo), quantos dias de aluguer e
quantos Km foram percorridos. No final mostre o preço a ser pago de acordo com a
tabela a seguir:
- Carros populares (aluguer de 90€ por dia)
- Até 100Km percorridos: 0,20€ por Km
- Acima de 100Km percorridos: 0,10€ por Km
- Carros de luxo (aluguer de 150€ por dia)
- Até 200Km percorridos: 0,30€ por Km
- Acima de 200Km percorridos: 0,25€ por Km
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
#  FUNÇÕES DE VALIDAÇÃO NUMÉRICA
# ============================================================
def ler_int(mensagem: str) -> int:
    while True:
        try:
            valor = int(input(mensagem))
            if valor < 0:
                print(Fore.RED + "❌ O valor não pode ser negativo.")
                continue
            return valor
        except ValueError:
            print(Fore.RED + "❌ Entrada inválida. Digite um número inteiro.")

def ler_float(mensagem: str) -> float:
    while True:
        try:
            valor = float(input(mensagem))
            if valor < 0:
                print(Fore.RED + "❌ O valor não pode ser negativo.")
                continue
            return valor
        except ValueError:
            print(Fore.RED + "❌ Entrada inválida. Digite um número válido.")

# ============================================================
#  PROGRAMA PRINCIPAL
# ============================================================
cls()
while True:
    print(Fore.CYAN + Style.BRIGHT + "🚗 Bem-vindo à Simulação de aluguer de carros! 🚗\n")

    # Leitura do tipo de carro
    tipo_carro = input(Fore.YELLOW + "Digite o tipo de carro (popular/luxo): ").strip().lower()

    # Validação do tipo de carro
    while tipo_carro not in ["popular", "luxo"]:
        print(Fore.RED + "\n❌ Tipo de carro inválido. Por favor, digite 'popular' ou 'luxo'.")
        tipo_carro = input(Fore.YELLOW + "Digite o tipo de carro (popular/luxo): ").strip().lower()

    # Ícones específicos
    if tipo_carro == "popular":
        print(Fore.GREEN + "\n 🛻 Carro popular selecionado!")
    else:
        print(Fore.CYAN + "\n🏎️  Carro de luxo selecionado!")

    # Leitura dos valores numéricos
    dias = ler_int(Fore.YELLOW + "\n📅 Digite o número de dias de aluguer: ")
    km_percorridos = ler_float(Fore.YELLOW + "📏 Digite o número de Km percorridos: ")

    # Cálculo do preço
    if tipo_carro == "popular":
        preco_dia = 90
        preco_km = 0.20 if km_percorridos <= 100 else 0.10
    else:
        preco_dia = 150
        preco_km = 0.30 if km_percorridos <= 200 else 0.25

    preco_total = (preco_dia * dias) + (preco_km * km_percorridos)

    # Exibição do resultado
    print(Fore.GREEN + Style.BRIGHT + f"\n💰 Preço total a pagar: {preco_total:.2f}€")


    # Pergunta para nova simulação
    novo = input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()


    # Limpa o ecrã entre simulações para melhorar a experiência do utilizador
    cls()

    if novo != "s":
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break
