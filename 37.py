# ============================================
# [37] Reajuste salarial por gênero / Salary Adjustment by Gender
# Tags: float, conditions
#
# Descrição (PT):
#   O programa aplica aumentos diferentes conforme género e tempo de empresa. Trabalha condições compostas e múltiplos critérios.
#
# Description (EN):
#   The program applies salary raises based on gender and years of employment. It practices compound conditions and multi‑criteria logic.
# ============================================

import os
import subprocess

"""Exercício 37
37) Uma empresa precisa reajustar o salário dos seus funcionários, dando um
aumento de acordo com alguns fatores. Faça um programa que leia o salário atual,
o género do funcionário e há quantos anos esse funcionário trabalha na empresa.
No final, mostre o seu novo salário, baseado na tabela a seguir:
- Mulheres
- menos de 15 anos de empresa: +5%
- de 15 até 20 anos de empresa: +12%
- mais de 20 anos de empresa: +23%
- Homens
- menos de 20 anos de empresa: +3%
- de 20 até 30 anos de empresa: +13%
- mais de 30 anos de empresa: +25%
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

def cabecalho():
    print(
        Fore.CYAN
        + Style.BRIGHT
        + "📊 Simulador de reajuste salarial\n"
        + Fore.YELLOW
        + "💡 Este programa calcula o novo salário de um funcionário com base no seu género e antiguidade na empresa.\n"
    )

cls()
cabecalho()

while True:

    # --- SALÁRIO ---
    while True:
        try:
            salario_atual = float(input(Fore.YELLOW + "💰 Digite o salário atual do funcionário (€): ").replace(",", "."))
            if salario_atual <= 0:
                print(Fore.RED + "❌ Salário inválido. Digite um valor numérico positivo.")
            else:
                break
        except ValueError:
            print(Fore.RED + "❌ Valor inválido. Digite um número (use vírgula ou ponto).")

    # --- GÉNERO ---
    genero = (input(Fore.YELLOW + "👤 Digite o género do funcionário (M/F): ").strip().upper())
    while genero not in ["M", "F"]:
        print(Fore.RED + "❌ Género inválido. Por favor, digite 'M' para masculino ou 'F' para feminino.")
        genero = (input(Fore.YELLOW + "👤 Digite o género do funcionário (M/F): ").strip().upper())

    # --- ANOS DE EMPRESA ---
    while True:
        try:
            anos_empresa = int(
                input(
                    Fore.YELLOW
                    + "📅 Há quantos anos o funcionário trabalha na empresa? "
                )
            )
            if anos_empresa < 0:
                print(
                    Fore.RED
                    + "❌ Antiguidade inválida. Digite um número inteiro não negativo."
                )
            else:
                break
        except ValueError:
            print(Fore.RED + "❌ Valor inválido. Digite um número inteiro.")

    # --- CÁLCULO ---
    if genero == "F":
        if anos_empresa < 15:
            aumento = 0.05
        elif anos_empresa <= 20:
            aumento = 0.12
        else:
            aumento = 0.23
    else:
        if anos_empresa < 20:
            aumento = 0.03
        elif anos_empresa <= 30:
            aumento = 0.13
        else:
            aumento = 0.25

    novo_salario = salario_atual * (1 + aumento)
    print(
        Fore.GREEN
        + Style.BRIGHT
        + f"\n✅ O novo salário do funcionário é: €{novo_salario:.2f}"
    )

    # --- NOVA SIMULAÇÃO ---
    novo = (
        input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()
    )

    cls()

    if novo != "s":
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break

    cabecalho()
