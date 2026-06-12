#!/usr/bin/env python3

################################################################################
#                   ENUMERAÇÃO DE SUBDOMÍNIOS - GUIA COMPLETO
#
# Este arquivo consolida exemplos sobre:
# - Brute force básico de subdomínios
# - Requisições HTTP com tratamento de exceções
# - Listas de palavras comuns
# - Verificação de disponibilidade
# - Timeout e tratamento de erros
# - Variações e melhorias
################################################################################

import requests
import sys
from typing import List, Tuple

###############################################################################
# 📘 PARTE 1: CONCEITOS FUNDAMENTAIS
###############################################################################

CONCEITOS = """
╔════════════════════════════════════════════════════════════════╗
║          ENUMERAÇÃO DE SUBDOMÍNIOS - CONCEITOS                ║
╚════════════════════════════════════════════════════════════════╝

═══════════════════════════════════════════════════════════════════
1. O QUE É ENUMERAÇÃO DE SUBDOMÍNIOS?
═══════════════════════════════════════════════════════════════════

Descobrir subdomínios de um domínio através de força bruta.

Exemplos:
    Domínio: example.com
    Subdomínios possíveis:
        admin.example.com
        mail.example.com
        app.example.com
        api.example.com
        ...

Técnica: Tentar palavras comuns com o domínio até encontrar os que
existem (aqueles que responderm HTTP).

═══════════════════════════════════════════════════════════════════
2. LISTA DE PALAVRAS COMUNS
═══════════════════════════════════════════════════════════════════

Subdomínios que costumam existir:
    admin, api, app, beta, blog, cdn, cms, cp, dashboard,
    dev, ftp, git, gitlab, grafana, help, home, jenkins,
    login, mail, media, old, phpmyadmin, proxy, qa, shop,
    staging, status, support, test, webmail, www, ...

Lista pode ser:
- Hardcoded no script
- Lido de arquivo
- Obtido de APIs (SecLists, projetos OSINT)

═══════════════════════════════════════════════════════════════════
3. CONSTRUIR URL DE SUBDOMÍNIO
═══════════════════════════════════════════════════════════════════

Padrão:
    f"https://{palavra}.{domínio}"

Exemplo:
    palavra = "admin"
    dominio = "example.com"
    subdominio = f"https://{palavra}.{dominio}"
    # Resultado: https://admin.example.com

═══════════════════════════════════════════════════════════════════
4. VERIFICAR SE SUBDOMÍNIO EXISTE
═══════════════════════════════════════════════════════════════════

Fazer requisição e capturar resultado:

try:
    response = requests.get(url, timeout=5)
    print(f"✓ {url} existe")  # Respondeu com sucesso
    
except requests.ConnectionError:
    print(f"✗ {url} não respondeu")
except requests.Timeout:
    print(f"✗ {url} timeout")

═══════════════════════════════════════════════════════════════════
5. EXCEÇÕES E TRATAMENTO
═══════════════════════════════════════════════════════════════════

requests.ConnectionError   → DNS não resolveu ou conexão recusada
requests.Timeout           → URL não respondeu no prazo
requests.RequestException  → Exceção geral de requisição
Exception                  → Qualquer outra exceção

═══════════════════════════════════════════════════════════════════
6. MELHORIAS POSSÍVEIS
═══════════════════════════════════════════════════════════════════

- Usar wordlist de arquivo para maior cobertura
- Validar com DNS lookup (socket, dnspython)
- Verificar redirecionamentos
- Armazenar resultados em arquivo
- Paralelizar com threading/asyncio (mais rápido)
- Usar APIs públicas (Shodan, VirusTotal)

═══════════════════════════════════════════════════════════════════
"""

print(CONCEITOS)


###############################################################################
# 📝 PARTE 2: EXEMPLOS PRÁTICOS
###############################################################################

print("\\n" + "="*73)
print("EXEMPLOS PRÁTICOS - ENUMERAÇÃO DE SUBDOMÍNIOS")
print("="*73)

# Lista padrão de palavras comuns
PALAVRAS_PADRAO = [
    "admin", "api", "app", "beta", "blog", "cdn", "cms", "dashboard",
    "dev", "ftp", "git", "help", "home", "mail", "news", "proxy",
    "staging", "status", "support", "test", "webmail", "www"
]


# --- EXEMPLO 1: Enumeração simples ---
print("\\n🔹 EXEMPLO 1: Enumeração simples")
print("-" * 73)

def enumerar_subdomínios_simples(domínio: str, palavras: List[str]) -> List[str]:
    """Tenta encontrar subdomínios que existem"""
    encontrados = []
    
    print(f"\\nTestando subdomínios de {domínio}:")
    
    for palavra in palavras:
        url = f"https://{palavra}.{domínio}"
        
        try:
            response = requests.get(url, timeout=5)
            print(f"  ✓ {url}")
            encontrados.append(url)
            
        except requests.RequestException:
            print(f"  ✗ {url}")
    
    return encontrados

# Exemplo com domínio real
print("Enumerando subdomínios de 'example.com' (primeiras 5 palavras):")
resultado = enumerar_subdomínios_simples("example.com", PALAVRAS_PADRAO[:5])
print(f"\\nEncontrados: {len(resultado)} subdomínios")


# --- EXEMPLO 2: Com informações adicionais ---
print("\\n\\n🔹 EXEMPLO 2: Enumeração com detalhes")
print("-" * 73)

def enumerar_com_detalhes(domínio: str, palavras: List[str]) -> List[Tuple[str, int, bool]]:
    """Enumera e retorna (url, status_code, existe)"""
    resultados = []
    
    print(f"\\nEnumerando {domínio}...")
    
    for palavra in palavras:
        url = f"https://{palavra}.{domínio}"
        
        try:
            response = requests.get(url, timeout=5)
            existe = response.status_code < 400
            status = "✓" if existe else "?"
            print(f"  {status} {url:<40} ({response.status_code})")
            resultados.append((url, response.status_code, existe))
            
        except requests.Timeout:
            print(f"  ? {url:<40} (TIMEOUT)")
            resultados.append((url, None, False))
        except requests.ConnectionError:
            print(f"  ✗ {url:<40} (SEM CONEXÃO)")
            resultados.append((url, None, False))
        except Exception as e:
            print(f"  ✗ {url:<40} ({type(e).__name__})")
            resultados.append((url, None, False))
    
    return resultados

# Testar
resultado = enumerar_com_detalhes("example.com", PALAVRAS_PADRAO[:7])
print(f"\\nResultado: {sum(1 for _, _, existe in resultado if existe)} subdomínios encontrados")


# --- EXEMPLO 3: Salvar resultados em arquivo ---
print("\\n\\n🔹 EXEMPLO 3: Salvar resultados")
print("-" * 73)

def enumerar_e_salvar(domínio: str, palavras: List[str], arquivo_saida: str = "subdomínios.txt"):
    """Enumera subdomínios e salva em arquivo"""
    encontrados = []
    
    print(f"Enumerando {domínio}...\\n")
    
    for palavra in palavras:
        url = f"https://{palavra}.{domínio}"
        
        try:
            response = requests.get(url, timeout=5)
            if response.status_code < 400:
                encontrados.append(url)
                print(f"  ✓ {url}")
        except requests.RequestException:
            pass
    
    # Salvar em arquivo
    if encontrados:
        with open(arquivo_saida, 'w') as f:
            for url in encontrados:
                f.write(f"{url}\\n")
        print(f"\\n✓ {len(encontrados)} subdomínios salvos em '{arquivo_saida}'")
    else:
        print(f"\\n✗ Nenhum subdomínio encontrado")
    
    return encontrados

# Demonstração (comentada para não criar arquivo)
# enumerar_e_salvar("example.com", PALAVRAS_PADRAO[:10], "/tmp/subs.txt")
print("(Função definida - usável em scripts)")


# --- EXEMPLO 4: Com diferentes timeouts ---
print("\\n\\n🔹 EXEMPLO 4: Ajustando timeout")
print("-" * 73)

def enumerar_com_timeout_ajustavel(domínio: str, palavras: List[str], timeout: int = 5):
    """Permite ajustar timeout (quanto maior, mais tempo espera)"""
    
    print(f"Enumerando {domínio} (timeout: {timeout}s)...\\n")
    
    encontrados = []
    timeouts = 0
    erros = 0
    
    for palavra in palavras:
        url = f"https://{palavra}.{domínio}"
        
        try:
            response = requests.get(url, timeout=timeout)
            if response.status_code < 400:
                print(f"  ✓ {url}")
                encontrados.append(url)
                
        except requests.Timeout:
            timeouts += 1
        except requests.ConnectionError:
            erros += 1
        except Exception:
            pass
    
    print(f"\\nResumo:")
    print(f"  Encontrados: {len(encontrados)}")
    print(f"  Timeouts: {timeouts}")
    print(f"  Erros de conexão: {erros}")
    
    return encontrados

resultado = enumerar_com_timeout_ajustavel("example.com", PALAVRAS_PADRAO[:10], timeout=3)


# --- EXEMPLO 5: Palavras customizadas ---
print("\\n\\n🔹 EXEMPLO 5: Usando lista customizada de palavras")
print("-" * 73)

def enumerar_customizado(domínio: str, palavras: List[str]):
    """Enumera com lista de palavras customizada"""
    
    print(f"Enumerando {domínio}:")
    print(f"Testando {len(palavras)} palavras...\\n")
    
    encontrados = []
    
    for i, palavra in enumerate(palavras, 1):
        url = f"https://{palavra}.{domínio}"
        
        try:
            response = requests.get(url, timeout=5)
            print(f"  [{i}/{len(palavras)}] ✓ {palavra}")
            encontrados.append(palavra)
        except:
            print(f"  [{i}/{len(palavras)}] ✗ {palavra}")
    
    return encontrados

# Palavras específicas para teste
palavras_segurança = ["admin", "phpmyadmin", "cpanel", "test", "debug"]
print("Testando subdomínios comuns em segurança:")
resultado = enumerar_customizado("example.com", palavras_segurança)


# --- EXEMPLO 6: Validar subdomínios com DNS ---
print("\\n\\n🔹 EXEMPLO 6: Conceito de validação com DNS (teórico)")
print("-" * 73)

print("""
Para validação mais confiável com DNS, seria necessário:

import socket

def verificar_dns(subdominio):
    try:
        ip = socket.gethostbyname(subdominio)
        return True, ip
    except socket.gaierror:
        return False, None

Exemplo:
    existe, ip = verificar_dns("google.com")
    if existe:
        print(f"Domínio resolvido para: {ip}")
    else:
        print("Domínio não existe no DNS")
""")


###############################################################################
# 🔧 PARTE 3: FUNÇÃO COMPLETA
###############################################################################

print("\\n" + "="*73)
print("FUNÇÃO COMPLETA - Enumerador de Subdomínios")
print("="*73 + "\\n")

def enumerador_completo(domínio: str = None, arquivo_palavras: str = None):
    """
    Enumerador de subdomínios completo.
    
    Uso:
        python3 script.py example.com
        python3 script.py example.com -w palavras.txt
    """
    
    if not domínio:
        if len(sys.argv) > 1:
            domínio = sys.argv[1]
        else:
            print("Uso: python3 script.py <domínio>")
            print("Exemplo: python3 script.py example.com")
            return
    
    # Usar palavras padrão ou arquivo
    if arquivo_palavras:
        try:
            with open(arquivo_palavras, 'r') as f:
                palavras = [linha.strip() for linha in f if linha.strip()]
        except FileNotFoundError:
            print(f"Arquivo não encontrado: {arquivo_palavras}")
            palavras = PALAVRAS_PADRAO
    else:
        palavras = PALAVRAS_PADRAO
    
    print(f"Enumerando subdomínios de: {domínio}")
    print(f"Testando {len(palavras)} palavras...\\n")
    
    encontrados = []
    
    for i, palavra in enumerate(palavras, 1):
        url = f"https://{palavra}.{domínio}"
        
        try:
            response = requests.get(url, timeout=5)
            print(f"  [{i:3d}/{len(palavras)}] ✓ {url:<50} ({response.status_code})")
            encontrados.append((url, response.status_code))
        except requests.Timeout:
            print(f"  [{i:3d}/{len(palavras)}] ? {url:<50} (TIMEOUT)")
        except requests.ConnectionError:
            print(f"  [{i:3d}/{len(palavras)}] ✗ {url:<50} (sem conexão)")
        except Exception as e:
            print(f"  [{i:3d}/{len(palavras)}] ✗ {url:<50} ({type(e).__name__})")
    
    print(f"\\n{'='*73}")
    print(f"Resultado: {len(encontrados)} subdomínios encontrados")
    
    if encontrados:
        print(f"\\nSubdomínios descobertos:")
        for url, status in encontrados:
            print(f"  • {url}")

# Exemplo de uso (comentado)
# enumerador_completo("example.com")


###############################################################################
# 📊 PARTE 4: TABELA DE REFERÊNCIA
###############################################################################

print("\\n" + "="*73)
print("TABELA DE REFERÊNCIA")
print("="*73 + "\\n")

TABELA = """
┌──────────────────────────┬──────────────────┬───────────────────────────┐
│ Operação                 │ Sintaxe           │ Exemplo                   │
├──────────────────────────┼──────────────────┼───────────────────────────┤
│ Construir URL            │ f"https://{sub}" │ f"https://{palavra}.{dom}"│
│ Fazer requisição         │ requests.get()    │ r = requests.get(url)     │
│ Com timeout              │ timeout=N         │ requests.get(url, t=5)    │
│                          │                   │                           │
│ Verificar status         │ r.status_code     │ if r.status_code < 400:   │
│ Existe? (aprox)          │ status < 400      │ if r.status_code < 400:   │
│ Não existe               │ status >= 400     │ if r.status_code >= 400:  │
│                          │                   │                           │
│ Erro de conexão          │ ConnectionError   │ except Connection Error:  │
│ Timeout                  │ Timeout           │ except requests.Timeout:  │
│ Exceção genérica         │ RequestException  │ except RequestException:  │
│                          │                   │                           │
│ Loop com enumerate       │ for i, v in enum  │ for i, p in enumerate(pal)│
│ Loop simples             │ for x in lista    │ for palavra in PALAVRAS:  │
│ Verificar lista          │ len(lista)        │ len(PALAVRAS_PADRAO)      │
│                          │                   │                           │
│ Adicionar à lista        │ lista.append()    │ encontrados.append(url)   │
│ Ler arquivo              │ open() readlines  │ with open(f) as file:     │
│ Escrever arquivo         │ open() write      │ f.write(linha)            │
│                          │                   │                           │
└──────────────────────────┴──────────────────┴───────────────────────────┘
"""

print(TABELA)

print("\\n" + "="*73)
print("✅ Script finalizado!")
print("="*73)

if __name__ == "__main__":
    # Executar apenas se chamado com argumentos
    if len(sys.argv) > 1:
        enumerador_completo()
