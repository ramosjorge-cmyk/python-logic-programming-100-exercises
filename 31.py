import os
import subprocess

"""Exercício 31
31) [DESAFIO] Crie um jogo de JoKenPo (Pedra-Papel-Tesoura)
"""

# ============================================================
#  LIMPAR ECRÃ (Windows / Linux / macOS)
# ============================================================
def cls():
    """Limpa o terminal de forma compatível com vários sistemas operativos."""
    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run(comando, shell=True)


cls()
import random
from colorama import init, Fore, Style

# Inicializar o Colorama
init(autoreset=True)

print(Style.BRIGHT + Fore.CYAN + "=== 🎮 Bem-vindo ao jogo de Pedra🪨  - Papel📄 - Tesoura✂️ ! ===\n")

# Dicionário para verificar as escolhas do jogador e do computador
opcoes = {
    "1": ("🪨", " Pedra"),
    "2": ("📄", "Papel"),
    "3": ("✂️", " Tesoura")
}

while True:
    print(Fore.YELLOW + "Escolha uma opção:")

    # Escolha do jogador
    print(Fore.GREEN   + "🪨   1 - Pedra")
    print(Fore.BLUE    + "📄  2 - Papel")
    print(Fore.MAGENTA + "✂️   3 - Tesoura")

    opcao_jogador = input(Fore.YELLOW + "Digite o número da sua escolha: ").strip()

    # Verificar se a escolha do jogador é válida
    if opcao_jogador not in opcoes:
        print(Fore.RED + Style.BRIGHT + "❌ Opção inválida. Por favor, escolha 1, 2 ou 3.")
    else:
        icone_jog, escolha_jogador = opcoes[opcao_jogador]

        # Escolha do computador
        icone_comp, escolha_computador = random.choice(list(opcoes.values()))

        print(Fore.GREEN + f"\nVocê escolheu: {icone_jog}  {escolha_jogador}")
        print(Fore.CYAN  + f"O computador escolheu: {icone_comp}  {escolha_computador}")

        # Resultado
        if escolha_jogador == escolha_computador:
            print(Fore.BLUE + Style.BRIGHT + "🤝 Empate!")
        elif (escolha_jogador == " Pedra" and escolha_computador == " Tesoura") or \
             (escolha_jogador == "Papel" and escolha_computador == " Pedra") or \
             (escolha_jogador == " Tesoura" and escolha_computador == "Papel"):
            print(Fore.GREEN + Style.BRIGHT + "🏆 Você venceu!")
        else:
            print(Fore.RED + Style.BRIGHT + "💀 O computador venceu!")

        # Pergunta para novo jogo
        novo = input(Fore.MAGENTA + "\n🔁 Deseja jogar novamente? (s/n): ").strip().lower()
        cls()
        
        if novo != "s":
            print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por jogar! Até a próxima!\n")
            break
