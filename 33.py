import os
import subprocess

"""Exercício 33
33) Escreva um programa para aprovar ou não o empréstimo bancário para a compra
de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e
em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que
ela não pode exceder 30% do salário ou então o empréstimo será negado.
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
    print(Fore.CYAN + Style.BRIGHT + "\n🏠 Empréstimo para Compra de Casa 🏠")  
    
    # Entrada de dados
    try:    
        valor_casa = float(input(Fore.YELLOW + "\n💰 Valor da casa: € ").replace(",", "."))
        salario = float(input(Fore.YELLOW + "💼 Salário do comprador: € ").replace(",", "."))
        anos = int(input(Fore.YELLOW + "📅 Quantos anos para pagar: "))
        
        # Cálculo da prestação mensal
        meses = anos * 12
        prestacao_mensal = valor_casa / meses
        limite = salario * 0.30
        
        # Verificação do empréstimo
        if prestacao_mensal <= limite:
            print(Fore.GREEN + Style.BRIGHT + f"\n✅ Empréstimo aprovado! Prestação mensal: € {prestacao_mensal:.2f}")
        else:
            print(Fore.RED + Style.BRIGHT + f"\n❌ Empréstimo negado! Prestação mensal: € {prestacao_mensal:.2f} excede 30% do salário.")
            
    except ValueError:
        print(Fore.RED + Style.BRIGHT + "\n⚠️ Entrada inválida! Por favor, insira números válidos.")
   
    # Pergunta para nova simulação
    novo = input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()
    
    # Limpa o ecrã entre simulações para melhorar a experiência do jogador
    cls()
            
    if novo != "s":
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break
