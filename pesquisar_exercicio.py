"""
pesquisar_exercicio.py
----------------------

Interface principal da aplicação de pesquisa de exercícios.

Este módulo fornece:
- um menu interativo em modo consola
- pesquisa inteligente com paginação
- abertura de exercícios no VS Code
- navegação por setas e seleção por número
- destaque visual dos termos pesquisados

Fluxo geral:
1) Carrega o índice de exercícios
2) Constrói o índice semântico
3) Aguarda termos de pesquisa do utilizador
4) Executa a pesquisa inteligente
5) Mostra resultados paginados
6) Permite abrir exercícios diretamente no VS Code
"""

import os
import subprocess
import time
import msvcrt
from colorama import init, Fore, Style

from index_loader import carregar_index
from utils import cls, destacar, sem_ansi, id_para_int
from indice_termos import construir_indice
from pesquisa import pesquisar_inteligente

init(autoreset=True)

# ============================================================
#  ABRIR FICHEIRO NO VS CODE
# ============================================================

def abrir_no_vscode(ficheiro: str) -> None:
    """
    Abre um ficheiro no Visual Studio Code.

    Parâmetros:
        ficheiro (str): Caminho do ficheiro a abrir.

    Comportamento:
        - Verifica se o ficheiro existe.
        - Se existir, abre no VS Code.
        - Caso contrário, mostra erro e aguarda ENTER.
    """
    if not os.path.exists(ficheiro):
        print(Fore.RED + Style.BRIGHT + f"❌ Ficheiro não encontrado: {ficheiro}" + Style.RESET_ALL)
        input("ENTER para continuar...")
        return

    comando = f'code "{ficheiro}"'
    subprocess.run(comando, shell=True)

# ============================================================
#  MENU PRINCIPAL
# ============================================================

def menu():
    """
    Menu principal da aplicação.

    Funcionalidades:
        - Recebe termos de pesquisa do utilizador.
        - Executa a pesquisa inteligente.
        - Mostra resultados paginados.
        - Permite abrir exercícios pelo número.
        - Navegação por setas esquerda/direita.
    """
    exercicios = carregar_index()
    indice_termos = construir_indice(exercicios)

    while True:
        cls()
        print("\n" + Fore.CYAN + Style.BRIGHT + "🔎 PESQUISA DE EXERCÍCIOS (1–100)" + Style.RESET_ALL)

        termo = input(
            Fore.WHITE + Style.BRIGHT +
            "Digite o termo a pesquisar (ou ENTER para sair): " +
            Style.RESET_ALL
        ).strip()

        if termo == "":
            print("\n" + Fore.GREEN + Style.BRIGHT + "👋 A sair..." + Style.RESET_ALL)
            break

        # Executa a pesquisa inteligente
        resultados = pesquisar_inteligente(termo, indice_termos, exercicios)
        resultados = sorted(resultados, key=lambda ex: id_para_int(ex["id"]) or 0)

        if not resultados:
            print(Fore.RED + Style.BRIGHT + "❌ Nenhum exercício encontrado." + Style.RESET_ALL)
            input(Fore.WHITE + Style.BRIGHT + "Pressione ENTER para continuar..." + Style.RESET_ALL)
            continue

        # Termos para destacar nos resultados
        termos = [
            p for p in termo.split()
            if not p.startswith(("-", "id:", "tag:")) and p != "or"
        ]

        por_pagina = 10
        pagina = 0
        total = len(resultados)
        total_paginas = (total - 1) // por_pagina + 1

        while True:
            cls()

            print("\n" + Fore.CYAN + Style.BRIGHT + "🔎 PESQUISA DE EXERCÍCIOS (1–100)" + Style.RESET_ALL)
            print(Fore.YELLOW + Style.BRIGHT + "\n📌 RESULTADOS:" + Style.RESET_ALL)
            print(Fore.CYAN + Style.BRIGHT + f"🔍 {total} exercício(s) encontrado(s)" + Style.RESET_ALL)
            print(Fore.MAGENTA + Style.BRIGHT + f"\n📄 Página {pagina + 1} de {total_paginas}" + Style.RESET_ALL)

            inicio = pagina * por_pagina
            fim = inicio + por_pagina
            pagina_resultados = resultados[inicio:fim]

            largura_titulo = max(len(str(ex["titulo_pt"])) for ex in pagina_resultados)

            for ex in pagina_resultados:
                tags: list[str] = ex.get("tags") or []
                tags_str = destacar(", ".join(str(tag) for tag in tags), termos)

                ex_id = id_para_int(ex.get("id")) or 0
                id_str = f"[{ex_id}]".ljust(5)

                titulo_color = destacar(str(ex["titulo_pt"]), termos)
                titulo_sem_cor = sem_ansi(titulo_color)
                padding = largura_titulo - len(titulo_sem_cor)
                titulo_final = titulo_color + (" " * padding)

                print(
                    Fore.YELLOW + id_str + Style.RESET_ALL + " " +
                    Fore.WHITE + Style.BRIGHT + titulo_final + Style.RESET_ALL + "  " +
                    "🏷️ " + Fore.MAGENTA + Style.BRIGHT + tags_str + Style.RESET_ALL
                )

            print("\n← → para navegar | número = abrir exercício | ENTER = voltar à pesquisa")
            print("Escolha: ", end="", flush=True)

            buffer = ""
            start_time = time.time()
            voltar_pesquisa = False

            while True:
                if msvcrt.kbhit():
                    tecla = msvcrt.getch()

                    # SETAS (sequência especial)
                    if tecla == b'\xe0':
                        seta = msvcrt.getch()

                        # seta esquerda ←
                        if seta == b'K':
                            pagina = max(pagina - 1, 0)
                            buffer = ""
                            break

                        # seta direita →
                        if seta == b'M':
                            pagina = min(pagina + 1, total_paginas - 1)
                            buffer = ""
                            break

                        continue

                    tecla = tecla.decode("utf-8").lower()

                    # ENTER → voltar
                    if tecla == "\r":
                        buffer = ""
                        voltar_pesquisa = True
                        break

                    # dígito → adicionar ao buffer
                    if tecla.isdigit():
                        buffer += tecla

                        if len(buffer) > 3:
                            buffer = ""
                            break

                        num = int(buffer)

                        # 2 ou 3 dígitos → tenta abrir imediatamente
                        if len(buffer) >= 2:
                            ex_escolhido = next(
                                (ex for ex in pagina_resultados if id_para_int(ex.get("id")) == num),
                                None
                            )

                            if ex_escolhido:
                                ficheiro = str(ex_escolhido["ficheiro"])
                                print(Fore.GREEN + Style.BRIGHT + f"\n📂 Abrindo: {ficheiro}" + Style.RESET_ALL)
                                abrir_no_vscode(ficheiro)
                                buffer = ""
                                break
                            else:
                                print(Fore.RED + Style.BRIGHT + "\n❌ Exercício não encontrado nesta página." + Style.RESET_ALL)
                                time.sleep(1)
                                buffer = ""
                                break

                        start_time = time.time()
                        continue

                # timeout de 1 segundo para 1 dígito
                if buffer and (time.time() - start_time >= 1):
                    num = int(buffer)

                    ex_escolhido = next(
                        (ex for ex in pagina_resultados if id_para_int(ex.get("id")) == num),
                        None
                    )

                    if ex_escolhido:
                        ficheiro = str(ex_escolhido["ficheiro"])
                        print(Fore.GREEN + Style.BRIGHT + f"\n📂 Abrindo: {ficheiro}" + Style.RESET_ALL)
                        abrir_no_vscode(ficheiro)
                    else:
                        print(Fore.RED + Style.BRIGHT + "\n❌ Exercício não encontrado nesta página." + Style.RESET_ALL)
                        time.sleep(1)

                    buffer = ""
                    break

            if voltar_pesquisa:
                break

if __name__ == "__main__":
    menu()