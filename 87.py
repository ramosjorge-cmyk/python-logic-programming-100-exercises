# ============================================
# [87] Gerador com mensagem personalizada / Custom Message Generator
# Tags: procedure, print
#
# Descrição (PT):
#   O programa permite passar uma mensagem personalizada ao gerador. Trabalha procedimentos com parâmetros.
#
# Description (EN):
#   The program allows passing a custom message to the generator. It reinforces procedures with parameters.
# ============================================

import os
import subprocess

"""Exercício 87
87) Crie um programa que melhore o procedimento Gerador() da questão anterior  
para que mostre uma mensagem personalizada, passada como parâmetro. Ex: Ao 
chamar Gerador("Aprendendo Portugol") aparece:  
+-------=======------+  
Aprendendo Portugol   
+-------=======------+ 
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

# Entrada de dados
    mensagem = input(Fore.CYAN + Style.BRIGHT + "Digite a mensagem para simular: ").strip()

    # Procedimento Gerador com parâmetro
    def Gerador(mensagem: str):
        print(Fore.GREEN + Style.BRIGHT + "+-------=======------+")
        print(Fore.YELLOW + Style.BRIGHT + f"      {mensagem}")
        print(Fore.GREEN + Style.BRIGHT + "+-------=======------+")

    Gerador(mensagem)  # Chama o procedimento Gerador com a mensagem fornecida

    # Pergunta para nova simulação
    novo = (
        input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()
    )

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break
