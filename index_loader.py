"""
index_loader.py
---------------

Responsável por carregar o ficheiro INDEX.md e convertê-lo numa lista
estruturada de exercícios.

Cada entrada do INDEX.md segue o formato:

    [ID] Título em Português
    Título em Inglês
    Tags: tag1, tag2, tag3

Este módulo:
- lê o ficheiro INDEX.md
- extrai ID, títulos, tags e nome do ficheiro correspondente
- devolve uma lista de dicionários prontos para pesquisa
"""

import os
import re
from typing import Any

# Caminho absoluto da pasta onde estão os exercícios e o INDEX.md
PASTA_EXERCICIOS = os.path.dirname(os.path.abspath(__file__))

def carregar_index() -> list[dict[str, Any]]:
    """
    Carrega e interpreta o ficheiro INDEX.md, devolvendo uma lista de exercícios.

    Retorna:
        list[dict]:
            Cada dicionário contém:
                - id (int)
                - titulo_pt (str)
                - titulo_en (str)
                - tags (list[str])
                - ficheiro (str): caminho completo do ficheiro Python do exercício
    """
    caminho = os.path.join(PASTA_EXERCICIOS, "INDEX.md")
    exercicios: list[dict[str, Any]] = []

    # Ler todas as linhas do ficheiro
    with open(caminho, "r", encoding="utf-8") as f:
        linhas = [linha.rstrip("\n") for linha in f]

    i = 0
    while i < len(linhas):
        linha = linhas[i].strip()

        # Encontrar início de entrada: "[ID] Título"
        m = re.match(r"\[(\d+)\]\s*(.*)", linha)
        if not m:
            i += 1
            continue

        num = int(m.group(1))
        titulo_pt = m.group(2).strip()

        # Próxima linha = título EN
        titulo_en = ""
        if i + 1 < len(linhas):
            titulo_en = linhas[i + 1].strip()

        # Linha seguinte = Tags
        tags = []
        if i + 2 < len(linhas):
            m_tags = re.match(r"Tags:\s*(.*)", linhas[i + 2].strip())
            if m_tags:
                tags = [t.strip() for t in m_tags.group(1).split(",")]

        # Nome do ficheiro (casos especiais incluídos)
        if 38 <= num <= 41:
            nome_ficheiro = "38 a 41.py"
        elif 44 <= num <= 45:
            nome_ficheiro = "44 e 45.py"
        else:
            nome_ficheiro = f"{num:02}.py"

        exercicios.append({
            "id": num,
            "titulo_pt": titulo_pt,
            "titulo_en": titulo_en,
            "tags": tags,
            "ficheiro": os.path.join(PASTA_EXERCICIOS, nome_ficheiro),
        })

        # Avançar até ao próximo bloco (linha que começa por "[")
        i += 1
        while i < len(linhas) and not linhas[i].strip().startswith("["):
            i += 1

    return exercicios