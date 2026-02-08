import os
import subprocess

"""Exercício 22
22) Escreva um programa que leia o ano de nascimento de um rapaz e mostre a sua situação em relação ao alistamento militar.
- Se estiver antes dos 18 anos, mostre em quantos anos faltam para o alistamento.
- Se já tiver depois dos 18 anos, mostre quantos anos já se passaram do alistamento.
"""

# ============================================================
#  LIMPAR ECRÃ (Windows / Linux / macOS)
# ============================================================
def cls():
    """Limpa o terminal de forma compatível com vários sistemas operativos."""
    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run(comando, shell=True)


cls()
while True:
    ano = input("Digite o ano de nascimento:\n")

    if ano.isdigit():
        ano = int(ano)
        break
    else:
        print("Erro: só são permitidos números.")

ano = int(ano)  
idade = 2024 - ano
    
if idade < 18:
        tempo = 18 - idade
        print("\nAinda faltam {} anos para o alistamento.\n".format(tempo))
elif idade > 18:
        tempo = idade - 18
        print("\nJá se passaram {} anos do alistamento.\n".format(tempo))
else:
        print("\nVocê está com 18 anos. Aliste-se imediatamente.\n")