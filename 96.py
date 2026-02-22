import os
import subprocess

"""Exercício 96
96) Crie um programa que tenha uma função Media(), que vai receber as 2 notas de  
um aluno e retornar a sua média para o programa principal. 
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
#  FUNÇÃO MEDIA
# ============================================================
# Regras:
# - recebe duas notas
# - devolve a média aritmética
# - não imprime nada dentro da função
# ============================================================
def Media(nota1: float, nota2: float) -> float:
    """Calcula a média de duas notas."""
    return (nota1 + nota2) / 2


while True:
    cls()

    print(Fore.CYAN + Style.BRIGHT + "📚 Simulador de Média Escolar 📚\n")

    # ============================================================
    #  ENTRADA E VALIDAÇÃO DAS NOTAS
    # ============================================================
    # Regras:
    # - devem ser números
    # - devem estar entre 0 e 20
    # - se houver erro, repete a leitura
    # ============================================================
    while True:
        try:
            nota1 = float(input(Fore.YELLOW + "Digite a primeira nota (0 a 20): ")) # tenta converter a entrada para float
            if nota1 < 0 or nota1 > 20: # validação da primeira nota
                print(Fore.RED + "❌ A nota deve estar entre 0 e 20.")
                continue # volta ao início do loop de validação para pedir as notas novamente

            nota2 = float(input(Fore.YELLOW + "Digite a segunda nota (0 a 20): "))
            if nota2 < 0 or nota2 > 20: # validação da segunda nota
                print(Fore.RED + "❌ A nota deve estar entre 0 e 20.")
                continue

            break  # notas válidas → sai do loop

        except ValueError: # captura erros de conversão (ex: se o utilizador digitar texto em vez de número)
            print(Fore.RED + "⚠️ Por favor, insira um número válido para as notas.")
            continue

    # ============================================================
    #  CÁLCULO DA MÉDIA
    # ============================================================
    media = Media(nota1, nota2) # chama a função Media, passando as notas digitadas pelo utilizador, e armazena o resultado da média na variável 'media'

    # ============================================================
    #  EXIBIÇÃO DO RESULTADO
    # ============================================================
    print(Fore.GREEN + Style.BRIGHT + f"\n📊 A média do aluno é: {media:.2f}") # imprime a média

    # mensagem de aprovado/reprovado
    if media >= 10: # condição de aprovação (média igual ou superior a 10)
        print(Fore.GREEN + Style.BRIGHT + "✅ Aprovado!") # imprime mensagem de aprovação
    else: # condição de reprovação (média inferior a 10)
        print(Fore.RED + Style.BRIGHT + "❌ Reprovado!") # imprime mensagem de reprovação

    # Pergunta para nova simulação
    novo = input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break