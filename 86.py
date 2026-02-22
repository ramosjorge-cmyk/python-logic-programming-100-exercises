import os
import subprocess

"""Exercício 86
86) Crie um programa que tenha um procedimento Gerador() que, quando chamado,  
mostre a mensagem "Olá, Mundo!" com algum componente visual (linhas) Ex: Ao 
chamar Gerador() aparece:  
+-------=======------+  
Olá, Mundo!   
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

# Procedimento Gerador
    def Gerador(): # Gerador() é um procedimento que exibe a mensagem "Olá, Mundo!" com um componente visual.
        print(Fore.GREEN + Style.BRIGHT + "+-------=======------+")
        print(Fore.YELLOW + Style.BRIGHT + "      Olá, Mundo!")
        print(Fore.GREEN + Style.BRIGHT + "+-------=======------+")

    Gerador() # Chama o procedimento Gerador para exibir a mensagem formatada.

    # Pergunta para nova simulação
    novo = (
        input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()
    )

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break
