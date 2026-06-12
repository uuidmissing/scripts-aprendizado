#!/usr/bin/env python3

################################################################################
#                   FUNDAMENTOS PYTHON - GUIA COMPLETO
#
# Este arquivo consolida conceitos sobre:
# - Listas e dicionários
# - Manipulação com input do usuário
# - Loops e iteração
# - Estrutura de pacotes (__init__.py)
# - Exceções (try/except)
# - Função principal (__main__)
# - Modificação de sys.path
################################################################################


###############################################################################
# 📘 PARTE 1: CONCEITOS FUNDAMENTAIS
###############################################################################

"""
╔════════════════════════════════════════════════════════════════╗
║              FUNDAMENTOS PYTHON - CONCEITOS                   ║
╚════════════════════════════════════════════════════════════════╝
"""

CONCEITOS = """

═══════════════════════════════════════════════════════════════════
1. LISTAS E DICIONÁRIOS
═══════════════════════════════════════════════════════════════════

LISTA (array):
    lista = [1, 2, 3, 4, 5]
    lista.append(6)      → Adiciona ao final
    lista.remove(3)      → Remove elemento específico
    lista.pop()          → Remove e retorna último
    lista[0]             → Acessa índice 0
    len(lista)           → Tamanho da lista
    
LISTA DE DICIONÁRIOS (estrutura de dados):
    pessoas = [
        {'nome': 'Alice', 'idade': 25},
        {'nome': 'Bob', 'idade': 30}
    ]
    
DICIONÁRIO (key-value):
    pessoa = {'nome': 'Alice', 'idade': 25}
    pessoa['nome']       → Acessa valor
    pessoa['cidade'] = 'SP'  → Adiciona novo par
    del pessoa['idade']  → Remove chave
    pessoa.keys()        → Todas as chaves
    pessoa.values()      → Todos os valores
    pessoa.items()       → Pares (chave, valor)

═══════════════════════════════════════════════════════════════════
2. LOOPS E ITERAÇÃO
═══════════════════════════════════════════════════════════════════

FOR com índice:
    for i in range(5):
        print(i)  # 0, 1, 2, 3, 4

FOR com elemento:
    for item in lista:
        print(item)

FOR com enumerate (índice + elemento):
    for idx, item in enumerate(lista):
        print(f"Índice {idx}: {item}")

FOR com dicionário:
    for chave in dicionario:
        print(dicionario[chave])
    
    for chave, valor in dicionario.items():
        print(f"{chave}: {valor}")

WHILE:
    while condicao:
        # código
        if alguma_condicao:
            break

═══════════════════════════════════════════════════════════════════
3. ENTRADA DO USUÁRIO (input)
═══════════════════════════════════════════════════════════════════

input() retorna string SEMPRE:
    idade_str = input("Digite sua idade: ")
    
Converter para tipo correto:
    idade = int(idade_str)          # Para inteiro
    preco = float(entrada)           # Para float
    booleano = entrada.lower() == 'sim'  # Para booleano

VALIDAÇÃO com try/except:
    try:
        idade = int(input("Idade: "))
        if 0 <= idade <= 120:
            print("Idade válida")
        else:
            print("Idade fora do intervalo")
    except ValueError:
        print("Entrada deve ser um número")

═══════════════════════════════════════════════════════════════════
4. FUNÇÕES len(), set(), UNION()
═══════════════════════════════════════════════════════════════════

len() - comprimento:
    len("hello")  → 5
    len([1,2,3]) → 3
    len({'a':1}) → 1 (número de chaves)

set() - conjunto único (sem duplicatas):
    set([1, 1, 2, 3, 3])  → {1, 2, 3}
    
set().union() - combinar conjuntos:
    dicts = [{'a': 1}, {'a': 2, 'b': 3}, {'c': 4}]
    chaves_todas = set().union(*(d.keys() for d in dicts))
    # Resultado: {'a', 'b', 'c'}

═══════════════════════════════════════════════════════════════════
5. PACOTES E MÓDULOS (__init__.py)
═══════════════════════════════════════════════════════════════════

Estrutura de pacote:
    meu_projeto/
    ├── main.py
    ├── meupacote/
    │   ├── __init__.py     ← Arquivo especial
    │   ├── funcoes.py
    │   └── utilitarios.py

Para importar:
    from meupacote import funcoes
    from meupacote.funcoes import minha_funcao

sem __init__.py, Python não reconhece como pacote!

═══════════════════════════════════════════════════════════════════
6. FUNÇÃO __main__
═══════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    main()

Significa:
- Se o arquivo é executado DIRETAMENTE: executa o código
- Se o arquivo é IMPORTADO: não executa o código

Permite reutilizar funções em outros scripts!

═══════════════════════════════════════════════════════════════════
7. MODIFICANDO sys.path
═══════════════════════════════════════════════════════════════════

sys.path é uma lista de diretórios onde Python procura módulos.

import sys
sys.path.insert(0, './libs')  # Adiciona libs no início da busca

Permite importar módulos de diretórios locais customizados.

═══════════════════════════════════════════════════════════════════
"""

print(CONCEITOS)


###############################################################################
# 📝 PARTE 2: EXEMPLOS PRÁTICOS
###############################################################################

print("\n" + "="*73)
print("EXEMPLOS PRÁTICOS - FUNDAMENTOS PYTHON")
print("="*73)

# --- EXEMPLO 1: Listas de dicionários ---
print("\n🔹 EXEMPLO 1: Listas de dicionários")
print("-" * 73)

# Representando "tabelas" de dados
locais = [
    {'tipo': "Apartamento", 'rua': "Catarolas", 'numero': "345"},
    {'tipo': "Residência", 'rua': "Miramar", 'numero': "67"},
    {'tipo': "Comércio", 'rua': "Av. Paulista", 'numero': "1000"}
]

print(f"Total de locais: {len(locais)}")
print("\nMostrando todos os locais:")
for i, local in enumerate(locais):
    print(f"\n  Local {i}:")
    for chave, valor in local.items():
        print(f"    {chave}: {valor}")


# --- EXEMPLO 2: Encontrar todas as chaves únicas ---
print("\n\n🔹 EXEMPLO 2: Encontrar chaves únicas com set().union()")
print("-" * 73)

# Extrair todas as chaves únicas de uma lista de dicionários
chaves_unicas = set().union(*(local.keys() for local in locais))
print(f"Chaves encontradas em todos os locais: {sorted(chaves_unicas)}")


# --- EXEMPLO 3: Dicionários com operações ---
print("\n\n🔹 EXEMPLO 3: Operações com dicionários")
print("-" * 73)

pessoa = {'nome': 'Alice', 'idade': 25}
print(f"Dicionário inicial: {pessoa}")

# Adicionar
pessoa['cidade'] = 'São Paulo'
pessoa['profissao'] = 'Engenheira'
print(f"Após adicionar: {pessoa}")

# Remover
del pessoa['profissao']
print(f"Após remover 'profissao': {pessoa}")

# Iterar
print("\nIterando:")
for chave, valor in pessoa.items():
    print(f"  {chave}: {valor}")


# --- EXEMPLO 4: Validação com try/except ---
print("\n\n🔹 EXEMPLO 4: Entrada com validação")
print("-" * 73)

def entrada_validada(prompt, tipo=int, min_val=None, max_val=None):
    """Pede entrada até o usuário digitar corretamente"""
    while True:
        try:
            entrada = input(prompt)
            valor = tipo(entrada)
            
            if min_val is not None and valor < min_val:
                print(f"  Erro: deve ser no mínimo {min_val}")
                continue
            if max_val is not None and valor > max_val:
                print(f"  Erro: deve ser no máximo {max_val}")
                continue
                
            return valor
        except ValueError:
            print(f"  Erro: entrada inválida. Digite um {tipo.__name__}")

# Simular entrada (em programa real seria descomentado)
# idade = entrada_validada("Digite sua idade (0-120): ", int, 0, 120)
print("(Função entrada_validada definida - usável em scripts interativos)")


# --- EXEMPLO 5: Trabalhar com len() ---
print("\n\n🔹 EXEMPLO 5: Usando len()")
print("-" * 73)

strings = ["gato", "cachorro", "pássaro"]
numeros = [10, 20, 30, 40, 50]
dicionario = {'a': 1, 'b': 2, 'c': 3}

print(f"Comprimento de 'pássaro': {len('pássaro')}")
print(f"Elementos em {strings}: {len(strings)}")
print(f"Elementos em {numeros}: {len(numeros)}")
print(f"Chaves em {dicionario}: {len(dicionario)}")

print(f"\nÚltimo índice válido de {strings}: {len(strings) - 1}")
print(f"  (indices vão de 0 até {len(strings) - 1})")


# --- EXEMPLO 6: Dividir lista com range ---
print("\n\n🔹 EXEMPLO 6: Iterar com range")
print("-" * 73)

print("De 0 a 4:")
for i in range(5):
    print(f"  {i}")

print("\nDe 2 a 8 com step 2:")
for i in range(2, 9, 2):
    print(f"  {i}")

print("\nReverso (5 a 0):")
for i in range(5, -1, -1):
    print(f"  {i}")


# --- EXEMPLO 7: List comprehension ---
print("\n\n🔹 EXEMPLO 7: List comprehension")
print("-" * 73)

# Forma tradicional
quadrados_tradicional = []
for i in range(5):
    quadrados_tradicional.append(i ** 2)

# List comprehension
quadrados_compacto = [i ** 2 for i in range(5)]

print(f"Forma tradicional: {quadrados_tradicional}")
print(f"List comprehension: {quadrados_compacto}")

# Com condição
pares = [i for i in range(10) if i % 2 == 0]
print(f"Números pares de 0 a 9: {pares}")


# --- EXEMPLO 8: Ordenar e manipular lista ---
print("\n\n🔹 EXEMPLO 8: Ordenar e manipular")
print("-" * 73)

numeros_desordenados = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original: {numeros_desordenados}")

# sorted() retorna nova lista
ordenado = sorted(numeros_desordenados)
print(f"Ordenado: {ordenado}")

# Remover duplicatas com set
unicos = sorted(set(numeros_desordenados))
print(f"Sem duplicatas: {unicos}")

# Reverso
reverso = sorted(numeros_desordenados, reverse=True)
print(f"Reverso: {reverso}")


# --- EXEMPLO 9: Conversão de tipos ---
print("\n\n🔹 EXEMPLO 9: Conversão de tipos")
print("-" * 73)

entrada_str = "123"
numero_int = int(entrada_str)
numero_float = float(entrada_str)
numero_str_novamente = str(numero_int)

print(f"'{entrada_str}' (string) → {numero_int} (int) → {numero_float} (float)")
print(f"De volta para string: '{numero_str_novamente}'")

# Booleano
print(f"\nbool(''): {bool('')}")          # False
print(f"bool('texto'): {bool('texto')}")  # True
print(f"bool(0): {bool(0)}")              # False
print(f"bool(1): {bool(1)}")              # True
print(f"bool([]): {bool([])}")            # False
print(f"bool([1]): {bool([1])}")          # True


# --- EXEMPLO 10: Funções reutilizáveis ---
print("\n\n🔹 EXEMPLO 10: Funções para reutilização")
print("-" * 73)

def encontrar_chaves_unicas(lista_dicts):
    """Encontra todas as chaves únicas em lista de dicionários"""
    return sorted(set().union(*(d.keys() for d in lista_dicts)))

def adicionar_item(lista, item):
    """Adiciona item à lista e retorna a lista"""
    lista.append(item)
    return lista

def remover_item(lista, item):
    """Remove item da lista se existir"""
    if item in lista:
        lista.remove(item)
    return lista

# Usando as funções
dados = [
    {'id': 1, 'nome': 'Alice'},
    {'id': 2, 'nome': 'Bob', 'email': 'bob@mail.com'},
    {'id': 3, 'idade': 25}
]

print(f"Chaves únicas nos dados: {encontrar_chaves_unicas(dados)}")

numeros = [1, 2, 3]
print(f"Lista: {numeros}")
print(f"Após adicionar 4: {adicionar_item(numeros, 4)}")
print(f"Após remover 2: {remover_item(numeros, 2)}")


###############################################################################
# 🔧 PARTE 3: ESTRUTURA DE PACOTES
###############################################################################

print("\n\n" + "="*73)
print("ESTRUTURA DE PACOTES (__init__.py)")
print("="*73)

ESTRUTURA_INFO = """

Exemplo de estrutura:
────────────────────
meu_projeto/
├── main.py              ← Script principal
├── meupacote/           ← Diretório do pacote
│   ├── __init__.py      ← Indica que é um pacote Python
│   ├── funcoes.py
│   ├── utilitarios.py
│   └── subpacote/
│       ├── __init__.py
│       └── ferramentas.py

Para importar:
──────────────
from meupacote import funcoes
from meupacote.funcoes import minha_funcao
from meupacote.subpacote.ferramentas import ferramenta_x

Conteúdo do __init__.py (pode estar vazio ou ter inicialização):
─────────────────────────────────────────────────────────────────
# __init__.py vazio (apenas marca como pacote)
# Ou:
from .funcoes import minha_funcao
from .utilitarios import *

# Agora em main.py:
from meupacote import minha_funcao  # Importa diretamente!

"""

print(ESTRUTURA_INFO)


###############################################################################
# 📊 PARTE 4: TABELA DE REFERÊNCIA
###############################################################################

print("\n" + "="*73)
print("TABELA DE REFERÊNCIA")
print("="*73 + "\n")

TABELA = """
┌────────────────────────┬──────────────────┬─────────────────────────┐
│ Operação               │ Sintaxe           │ Exemplo                 │
├────────────────────────┼──────────────────┼─────────────────────────┤
│ Criar lista            │ [...]             │ lista = [1, 2, 3]       │
│ Criar dicionário       │ {...}             │ dic = {'a': 1}          │
│ Acessar elemento       │ list[índice]      │ lista[0]                │
│ Acessar valor          │ dic[chave]        │ dic['a']                │
│ Comprimento            │ len(...)          │ len(lista)              │
│                        │                   │                         │
│ Adicionar elemento     │ list.append(x)    │ lista.append(4)         │
│ Remover elemento       │ list.remove(x)    │ lista.remove(2)         │
│ Remover e retornar     │ list.pop()        │ x = lista.pop()         │
│                        │                   │                         │
│ For com elemento       │ for x in list     │ for item in lista:      │
│ For com índice         │ for i in range    │ for i in range(len(l))  │
│ For com índice+elem    │ enumerate()       │ for i,v in enum(l):     │
│ For em dicionário      │ for k, v in d...  │ for k,v in dic.items(): │
│                        │                   │                         │
│ Converter para int     │ int(x)            │ int("123")              │
│ Converter para float   │ float(x)          │ float("3.14")           │
│ Converter para string  │ str(x)            │ str(123)                │
│ Converter para bool    │ bool(x)           │ bool("sim")             │
│                        │                   │                         │
│ Entrada do usuário     │ input(prompt)     │ x = input("Digite: ")   │
│ Tratar exceção         │ try/except        │ try:                    │
│                        │                   │     x = int(input())    │
│                        │                   │ except ValueError:      │
│                        │                   │     print("erro")       │
│                        │                   │                         │
│ Chaves únicas          │ set().union(...)  │ set().union(*(d.keys()) │
│ Ordenar                │ sorted(...)       │ sorted(lista)           │
│ Reverso                │ reversed/[::-1]   │ lista[::-1]             │
│ List comprehension     │ [x for x in ...]  │ [i*2 for i in range(5)] │
│                        │                   │                         │
│ Importar módulo        │ import módulo     │ import sys              │
│ Importar de pacote     │ from pac import x │ from lib import func    │
│ __main__               │ if __name__ ==    │ if __name__ ==          │
│                        │     "__main__"    │     "__main__":         │
│                        │                   │                         │
└────────────────────────┴──────────────────┴─────────────────────────┘
"""

print(TABELA)

print("\n" + "="*73)
print("✅ Script de exemplos finalizado!")
print("="*73)

# Permitir que o arquivo seja importado sem executar tudo
if __name__ == "__main__":
    print("\n✓ Execute exemplos específicos importando este arquivo em outro script")
