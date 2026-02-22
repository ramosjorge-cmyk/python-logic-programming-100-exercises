import os
import subprocess

"""Exercício 100 
100) Melhore o exercício 96, criando além da função Media() uma outra função  
chamada Situacao(), que vai retornar para o programa principal se o aluno está  
APROVADO, em RECUPERAÇÃO ou REPROVADO. Essa nova função vai receber como  
parâmetro o resultado retornado pela função Media().  
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
#  FUNÇÃO MÉDIA
# ============================================================
# Regras:
# - recebe duas notas
# - devolve a média aritmética
# - não imprime nada dentro da função
# ============================================================
def Media(n1: float, n2: float) -> float: # -> float indica que a função retorna um valor do tipo float
    """Calcula a média de duas notas e retorna o valor."""
    return (n1 + n2) / 2 # calcula a média aritmética das duas notas e retorna o resultado


# ============================================================
#  FUNÇÃO SITUAÇÃO
# ============================================================
# Regras:
# - recebe a média calculada pela função Media()
# - devolve uma string com a situação do aluno
# - não imprime nada dentro da função
# - segue as regras:
#     APROVADO: média >= 10.0
#     RECUPERAÇÃO: 7.0 <= média < 10.0
#     REPROVADO: média < 7.0
# ============================================================
def Situacao(media: float) -> str: # -> str indica que a função retorna um valor do tipo string
    """Retorna a situação do aluno com base na média."""
    if media >= 10.0: # se a média for maior ou igual a 10.0, o aluno está aprovado
        return "APROVADO"
    elif 7.0 <= media < 10.0: # se a média for maior ou igual a 7.0 e menor que 10.0, o aluno está em recuperação
        return "RECUPERAÇÃO"
    else: # se a média for menor que 7.0, o aluno está reprovado
        return "REPROVADO"


while True:
    cls()

    print(Fore.CYAN + Style.BRIGHT + "📚 Simulador de média e situação do aluno 📚\n")

    # ============================================================
    #  ENTRADA E VALIDAÇÃO DAS NOTAS
    # ============================================================
    # Regras:
    # - devem ser números
    # - devem estar entre 0 e 20
    # - se houver erro, repete a leitura
    # ============================================================
    try:
        nota1 = float(input(Fore.YELLOW + "Digite a primeira nota (0 a 20): "))
        if nota1 < 0 or nota1 > 20: # valida se a nota está dentro do intervalo permitido
            print(Fore.RED + "❌ A nota deve estar entre 0 e 20.")
            input(Fore.MAGENTA + "Pressione Enter para tentar novamente...")
            continue

        nota2 = float(input(Fore.YELLOW + "Digite a segunda nota (0 a 20): "))
        if nota2 < 0 or nota2 > 20: # valida se a nota está dentro do intervalo permitido
            print(Fore.RED + "❌ A nota deve estar entre 0 e 20.")
            input(Fore.MAGENTA + "Pressione Enter para tentar novamente...")
            continue

    except ValueError: # captura o erro caso o usuário digite algo que não seja um número
        print(Fore.RED + "\n❌ Entrada inválida! Por favor, insira números válidos.")
        input(Fore.MAGENTA + "Pressione Enter para tentar novamente...")
        continue

    # ============================================================
    #  PROCESSAMENTO (CÁLCULO DA MÉDIA E SITUAÇÃO)
    # ============================================================
    media = Media(nota1, nota2)          # calcula a média usando a função Media()
    situacao = Situacao(media)           # determina a situação usando a função Situacao()

    # ============================================================
    #  EXIBIÇÃO DOS RESULTADOS
    # ============================================================
    print(Fore.GREEN + f"\n📊 Média: {media:.2f}") # imprime a média
    print(Fore.BLUE + f"🎓 Situação: {situacao}") # imprime a situação

    # Pergunta para nova simulação
    novo = input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break