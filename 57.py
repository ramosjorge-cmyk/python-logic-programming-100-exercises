import os
import subprocess

"""Exercício 57
57) Desenvolva um aplicativo que leia o salário e o sexo de vários funcionários. 
No final, mostre o total de salários pagos aos homens e o total pago às mulheres. 
O programa vai perguntar ao usuário se ele quer continuar ou não sempre que ler 
os dados de um funcionário.
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

# Acumuladores dos salários por género
salarios_homens = 0.0
salarios_mulheres = 0.0

while True:
    cls()
    print(Fore.CYAN + Style.BRIGHT + "💼 Simulador de Salários por Gênero 💼\n")

    # ============================================================
    #  LEITURA DO SALÁRIO E DO SEXO
    # ============================================================
    try:
        # Leitura do salário
        salario = float(
            input(Fore.YELLOW + "💰 Digite o salário do funcionário (€): ").strip()
        )

        # Validação simples de salário (não negativo)
        if salario < 0:
            print(Fore.RED + "❌ O salário não pode ser negativo.")
            input(Fore.MAGENTA + "Pressione ENTER para continuar...")
            continue

        # Leitura do sexo
        sexo = input(
            Fore.GREEN + "👤 Digite o sexo do funcionário (M/F): "
        ).strip().upper()

        # Atualização dos acumuladores conforme o sexo
        if sexo == "M":
            salarios_homens += salario
        elif sexo == "F":
            salarios_mulheres += salario
        else:
            # Sexo inválido → não acumula salário
            print(Fore.RED + "❌ Sexo inválido. Digite 'M' para masculino ou 'F' para feminino.")
            input(Fore.MAGENTA + "Pressione ENTER para continuar...")
            continue

    except ValueError:
        # Tratamento de erro caso o salário não seja numérico
        print(Fore.RED + "❌ Entrada inválida. Digite um número válido para o salário.")
        input(Fore.MAGENTA + "Pressione ENTER para continuar...")
        continue

    # ============================================================
    #  PERGUNTA SE QUER CONTINUAR A REGISTAR FUNCIONÁRIOS
    # ============================================================
    continuar = input(
        Fore.CYAN + "\nDeseja adicionar outro funcionário? (s/n): "
    ).strip().lower()

    # Se não for "s", sai do ciclo e mostra os resultados
    if continuar != "s":
        break

# ============================================================
#  APRESENTAÇÃO DOS RESULTADOS FINAIS
# ============================================================
cls()
print(Fore.CYAN + Style.BRIGHT + "📊 Resultados da Simulação 📊\n")
print(Fore.CYAN + f"📊 Total de salários pagos aos homens: €{salarios_homens:.2f}")
print(Fore.CYAN + f"📊 Total de salários pagos às mulheres: €{salarios_mulheres:.2f}")

# Mensagem final
print(Fore.MAGENTA + "\n👋 Obrigado por simular! Até a próxima!\n")