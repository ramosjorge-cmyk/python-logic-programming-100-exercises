"""
utils.py
--------

Funções utilitárias usadas pela interface de pesquisa:

Inclui:
- remoção de códigos ANSI (para medir larguras corretamente)
- limpeza do ecrã (Windows, Linux, macOS)
- destaque visual de termos pesquisados
- conversão segura de IDs para inteiro

Nenhuma destas funções altera dados — apenas ajudam na apresentação.
"""

import os
import re
import subprocess
from typing import Any
from colorama import Fore, Style

# ============================================================
#  REMOVER CÓDIGOS ANSI
# ============================================================

ANSI_REGEX = re.compile(r'\x1b\[[0-9;]*m')

def sem_ansi(texto: str) -> str:
    """
    Remove códigos ANSI de um texto.

    Útil para:
        - calcular larguras reais de strings
        - alinhar colunas
        - medir títulos sem cores

    Parâmetros:
        texto (str): Texto com possíveis códigos ANSI.

    Retorna:
        str: Texto sem códigos ANSI.
    """
    return ANSI_REGEX.sub('', texto)

# ============================================================
#  LIMPAR ECRÃ
# ============================================================

def cls() -> None:
    """
    Limpa o terminal de forma compatível com Windows, Linux e macOS.

    Usa:
        - 'cls' no Windows
        - 'clear' em sistemas Unix-like
    """
    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run(comando, shell=True)

# ============================================================
#  DESTACAR TEXTO
# ============================================================

def destacar(texto: str, termos: list[str]) -> str:
    """
    Destaca visualmente os termos encontrados no texto.

    Cada ocorrência é envolvida em:
        Fore.CYAN + Style.BRIGHT + termo + Style.RESET_ALL

    Parâmetros:
        texto (str): Texto original.
        termos (list[str]): Lista de termos a destacar.

    Retorna:
        str: Texto com os termos destacados.
    """
    texto_lower = texto.lower()
    resultado = texto

    for t in termos:
        if not t:
            continue

        idx = 0
        while True:
            idx = texto_lower.find(t, idx)
            if idx == -1:
                break

            original = resultado[idx:idx + len(t)]
            colorido = Fore.CYAN + Style.BRIGHT + original + Style.RESET_ALL

            resultado = resultado[:idx] + colorido + resultado[idx + len(t):]
            idx += len(original)

    return resultado

# ============================================================
#  CONVERTER ID PARA INTEIRO
# ============================================================

def id_para_int(valor: Any) -> int | None:
    """
    Converte valores para inteiro, se possível.

    Aceita:
        - int
        - strings numéricas ("12")

    Retorna:
        int  → se a conversão for possível
        None → caso contrário
    """
    if valor is None:
        return None
    if isinstance(valor, int):
        return valor
    if isinstance(valor, str) and valor.isdigit():
        return int(valor)
    return None