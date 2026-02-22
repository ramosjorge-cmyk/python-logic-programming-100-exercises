import os
import subprocess

"""Exercício 97
97) Refaça o exercício 91, só que agora em forma de função Maior(), mas faça uma  
adaptação que vai receber TRÊS números como parâmetro e vai retornar qual foi o  
maior entre eles. 
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
#  FUNÇÃO MAIOR
# ============================================================
# Regras:
# - recebe três números
# - compara os três valores
# - retorna o maior deles
# - não imprime nada dentro da função
# ============================================================
def maior(num1: float, num2: float, num3: float) -> float:
    """Recebe três números e retorna o maior entre eles."""
    if num1 >= num2 and num1 >= num3:      # verifica se num1 é maior ou igual aos outros
        return num1
    elif num2 >= num1 and num2 >= num3:    # verifica se num2 é maior ou igual aos outros
        return num2
    else:                                  # caso contrário, num3 é o maior
        return num3


while True:
    cls()

    print(Fore.CYAN + Style.BRIGHT + "🔢 Simulador de maior número entre três números 🔢\n")

    # ============================================================
    #  ENTRADA DE DADOS COM VALIDAÇÃO
    # ============================================================
    try:
        n1 = float(input(Fore.YELLOW + "Digite o primeiro número: "))
        n2 = float(input(Fore.YELLOW + "Digite o segundo número: "))
        n3 = float(input(Fore.YELLOW + "Digite o terceiro número: "))
    except ValueError: # captura erros de conversão caso o usuário insira algo que não seja um número
        print(Fore.RED + "❌ Por favor, insira apenas números válidos.")
        input(Fore.MAGENTA + "Pressione Enter para tentar novamente...")
        continue # reinicia o loop para permitir nova tentativa de entrada de dados

    # ============================================================
    #  PROCESSAMENTO (CHAMADA DA FUNÇÃO)
    # ============================================================
    resultado = maior(n1, n2, n3) # chama a função maior passando os três números e armazena o resultado em 'resultado'

    # ============================================================
    #  SAÍDA DE RESULTADOS
    # ============================================================
    print(Fore.GREEN + Style.BRIGHT + f"\nO maior número entre {n1}, {n2} e {n3} é: {resultado}")

    # Pergunta para nova simulação
    novo = input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break