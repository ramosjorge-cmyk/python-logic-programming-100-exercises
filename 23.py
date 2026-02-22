# ============================================
# [23] Desconto especial por sexo / Gender‑Based Discount
# Tags: input, conditions, percentage
#
# Descrição (PT):
#   O exercício aplica descontos diferentes conforme o sexo do cliente. Trabalha condições simples e porcentagens.
#
# Description (EN):
#   The exercise applies different discounts based on customer gender. It practices simple conditions and percentages.
# ============================================

import os
import subprocess

"""Exercício 23
23) Numa promoção exclusiva para o Dia da Mulher, uma loja quer dar descontos para todos, mas especialmente para mulheres. Faça um programa que leia nome, sexo e o valor das compras do cliente e calcule o preço com desconto. Sabendo que:
- Homens ganham 5% de desconto
- Mulheres ganham 13% de desconto
"""

# ============================================================
#  LIMPAR ECRÃ (Windows / Linux / macOS)
# ============================================================
def cls():
    """Limpa o terminal de forma compatível com vários sistemas operativos."""
    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run(comando, shell=True)


cls()
nome = input("Digite o nome do cliente: ")
sexo = input("Digite o sexo do cliente (M/F): ").strip().upper()
valor_compras = float(input("Digite o valor das compras (€): "))

if sexo == "F":
    desconto = 0.13 # 13% de desconto para mulheres
elif sexo == "M":
    desconto = 0.05 # 5% de desconto para homens
else:
    print("Sexo inválido. Por favor, insira 'M' para masculino ou 'F' para feminino.")
    exit()
valor_desconto = valor_compras * desconto
valor_final = valor_compras - valor_desconto
print(f"\nCliente: {nome}")
print(f"Valor original das compras: {valor_compras:.2f}€")
print(f"Desconto aplicado: {valor_desconto:.2f}€")
print(f"Valor final a pagar: {valor_final:.2f}€\n")    