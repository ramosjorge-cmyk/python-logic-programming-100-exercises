"""
indice_termos.py
----------------

Constrói o índice invertido usado pela pesquisa inteligente.

O índice contém:
- palavras literais dos títulos e tags
- variações automáticas (acentos, plurais, erros comuns)
- sinónimos expandidos (SINONIMOS_EXPANDIDO)

Formato do índice:
    termo (str) → { ids de exercícios (set[int]) }

Este módulo não faz pesquisa — apenas prepara a estrutura usada pela pesquisa.
"""

# -*- coding: utf-8 -*-
from typing import Dict, List, Set, Any
from sinonimos import gerar_variacoes, SINONIMOS_EXPANDIDO

def construir_indice(exercicios: List[Dict[str, Any]]) -> Dict[str, Set[int]]:
    """
    Constrói um índice invertido para pesquisa semântica.

    Parâmetros:
        exercicios (list[dict]):
            Lista de exercícios carregados do index_loader.

    Retorna:
        dict[str, set[int]]:
            Mapa termo → conjunto de IDs de exercícios onde o termo aparece.

    O índice inclui:
        - palavras dos títulos (PT e EN)
        - palavras das tags
        - variações automáticas (acentos, plurais, erros comuns)
        - sinónimos expandidos (SINONIMOS_EXPANDIDO)
    """
    indice: Dict[str, Set[int]] = {}

    for ex in exercicios:
        ex_id: int = ex["id"]

        # Recolher texto base
        palavras: List[str] = []
        palavras.extend(ex["titulo_pt"].lower().split())
        palavras.extend(ex["titulo_en"].lower().split())
        palavras.extend([t.lower() for t in ex["tags"]])

        # Expandir cada palavra
        termos_final: Set[str] = set()
        for p in palavras:
            termos_final.add(p)

            # variações automáticas
            termos_final.update(gerar_variacoes(p))

            # sinónimos expandidos
            if p in SINONIMOS_EXPANDIDO:
                termos_final.update(SINONIMOS_EXPANDIDO[p])

        # Inserir no índice
        for termo in termos_final:
            if termo not in indice:
                indice[termo] = set()
            indice[termo].add(ex_id)

    return indice