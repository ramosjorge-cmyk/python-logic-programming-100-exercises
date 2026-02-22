# ============================================
# [95] Função Somador / Sum Function
# Tags: function, arithmetic
#
# Descrição (PT):
#   O programa cria uma função que recebe dois valores e retorna a soma. Trabalha retorno de funções.
#
# Description (EN):
#   The program creates a function that receives two values and returns their sum. It reinforces function returns.
# ============================================

import os
import subprocess

"""Exercício 95
95) Refaça o exercício 90, só que agora em forma de função Somador(), que vai  
receber dois parâmetros e vai retornar o resultado da soma entre eles para o  
programa principal.

[Dica: use a palavra reservada return para retornar o resultado da função.]
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
#  FUNÇÃO SOMADOR
# ============================================================
# Regras:
# - recebe dois números como parâmetros
# - calcula a soma
# - devolve (retorna) o resultado para o programa principal
# - não imprime nada dentro da função
# ============================================================
def Somador(num1: float, num2: float) -> float:
    """Recebe dois números e retorna a soma deles."""
    return num1 + num2


while True:
    cls()

    print(Fore.CYAN + Style.BRIGHT + "🔢 Simulador de Soma de Números 🔢\n")

    # ============================================================
    #  ENTRADA DE DADOS COM VALIDAÇÃO
    # ============================================================
    # regras:
    # - deve ser possível converter para float
    # - não pode ser vazio
    # - se der erro, volta a pedir os números
    # ============================================================
    try:
        numero1 = float(input(Fore.YELLOW + "Digite o primeiro número: "))
        numero2 = float(input(Fore.YELLOW + "Digite o segundo número: "))
    except ValueError:
        print(Fore.RED + "❌ Entrada inválida! Por favor, digite números válidos.")
        input(Fore.MAGENTA + "Pressione Enter para tentar novamente...")
        continue  # volta ao início do while principal

    # ============================================================
    #  PROCESSAMENTO (USO DA FUNÇÃO SOMADOR)
    # ============================================================
    # aqui chamamos a função Somador(), que devolve a soma
    # o programa principal é que decide o que fazer com o resultado
    # ============================================================
    resultado = Somador(numero1, numero2) # chama a função Somador, passando os números digitados pelo utilizador, e armazena o resultado da soma na variável 'resultado'

    # ============================================================
    #  SAÍDA DE RESULTADOS
    # ============================================================
    print(Fore.GREEN + f"✅ A soma de {numero1} e {numero2} é: {resultado}")

    # Pergunta para nova simulação
    novo = input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break
