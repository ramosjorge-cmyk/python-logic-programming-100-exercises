import os
import subprocess

"""Exercício 35
35) Uma empresa de aluguer de carros precisa cobrar pelos seus serviços. O
aluguer de um carro custa R$90 por dia para carro popular e 150€ por dia para
carro de luxo. Além disso, o cliente paga por Km percorrido. Faça um programa
que leia o tipo de carro alugado (popular ou luxo), quantos dias de aluguer e
quantos Km foram percorridos. No final mostre o preço a ser pago de acordo com a
tabela a seguir:
- Carros populares (aluguer de R$90 por dia)
- Até 100Km percorridos: R$0,20 por Km
- Acima de 100Km percorridos: R$0,10 por Km
- Carros de luxo (aluguer de R$150 por dia)
- Até 200Km percorridos: R$0,30 por Km
- Acima de 200Km percorridos: R$0,25 por Km
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

cls()
while True:
    print(Fore.CYAN + Style.BRIGHT + "\n📊 Simulador de Índice de Massa Corporal (IMC)")
    
    try:
        altura = float(input(Fore.YELLOW + "\n📏 Altura (m): "))
        peso = float(input(Fore.YELLOW + "⚖️  Peso (kg): "))
        
        imc = peso / (altura ** 2)
        
        if imc < 18.5:
            classificacao = "Abaixo do peso"
            cor = Fore.RED
        elif 18.5 <= imc < 25:
            classificacao = "Peso ideal"
            cor = Fore.GREEN
        elif 25 <= imc < 30:
            classificacao = "Sobrepeso"
            cor = Fore.YELLOW
        elif 30 <= imc < 40:
            classificacao = "Obesidade"
            cor = Fore.RED
        else:
            classificacao = "Obesidade mórbida"
            cor = Fore.RED
        
        print(cor + Style.BRIGHT + f"\n🧮 O seu IMC é: {imc:.2f}")
        print(cor + Style.BRIGHT + f"📊 Classificação: {classificacao}")
        
    except ValueError:
        print(Fore.RED + Style.BRIGHT + "\n⚠️ Entrada inválida! Por favor, insira números válidos.")
   
    # Pergunta para nova simulação
    novo = input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()
    
    # Limpa o ecrã entre simulações para melhorar a experiência do utilizador
    cls()
            
    if novo != "s":
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break
