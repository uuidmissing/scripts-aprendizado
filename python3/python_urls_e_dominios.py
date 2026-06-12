#!/usr/bin/env python3

################################################################################
#                   VERIFICAÇÃO DE URLs E DOMÍNIOS
#
# Este arquivo consolida exemplos sobre:
# - Requisições HTTP com requests
# - Status codes e verificação de disponibilidade
# - Correção de URLs (adicionar https://)
# - Tratamento de argumentos (sys.argv)
# - Exceções e timeout
# - Processamento em lote de domínios
################################################################################

import requests
import sys

###############################################################################
# 📘 PARTE 1: CONCEITOS FUNDAMENTAIS
###############################################################################

CONCEITOS = """
╔════════════════════════════════════════════════════════════════╗
║      VERIFICAÇÃO DE URLs E DOMÍNIOS - CONCEITOS               ║
╚════════════════════════════════════════════════════════════════╝

═══════════════════════════════════════════════════════════════════
1. REQUISIÇÕES HTTP COM requests
═══════════════════════════════════════════════════════════════════

Importar:
    import requests

Fazer requisição GET:
    response = requests.get("https://exemplo.com")
    
    response.status_code  → Código HTTP (200, 404, 500, etc)
    response.text         → HTML/texto da resposta
    response.headers      → Cabeçalhos HTTP
    response.url          → URL final (após redirecionamentos)

Requisição com timeout:
    response = requests.get(url, timeout=5)
    # Aguarda 5 segundos, depois falha

═══════════════════════════════════════════════════════════════════
2. STATUS CODES HTTP
═══════════════════════════════════════════════════════════════════

Série 2xx - Sucesso:
    200 OK                - Sucesso total
    201 Created           - Recurso criado
    202 Accepted          - Requisição aceita

Série 3xx - Redirecionamento:
    301 Moved Permanently - Redirecionamento permanente
    302 Found             - Redirecionamento temporário
    304 Not Modified      - Não modificado (cache válido)

Série 4xx - Erro do cliente:
    400 Bad Request       - Requisição inválida
    403 Forbidden         - Acesso negado
    404 Not Found         - Página não encontrada

Série 5xx - Erro do servidor:
    500 Internal Error    - Erro genérico do servidor
    502 Bad Gateway       - Gateway inválido
    503 Service Unavailable - Serviço indisponível

═══════════════════════════════════════════════════════════════════
3. ARGUMENTOS DE LINHA DE COMANDO (sys.argv)
═══════════════════════════════════════════════════════════════════

sys.argv é uma lista com:
    sys.argv[0]  → Nome do script
    sys.argv[1]  → 1º argumento
    sys.argv[2]  → 2º argumento
    ...

Exemplo:
    $ python3 script.py google.com github.com
    
    sys.argv[0] = "script.py"
    sys.argv[1] = "google.com"
    sys.argv[2] = "github.com"

Processar argumentos:
    dominios = sys.argv[1:]  # Todos exceto nome do script
    
    # Se separados por vírgula:
    dominios = []
    for arg in sys.argv[1:]:
        dominios.extend(arg.split(","))

═══════════════════════════════════════════════════════════════════
4. TRATAMENTO DE EXCEÇÕES (try/except)
═══════════════════════════════════════════════════════════════════

Exceção genérica:
    try:
        response = requests.get(url)
    except:
        print("Algo deu errado")

Exceção específica:
    try:
        response = requests.get(url, timeout=5)
    except requests.RequestException:
        print("Erro na requisição ou timeout")
    except requests.ConnectionError:
        print("Erro de conexão")

Múltiplas exceções:
    try:
        r = requests.get(url, timeout=5)
        codigo = int(r.status_code)
    except requests.RequestException:
        print("Erro de requisição")
    except ValueError:
        print("Erro ao converter status code")

═══════════════════════════════════════════════════════════════════
5. CORREÇÃO DE URLs
═══════════════════════════════════════════════════════════════════

Problema: URLs podem estar incompletas
    "google.com"      → Sem protocolo
    "http://old.com"  → HTTP inseguro

Solução: Adicionar protocolo automaticamente
    if not url.startswith(("http://", "https://")):
        url = f"https://{url}"

═══════════════════════════════════════════════════════════════════
6. VERIFICAÇÃO DE DISPONIBILIDADE
═══════════════════════════════════════════════════════════════════

Códigos considerados "ativos":
    ATIVOS = [200, 201, 202, 301, 302, 403]
    
    if status_code in ATIVOS:
        print("Domínio ativo")
    else:
        print("Domínio inativo ou bloqueado")

═══════════════════════════════════════════════════════════════════
"""

print(CONCEITOS)


###############################################################################
# 📝 PARTE 2: EXEMPLOS PRÁTICOS
###############################################################################

print("\\n" + "="*73)
print("EXEMPLOS PRÁTICOS - URLs E DOMÍNIOS")
print("="*73)

# Status codes considerados como "domínio ativo"
STATUS_CODES_ATIVOS = [200, 201, 202, 301, 302, 403]

# --- EXEMPLO 1: Função para corrigir URL ---
print("\\n🔹 EXEMPLO 1: Corrigir URLs incompletas")
print("-" * 73)

def corrigir_url(url):
    """Adiciona https:// se não tiver protocolo"""
    if not url.startswith(("http://", "https://")):
        return f"https://{url}"
    return url

urls_para_testar = [
    "google.com",
    "https://github.com",
    "http://example.com",
    "facebook.com"
]

print("URLs originais → URLs corrigidas:")
for url in urls_para_testar:
    corrigida = corrigir_url(url)
    print(f"  {url:<30} → {corrigida}")


# --- EXEMPLO 2: Requisição simples com tratamento de erro ---
print("\\n\\n🔹 EXEMPLO 2: Verificar status de um domínio")
print("-" * 73)

def verificar_dominio(url):
    """Verifica status HTTP de um domínio"""
    url_corrigida = corrigir_url(url)
    
    try:
        response = requests.get(url_corrigida, timeout=5)
        return response.status_code
    except requests.RequestException as e:
        print(f"  ✗ Erro ao acessar {url}: {type(e).__name__}")
        return None

# Testar alguns domínios
print("Verificando domínios:")
dominios = ["google.com", "github.com", "dominio-inexistente-12345.com"]

for dominio in dominios:
    status = verificar_dominio(dominio)
    if status:
        ativo = "Ativo ✓" if status in STATUS_CODES_ATIVOS else "Inativo ✗"
        print(f"  {dominio:<30} → {status} ({ativo})")


# --- EXEMPLO 3: Verificação com lista customizada de status codes ---
print("\\n\\n🔹 EXEMPLO 3: Verificar com status codes customizados")
print("-" * 73)

def esta_ativo(status_code, codigos_validos):
    """Verifica se status code está na lista de válidos"""
    return status_code in codigos_validos

def analisar_dominio(url, codigos_esperados):
    """Verifica domínio e classifica como ativo/inativo"""
    url_corrigida = corrigir_url(url)
    
    try:
        response = requests.get(url_corrigida, timeout=5)
        ativo = esta_ativo(response.status_code, codigos_esperados)
        
        print(f"  {url}")
        print(f"    Status: {response.status_code}")
        print(f"    Estado: {'✓ Ativo' if ativo else '✗ Inativo'}")
        
        return ativo
    except requests.RequestException:
        print(f"  {url}")
        print(f"    Status: Erro de conexão")
        print(f"    Estado: ✗ Inativo (não respondeu)")
        return False

print("Analisando com diferentes critérios:")
codigos_rigorosos = [200, 201, 202]  # Apenas sucesso
print("\\nCritério RIGOROSO (apenas 200, 201, 202):")
analisar_dominio("google.com", codigos_rigorosos)

codigos_permissivos = [200, 201, 202, 301, 302, 403]  # Sucesso + redir + bloqueio
print("\\nCritério PERMISSIVO (200, 201, 202, 301, 302, 403):")
analisar_dominio("google.com", codigos_permissivos)


# --- EXEMPLO 4: Processar múltiplos domínios ---
print("\\n\\n🔹 EXEMPLO 4: Processar lista de domínios")
print("-" * 73)

def verificar_lista(lista_dominios, timeout=5):
    """Verifica múltiplos domínios e retorna tuplas (domínio, status)"""
    resultados = []
    
    for dominio in lista_dominios:
        url_corrigida = corrigir_url(dominio)
        try:
            response = requests.get(url_corrigida, timeout=timeout)
            resultados.append((dominio, response.status_code, "✓ Respondeu"))
        except requests.Timeout:
            resultados.append((dominio, None, "✗ Timeout"))
        except requests.ConnectionError:
            resultados.append((dominio, None, "✗ Sem conexão"))
        except Exception as e:
            resultados.append((dominio, None, f"✗ {type(e).__name__}"))
    
    return resultados

dominios_teste = ["google.com", "github.com", "example.com"]
print(f"Verificando {len(dominios_teste)} domínios...\\n")

resultados = verificar_lista(dominios_teste)
for dominio, status, mensagem in resultados:
    status_str = f"({status})" if status else ""
    print(f"  {dominio:<25} {status_str:<8} {mensagem}")


# --- EXEMPLO 5: Operações com URLs ---
print("\\n\\n🔹 EXEMPLO 5: Informações sobre a resposta")
print("-" * 73)

def inspecionar_url(url):
    """Mostra informações detalhadas sobre a resposta"""
    url_corrigida = corrigir_url(url)
    
    try:
        response = requests.get(url_corrigida, timeout=5)
        
        print(f"URL: {url_corrigida}")
        print(f"Status Code: {response.status_code}")
        print(f"Razão: {response.reason}")
        print(f"URL final (após redirects): {response.url}")
        print(f"Tipo de conteúdo: {response.headers.get('Content-Type', 'N/A')}")
        print(f"Tamanho do corpo: {len(response.text)} caracteres")
        
    except requests.RequestException as e:
        print(f"Erro: {e}")

print("Inspecionando google.com:")
inspecionar_url("google.com")


# --- EXEMPLO 6: Converter argumentos do comando ---
print("\\n\\n🔹 EXEMPLO 6: Processar sys.argv")
print("-" * 73)

print(f"sys.argv = {sys.argv}")
print("\\nExplicação:")
print(f"  sys.argv[0] (nome do script): {sys.argv[0]}")
if len(sys.argv) > 1:
    print(f"  sys.argv[1:] (argumentos): {sys.argv[1:]}")
else:
    print(f"  (Nenhum argumento fornecido)")

print("\\nUso esperado:")
print("  python3 script.py google.com github.com")
print("  python3 script.py dominio1.com,dominio2.com,dominio3.com")


###############################################################################
# 🔧 PARTE 3: FUNÇÃO COMPLETA
###############################################################################

print("\\n\\n" + "="*73)
print("FUNÇÃO COMPLETA - Verificador de Domínios")
print("="*73 + "\\n")

def verificador_completo(dominios_arg=None):
    """
    Verifica disponibilidade de domínios.
    
    Uso:
        python3 script.py google.com github.com
        python3 script.py "google.com,github.com,example.com"
    """
    
    # Obter domínios de argumentos ou de entrada padrão
    if dominios_arg:
        dominios = dominios_arg
    elif len(sys.argv) > 1:
        dominios = []
        for arg in sys.argv[1:]:
            dominios.extend(arg.split(","))
    else:
        print("Uso: python3 script.py dominio1 dominio2 ...")
        return
    
    # Remover espaços em branco
    dominios = [d.strip() for d in dominios if d.strip()]
    
    if not dominios:
        print("Nenhum domínio fornecido")
        return
    
    print(f"Verificando {len(dominios)} domínio(s)...\\n")
    
    # Cabeçalho da tabela
    print(f"{'Domínio':<35} {'Status':<10} {'Resultado'}")
    print("-" * 70)
    
    # Verificar cada domínio
    for dominio in dominios:
        url_corrigida = corrigir_url(dominio)
        
        try:
            response = requests.get(url_corrigida, timeout=5)
            ativo = "✓ Ativo" if response.status_code in STATUS_CODES_ATIVOS else "✗ Bloqueado"
            print(f"{dominio:<35} {response.status_code:<10} {ativo}")
            
        except requests.Timeout:
            print(f"{dominio:<35} {'TIMEOUT':<10} ✗ Sem resposta (>5s)")
        except requests.ConnectionError:
            print(f"{dominio:<35} {'ERRO':<10} ✗ Sem conexão")
        except Exception as e:
            print(f"{dominio:<35} {'ERRO':<10} ✗ {type(e).__name__}")

# Exemplo de uso (comentado para não quebrar o script)
# verificador_completo(["google.com", "github.com", "example.com"])


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
│ Fazer requisição GET     │ requests.get()    │ r = requests.get(url)     │
│ Com timeout              │ timeout=N         │ requests.get(url, t=5)    │
│ Status code              │ response.status   │ if r.status_code == 200:  │
│ Texto da resposta        │ response.text     │ html = r.text             │
│ Cabeçalhos               │ response.headers  │ r.headers['Content-Type'] │
│                          │                   │                           │
│ Argumentos do script     │ sys.argv          │ dominio = sys.argv[1]     │
│ Todos os argumentos      │ sys.argv[1:]      │ args = sys.argv[1:]       │
│ Dividir por vírgula      │ arg.split(",")    │ dominios.extend(a.split())│
│                          │                   │                           │
│ Adicionar protocolo      │ f"https://{url}"  │ if not url.startswith...  │
│ Verificar prefixo        │ startswith()      │ url.startswith("http")    │
│                          │                   │                           │
│ Tratar exceção genérica  │ except:           │ except:                   │
│                          │                   │     print("erro")         │
│ Exceção específica       │ except Exception  │ except requests.RequestEx │
│                          │                   │                           │
│ Status code in lista     │ if code in [...]  │ if r.status_code in [200] │
│ Timeout                  │ timeout=N         │ requests.get(url, t=5)    │
│                          │                   │                           │
└──────────────────────────┴──────────────────┴───────────────────────────┘
"""

print(TABELA)

print("\\n" + "="*73)
print("✅ Script finalizado!")
print("="*73)

if __name__ == "__main__":
    # Executar apenas se chamado diretamente com argumentos
    if len(sys.argv) > 1:
        verificador_completo()
