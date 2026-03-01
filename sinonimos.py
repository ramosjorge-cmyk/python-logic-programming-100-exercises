"""
sinonimos.py
------------

Módulo responsável por todo o conhecimento semântico do motor de pesquisa.

Inclui:
- Dicionário base de sinónimos (BASE_SINONIMOS)
- Temas semânticos (TEMAS)
- Geração de variações automáticas
- Expansão inteligente de frases
- Construção do dicionário expandido de sinónimos
- Descoberta automática de tema
- Extração de intenção (ação, objeto, objetivo)
- Similaridade semântica leve

Este módulo não faz pesquisa — apenas fornece conhecimento semântico.
"""

# -*- coding: utf-8 -*-
from __future__ import annotations

import unicodedata
from typing import Dict, List, Set

# ============================================================
# 1) DICIONÁRIO BASE — conceitos principais
# ============================================================

BASE_SINONIMOS: Dict[str, List[str]] = {

    # CICLOS / REPETIÇÃO
    "ciclo": ["loop", "laço", "repetição", "iterar", "for", "while", "ciclos"],
    "loop": ["ciclo", "laço", "repetição", "loops"],
    "iterar": ["percorrer", "loop", "for", "iterar lista"],
    "percorrer": ["iterar", "for", "loop", "percorrer lista"],
    "laço": ["loop", "ciclo"],
    "repetição": ["loop", "ciclo", "while", "for", "repetir"],
    "while": ["ciclo", "loop", "repetição"],
    "for": ["ciclo", "loop", "repetição"],

    # CONTAGEM / CONTADOR
    "contador": ["contagem", "incrementar", "+=", "acumular", "count", "counter"],
    "contagem": ["contador", "incrementar", "contar"],
    "contar": ["contagem", "contador", "incrementar"],
    "incrementar": ["contador", "+=", "somar", "incremento"],
    "decrementar": ["contador", "-=", "regressiva", "decremento"],
    "regressiva": ["decrescente", "countdown"],
    "acumular": ["somar", "total", "somatório"],

    # STRINGS / TEXTO
    "string": ["texto", "frase", "palavra", "caracteres", "str"],
    "texto": ["string", "frase"],
    "caracteres": ["string", "letras"],
    "concatenar": ["juntar", "string", "+", "concat"],
    "separar": ["split", "dividir texto"],
    "juntar": ["concatenar", "join"],
    "substring": ["parte do texto", "subtexto"],

    # MATEMÁTICA
    "soma": ["somar", "adição", "+", "total"],
    "somar": ["soma", "+", "adicionar"],
    "adição": ["soma", "+"],
    "subtração": ["subtrair", "-", "diferença"],
    "multiplicação": ["multiplicar", "*", "produto"],
    "divisão": ["dividir", "/", "quociente"],
    "resto": ["módulo", "%", "mod"],
    "par": ["múltiplo de 2"],
    "ímpar": ["não par"],

    "inteiro": ["int", "número inteiro"],
    "decimal": ["float", "real"],
    "real": ["float"],

    # LISTAS / ARRAYS
    "lista": ["array", "vetor", "coleção", "sequência", "lista de números", "lista de strings"],
    "vetor": ["lista", "array"],
    "adicionar": ["append", "inserir"],
    "remover": ["delete", "pop"],
    "ordenar": ["sort", "ordenar lista"],
    "índice": ["posição"],

    # CONDIÇÕES / LÓGICA
    "condição": ["if", "elif", "else", "comparar", "condicional"],
    "comparar": ["==", "!=", ">", "<", "testar", "verificar"],
    "igual": ["=="],
    "diferente": ["!="],
    "maior": [">"],
    "menor": ["<"],
    "verdadeiro": ["true"],
    "falso": ["false"],
    "não": ["not"],
    "e": ["and"],
    "ou": ["or"],

    # VARIÁVEIS
    "variável": ["nome", "identificador", "var"],
    "atribuir": ["=", "definir", "guardar valor"],
    "trocar": ["swap"],

    # FICHEIROS / I/O
    "ficheiro": ["arquivo", "file"],
    "arquivo": ["ficheiro"],
    "guardar": ["salvar", "save", "write", "guardar ficheiro"],
    "carregar": ["load", "abrir", "ler ficheiro"],
    "ler": ["input", "read"],
    "mostrar": ["print", "exibir", "output"],

    # BOOLEANOS
    "booleano": ["bool", "lógico"],
    "lógico": ["booleano", "bool"],
}

# ============================================================
# 2) TEMAS SEMÂNTICOS
# ============================================================

TEMAS: Dict[str, List[str]] = {
    "ciclos": [
        "for", "while", "loop", "iterar", "repetir", "ciclo", "range"
    ],
    "listas": [
        "lista", "listas", "array", "vetor", "elementos", "percorrer"
    ],
    "strings": [
        "string", "texto", "frase", "caracteres", "separar", "split", "join"
    ],
    "ficheiros": [
        "ficheiro", "ficheiros", "abrir", "ler", "escrever", "guardar"
    ],
    "condicoes": [
        "if", "condição", "comparar", "verificar", "igual", "maior", "menor"
    ],
    "matematica": [
        "somar", "subtrair", "multiplicar", "dividir", "número", "numeros"
    ],
    "ordenacao": [
        "ordenar", "sort", "crescente", "decrescente"
    ],
}

# ============================================================
# 3) VARIAÇÕES AUTOMÁTICAS
# ============================================================

def remover_acentos(s: str) -> str:
    """
    Remove acentos de uma string, preservando apenas caracteres ASCII.
    """
    return ''.join(
        c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn'
    )


def gerar_variacoes(palavra: str) -> Set[str]:
    """
    Gera variações automáticas de uma palavra:
    - sem acentos
    - plural simples
    - erros comuns ('ç' → 'c')
    - trocas 'ão' ↔ 'ao'
    """
    variacoes: Set[str] = set()

    base = palavra.lower()
    sem_acento = remover_acentos(base)

    variacoes.add(base)
    variacoes.add(sem_acento)

    if not base.endswith("s"):
        variacoes.add(base + "s")
        variacoes.add(sem_acento + "s")

    variacoes.add(base.replace("ç", "c"))
    variacoes.add(sem_acento.replace("c", "ç"))

    variacoes.add(base.replace("ao", "ão"))
    variacoes.add(base.replace("ão", "ao"))

    return variacoes

# ============================================================
# 4) EXPANSÃO INTELIGENTE DE FRASES
# ============================================================

def expandir_frase(frase: str, sinonimos: Dict[str, List[str]]) -> Set[str]:
    """
    Expande uma frase em termos semânticos:
    - sinónimos
    - variações automáticas
    - inferências simples ('até' → range, 'igual' → ==)
    """
    tokens = frase.lower().split()
    expandidos: Set[str] = set(tokens)

    for token in tokens:
        if token in sinonimos:
            expandidos.update(sinonimos[token])

    if "até" in tokens:
        expandidos.update(["range", "contador", "incrementar"])

    if "igual" in tokens:
        expandidos.update(["==", "comparar"])

    if "percorrer" in tokens or "cada" in tokens:
        expandidos.update(["for", "iterar"])

    if "somar" in tokens:
        expandidos.update(["+", "soma"])

    return expandidos

# ============================================================
# 5) CONSTRUÇÃO DO DICIONÁRIO FINAL DE SINÓNIMOS
# ============================================================

SINONIMOS_EXPANDIDO: Dict[str, List[str]] = {}

for chave, lista in BASE_SINONIMOS.items():
    grupo = set(lista)
    grupo.add(chave)

    for termo in list(grupo):
        grupo.update(gerar_variacoes(termo))

    for termo in grupo:
        SINONIMOS_EXPANDIDO[termo] = list(grupo)

# ============================================================
# 6) DESCOBRIR TEMA
# ============================================================

def descobrir_tema(palavras: List[str]) -> str | None:
    """
    Determina o tema dominante numa lista de palavras,
    com base no dicionário TEMAS.
    """
    melhor_tema = None
    melhor_score = 0

    for tema, termos in TEMAS.items():
        score = sum(1 for p in palavras if p in termos)
        if score > melhor_score:
            melhor_score = score
            melhor_tema = tema

    return melhor_tema

# ============================================================
# 7) INTERPRETAÇÃO DE INTENÇÃO
# ============================================================

def extrair_intencao(frase: str) -> Dict[str, str | None]:
    """
    Extrai a intenção da frase:
    - ação (ex: 'remover', 'ordenar')
    - objeto (ex: 'lista', 'string')
    - objetivo (resto da frase)
    """
    frase = frase.lower()
    tokens = frase.split()

    acoes = [
        "contar", "somar", "subtrair", "multiplicar", "dividir",
        "separar", "juntar", "remover", "ordenar", "percorrer",
        "converter", "verificar", "comparar", "abrir", "ler"
    ]

    objetos = [
        "lista", "string", "texto", "ficheiro", "número", "numeros",
        "caracteres", "vetor"
    ]

    acao = next((t for t in tokens if t in acoes), None)
    objeto = next((t for t in tokens if t in objetos), None)

    objetivo = None
    if acao and acao in tokens:
        idx = tokens.index(acao)
        objetivo = " ".join(tokens[idx + 1:])
    elif objeto and objeto in tokens:
        idx = tokens.index(objeto)
        objetivo = " ".join(tokens[idx + 1:])

    return {
        "acao": acao,
        "objeto": objeto,
        "objetivo": objetivo.strip() if objetivo else None,
    }

# ============================================================
# 8) SIMILARIDADE SEMÂNTICA LEVE
# ============================================================

def similaridade_semantica(a: str, b: str) -> float:
    """
    Mede a similaridade entre duas palavras usando heurísticas:
    - igualdade
    - prefixos/sufixos
    - radicais
    - caracteres em comum
    - distância aproximada
    """
    a = a.lower()
    b = b.lower()

    if a == b:
        return 1.0

    if a.startswith(b) or b.startswith(a):
        return 0.8
    if a.endswith(b) or b.endswith(a):
        return 0.7

    if a[:3] == b[:3]:
        return 0.6

    inter = set(a) & set(b)
    if len(inter) >= min(len(a), len(b)) * 0.5:
        return 0.5

    dif = sum(1 for x, y in zip(a, b) if x != y)
    dif += abs(len(a) - len(b))

    if dif <= 2:
        return 0.6
    if dif <= 3:
        return 0.4

    return 0.0