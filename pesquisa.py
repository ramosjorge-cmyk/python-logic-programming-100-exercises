"""
pesquisa.py
-----------

Módulo responsável pelas duas funções de pesquisa:

1) pesquisar() — versão antiga, baseada em:
   - palavras literais
   - sinónimos diretos
   - filtros OR, NOT, TAG, ID
   - relevância simples

2) pesquisar_inteligente() — versão avançada, baseada em:
   - expansão semântica
   - intenção (ação, objeto, objetivo)
   - temas automáticos
   - similaridade semântica leve
   - pesos inteligentes
   - ranking avançado

Este módulo não carrega ficheiros nem gere interface — apenas calcula resultados.
"""

# -*- coding: utf-8 -*-
from typing import Dict, List, Set, Any

from sinonimos import (
    BASE_SINONIMOS,
    SINONIMOS_EXPANDIDO,
    expandir_frase,
    gerar_variacoes,
    descobrir_tema,
    extrair_intencao,
    similaridade_semantica,
)

# ============================================================
#  FUNÇÃO DE PESQUISA ANTIGA (compatibilidade)
# ============================================================

def pesquisar(exercicios: List[Dict[str, Any]], termo: str) -> List[Dict[str, Any]]:
    """
    Pesquisa simples baseada em:
    - palavras literais
    - sinónimos diretos (BASE_SINONIMOS)
    - filtros OR, NOT, TAG e ID
    - relevância básica por título e tags

    Parâmetros:
        exercicios (list): Lista de exercícios carregados do índice.
        termo (str): Termo de pesquisa introduzido pelo utilizador.

    Retorna:
        list: Lista de exercícios ordenados por relevância.
    """
    termo = termo.lower()
    partes = termo.split()

    termos_normais: List[str] = []
    termos_or: List[str] = []
    termos_not: List[str] = []
    termos_tag: List[str] = []
    termo_id: int | None = None

    for p in partes:
        if p == "or":
            continue
        if not p:
            continue
        if p.startswith("id:"):
            try:
                termo_id = int(p[3:])
            except ValueError:
                pass
        elif p.startswith("tag:"):
            termos_tag.append(p[4:])
        elif p.startswith("-"):
            termos_not.append(p[1:])
        elif "or" in p:
            termos_or.extend([x for x in p.split("or") if x])
        else:
            termos_normais.append(p)

    termos_expandidos: Dict[str, List[str]] = {}
    for t in termos_normais:
        lista: List[str] = [t]
        if t in BASE_SINONIMOS:
            lista.extend(BASE_SINONIMOS[t])
        termos_expandidos[t] = lista

    termos_para_scoring: List[str] = []
    for lista in termos_expandidos.values():
        termos_para_scoring.extend(lista)

    def relevancia(ex: Dict[str, Any]) -> int:
        """Calcula relevância simples para a pesquisa antiga."""
        score = 0
        titulo_pt = ex["titulo_pt"].lower()
        titulo_en = ex["titulo_en"].lower()
        tags = ex["tags"]
        tags_txt = " ".join(tags).lower()

        for t in termos_para_scoring + termos_or + termos_tag:
            if t in titulo_pt:
                score += 3
            if t in titulo_en:
                score += 2
            if t in tags_txt:
                score += 1

        tema_ex = descobrir_tema(tags + titulo_pt.split() + titulo_en.split())
        tema_pesq = descobrir_tema(termos_para_scoring)

        if tema_ex and tema_pesq:
            score += 5 if tema_ex == tema_pesq else 2

        return score

    resultados: List[Dict[str, Any]] = []

    for ex in exercicios:
        tags = ex["tags"]
        texto = f"{ex['titulo_pt'].lower()} {ex['titulo_en'].lower()} {' '.join(tags).lower()}"
        palavras = texto.split()

        def termo_encontrado(t: str) -> bool:
            """Verifica se um termo aparece no texto do exercício."""
            return t in texto or any(p.startswith(t) for p in palavras)

        if termo_id is not None and ex["id"] != termo_id:
            continue

        if not all(any(termo_encontrado(alt) for alt in termos_expandidos[t]) for t in termos_expandidos):
            continue

        if termos_or and not any(termo_encontrado(t) for t in termos_or):
            continue

        if any(termo_encontrado(t) for t in termos_not):
            continue

        if termos_tag:
            tags_lower = [t.lower() for t in tags]
            if not all(any(tag.startswith(t) or t in tag for tag in tags_lower) for t in termos_tag):
                continue

        resultados.append(ex)

    resultados.sort(key=relevancia, reverse=True)
    return resultados

# ============================================================
#  FUNÇÃO DE PESQUISA INTELIGENTE
# ============================================================

def pesquisar_inteligente(
    termo: str,
    indice_termos: Dict[str, Set[int]],
    exercicios: List[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    """
    Pesquisa avançada com:
    - expansão semântica (sinónimos, variações, inferências)
    - interpretação de intenção (ação, objeto, objetivo)
    - temas automáticos
    - similaridade semântica leve
    - pesos inteligentes
    - ranking avançado

    Parâmetros:
        termo (str): Termo de pesquisa do utilizador.
        indice_termos (dict): Índice invertido de termos → IDs de exercícios.
        exercicios (list): Lista completa de exercícios.

    Retorna:
        list: Lista ordenada de exercícios relevantes.
    """

    termo = termo.lower().strip()

    # 1) Expansão semântica
    termos_expandidos = expandir_frase(termo, SINONIMOS_EXPANDIDO)
    for t in list(termos_expandidos):
        termos_expandidos.update(gerar_variacoes(t))

    # 2) Intenção
    intencao = extrair_intencao(termo)
    acao = intencao["acao"]
    objeto = intencao["objeto"]
    objetivo = intencao["objetivo"]

    # 3) Matches no índice
    contador_matches: Dict[int, int] = {}
    for t in termos_expandidos:
        if t in indice_termos:
            for ex_id in indice_termos[t]:
                contador_matches[ex_id] = contador_matches.get(ex_id, 0) + 1

    mapa_ex = {ex["id"]: ex for ex in exercicios}

    # 4) Relevância avançada
    def relevancia(ex_id: int) -> int:
        """
        Calcula o score de relevância avançado para um exercício,
        combinando:
        - frequência no índice
        - matches no título PT/EN
        - matches nas tags
        - tema
        - intenção (ação/objeto/objetivo)
        - similaridade semântica
        - penalizações
        """
        ex = mapa_ex[ex_id]
        score = 0

        titulo_pt = ex["titulo_pt"].lower()
        titulo_en = ex["titulo_en"].lower()
        tags = [t.lower() for t in ex["tags"]]

        termos_genericos = {"lista", "número", "numeros", "texto", "string", "valor"}

        # A) Frequência no índice
        freq = contador_matches.get(ex_id, 0)
        score += freq * 4

        # B) Título PT
        for t in termos_expandidos:
            if t in titulo_pt:
                base = 12
                if t in termos_genericos:
                    base = 4
                if titulo_pt.startswith(t):
                    base += 4
                score += base

        # C) Título EN
        for t in termos_expandidos:
            if t in titulo_en:
                base = 8
                if t in termos_genericos:
                    base = 3
                score += base

        # D) Tags
        for t in termos_expandidos:
            if any(t in tag for tag in tags):
                base = 10
                if t in termos_genericos:
                    base = 4
                score += base

        # E) Tema
        tema_ex = descobrir_tema(tags + titulo_pt.split() + titulo_en.split())
        tema_pesq = descobrir_tema(list(termos_expandidos))
        if tema_ex and tema_pesq:
            score += 15 if tema_ex == tema_pesq else 5

        # F) Intenção: ação
        if acao:
            if acao in titulo_pt or acao in titulo_en or any(acao in tag for tag in tags):
                score += 15

        # G) Intenção: objeto
        if objeto:
            if objeto in titulo_pt or objeto in titulo_en or any(objeto in tag for tag in tags):
                score += 12

        # H) Intenção: objetivo
        if objetivo:
            for palavra in objetivo.split():
                if palavra in titulo_pt or palavra in titulo_en or any(palavra in tag for tag in tags):
                    score += 6

        # I) Similaridade semântica leve
        for t in termos_expandidos:
            for palavra in titulo_pt.split():
                sim = similaridade_semantica(t, palavra)
                if sim >= 0.6:
                    score += int(sim * 10)

            for palavra in titulo_en.split():
                sim = similaridade_semantica(t, palavra)
                if sim >= 0.6:
                    score += int(sim * 8)

            for tag in tags:
                sim = similaridade_semantica(t, tag)
                if sim >= 0.6:
                    score += int(sim * 12)

        # J) Penalizações leves (falsos positivos)
        if freq == 0:
            score -= 5
        if not tema_ex and tema_pesq:
            score -= 3

        return score

    if not contador_matches:
        return []

    ids_ordenados = sorted(contador_matches, key=relevancia, reverse=True)
    return [mapa_ex[i] for i in ids_ordenados]