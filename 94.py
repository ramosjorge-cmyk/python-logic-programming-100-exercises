import os
import subprocess

"""Exercício 94
94) [DESAFIO] Desenvolva um aplicativo que tenha um procedimento chamado  
Fibonacci() que recebe um único valor inteiro como parâmetro, indicando quantos  
termos da sequência serão mostrados na tela. O seu procedimento deve receber  
esse valor e mostrar a quantidade de elementos solicitados.  
Obs: Use os exercícios 70 e 75 para te ajudar na solução  
Ex:   
Fibonacci(5) vai gerar 1 >> 1 >> 2 >> 3 >> 5 >> FIM  
Fibonacci(9) vai gerar 1 >> 1 >> 2 >> 3 >> 5 >> 8 >> 13 >> 21 >> 34 >>
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

    print(Fore.CYAN + Style.BRIGHT + "🔢 Sequência de Fibonacci")
    
    while True:
        try: # Solicita o número de termos a mostrar, garantindo que seja um inteiro positivo
            n = int(input(Fore.YELLOW + "Digite o número de termos a mostrar: "))
            if n <= 0: # Verifica se o número é positivo
                print(Fore.RED + "Por favor, digite um número inteiro positivo.")
                continue # Se o número for válido, sai do loop
            break # Caso contrário, solicita novamente
        except ValueError: # Captura erros de conversão, caso o usuário digite algo que não seja um número inteiro
            print(Fore.RED + "Entrada inválida. Por favor, digite um número inteiro.")

    def fibonacci(termos: int) -> None:
        a, b = 1, 1 # Inicia os dois primeiros termos da sequência de Fibonacci
        for _ in range(termos): # Loop para gerar os termos da sequência, repetindo o número de vezes especificado por 'termos'
            print(Fore.GREEN + str(a), end=" >> " if _ < termos - 1 else " >> FIM\n") # Imprime o termo atual, seguido de ">>" se não for o último termo, ou ">> FIM" se for o último
            a, b = b, a + b # Atualiza os valores de 'a' e 'b' para os próximos termos da sequência (o próximo termo é a soma dos dois anteriores)

    fibonacci(n) # Chama a função para gerar e mostrar a sequência de Fibonacci com o número de termos especificado pelo usuário

    # Pergunta para nova simulação
    novo = (
        input(Fore.MAGENTA + "\n🔁 Deseja simular novamente? (s/n): ").strip().lower()
    )

    if novo != "s":
        cls()
        print(Fore.CYAN + Style.BRIGHT + "\n👋 Obrigado por simular! Até a próxima!\n")
        break
