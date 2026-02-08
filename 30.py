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

print("Bem-vindo ao jogo de JoKenPo!")
print("Escolha uma opção:")
print("1 - Pedra")
print("2 - Papel")
print("3 - Tesoura")

opcao_jogador = input("Digite o número da sua escolha: ")
opcoes = { "1": "Pedra", "2": "Papel", "3": "Tesoura" }
if opcao_jogador not in opcoes:
    print("Opção inválida. Por favor, escolha 1, 2 ou 3.")
else:
    escolha_jogador = opcoes[opcao_jogador]
    
    escolha_computador = random.choice(list(opcoes.values()))

    print(f"Você escolheu: {escolha_jogador}")
    print(f"O computador escolheu: {escolha_computador}")

    if escolha_jogador == escolha_computador:
        print("Empate!")
    elif (escolha_jogador == "Pedra" and escolha_computador == "Tesoura") or \
         (escolha_jogador == "Papel" and escolha_computador == "Pedra") or \
         (escolha_jogador == "Tesoura" and escolha_computador == "Papel"):
        print("Você venceu!")
    else:
        print("O computador venceu!")
    