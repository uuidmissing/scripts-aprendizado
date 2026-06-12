# 📚 Guias Educacionais Consolidados

Este arquivo documenta os scripts de aprendizado reorganizados em temas únicos, com exemplos e boas práticas.

## 🎯 Arquivos Consolidados

### Bash - Condicionais e Testes
**Arquivo:** `bash_condicionais_e_testes.sh`

Cobre:
- Operadores de teste: `[ ]`, `[[ ]]`, `(( ))`
- Comparações numéricas: `-eq`, `-lt`, `-gt`, etc
- Comparações de strings: `==`, `!=`, `-z`, `-n`
- Testes de arquivo: `-e`, `-f`, `-d`, `-r`, `-w`, `-x`
- Lógica booleana: `&&`, `||`, `!`
- Funções com validação
- Loops com condições
- **Boas práticas:** sempre use `[[ ]]`, use `-z/-n` para strings, aspas em variáveis

Consolida:
- `bash/condicionais.sh`
- `bash/condicionais_completo.sh`
- `bash/comparacoes_regex_e_posix`
- `bash/guia_if_bash.txt`

---

### Bash - EOF e HERE DOCUMENTS
**Arquivo:** `bash_eof_e_heredoc.sh`

Cobre:
- Sintaxe básica: `cat << EOF ... EOF`
- Interpolação de variáveis (com/sem aspas)
- Redirecionamento: `>` (gravar), `>>` (acrescentar)
- Leitura linha a linha: `while read`
- Armazenar em variável: `read -d ''`
- Agrupamento de comandos: `{ ... }`
- Case statement com patterns
- Criar scripts/arquivos de configuração

Consolida:
- `bash/EOF_E_IFS/EOF_IFS.sh`
- `bash/EOF_E_IFS/EOF_IFS2.sh`
- `bash/EOF_E_IFS/EOFtutorial`

---

### Bash - IFS (Internal Field Separator)
**Arquivo:** `bash_ifs_field_separator.sh`

Cobre:
- O que é IFS e seu valor padrão
- Customizar separadores: `IFS=','`, `IFS=':'`, `IFS='|'`
- Comando `read` com `-r` flag
- Leitura de arquivo linha a linha
- Preservar espaços em branco
- Problemas comuns e soluções
- Processar CSV, PATH, /etc/passwd

Consolida:
- `bash/EOF_E_IFS/IFS_NO_WHILE`
- `bash/lembrete_uso_de_variavel.txt`

---

### Bash - REGEX (Expressões Regulares)
**Arquivo:** `bash_regex.sh`

Cobre:
- Sintaxe: `[[ $var =~ regex ]]`
- Metacaracteres: `^`, `$`, `.`, `*`, `+`, `?`, `[]`, `()`
- Quantificadores: `{n}`, `{n,}`, `{n,m}`
- Classes de caracteres: `[a-z]`, `[0-9]`, `[^abc]`
- Captura de grupos: `BASH_REMATCH`
- Validação: email, telefone, URL, data, hora
- Glob vs Regex
- Exemplos práticos e casos de uso

Consolida:
- `bash/regex/ex_regex1.sh`
- `bash/regex/ex_regex2.sh`
- `bash/regex/regex.sh`
- `bash/regex/globing_e_regex`
- `bash/regex/regex_basico_bash.txt`
- `bash/regex/regex_ocorrencias`
- `bash/regex/tutorial_regex.sh`
- `bash/regex/regexfinal`
- `bash/regex/regex.zsh`

---

### Bash - Login e Autenticação
**Arquivo:** `bash_login_autenticacao.sh`

Cobre:
- Validação de email com regex
- Validação de username
- Validação de senha forte
- Return codes (0=sucesso, 1=falha)
- Contador de tentativas
- Feedback visual com cores ANSI
- Sistema completo de autenticação
- Menu interativo

Consolida:
- `bash/admloginteste.sh`
- `bash/login` (e sua cópia `bash/testelogin.sh`)

---

### Bash - Arrays e Strings
**Arquivo:** `bash_arrays_e_strings.sh`

Cobre:
- Arrays simples (indexados)
- Arrays associativos (dicionários)
- Operações com arrays: adicionar, remover, loop
- Manipulação de strings: substring, substituição, trim
- Converter maiúsculas/minúsculas
- Dividir strings (split)
- Printf para formatação de tabelas
- Validação antes de adicionar ao array
- Remover duplicatas
- Ordenação
- Buscar índice

Consolida:
- `bash/checar_strings_em_arrays.sh`
- `bash/tabeladeprecosbash`

---

### Bash - Parsing de Argumentos (getopts)
**Arquivo:** `bash/parsing_com_getopts`

Ainda existe como arquivo individual. Cobre:
- Processar opções de linha de comando
- Opções com valores: `-u url`, `-o output`
- Help com `-h`
- Validação de argumentos

---

### Bash - Git e Repositórios
**Arquivo:** `bash/baixador_de_repo.sh`

Ainda existe como arquivo individual. Cobre:
- Clone de repositório
- Reset hard
- Pull de repositório

---

### Bash - Cores ANSI
**Arquivo:** `bash/cores_ANSI`

Ainda existe como arquivo individual. Cobre:
- Variáveis com códigos de escape: `\033[...m`
- Cores básicas (30-37)
- Cores brilhantes (1;30-1;37)
- Estilos (bold, underline, blink)
- Reset

---

### Bash - Importação de Cores
**Arquivo:** `bash/importacao_de_cores`

Pequeno script que demonstra como importar e usar `cores_ANSI`.

---

### Lembrete de Uso de Variável
**Arquivo:** `bash/lembrete_uso_de_variavel.txt`

Tabela de referência: `%s`, `%b`, `$var`, `${var}`

---

## 🐍 Python3 - Consolidados (3 novos)

### Python - Fundamentos
**Arquivo:** `python_fundamentos.py`

Cobre:
- Listas e dicionários
- Manipulação de dados com `input()`
- Loops: for, while, enumerate
- Try/except para validação
- Listas de dicionários (estruturas de dados)
- Função `len()`, `set()`, `set().union()`
- Pacotes e módulos (`__init__.py`)
- Função `__main__`
- Modificação de `sys.path`

Consolida:
- `aulaIA.py`
- `guia_de_python3`
- `explicacao_do_init.py.txt`
- `teste_do_sys.py`

---

### Python - URLs e Domínios
**Arquivo:** `python_urls_e_dominios.py`

Cobre:
- Requisições HTTP com `requests`
- Status codes (2xx, 3xx, 4xx, 5xx)
- Argumentos de linha de comando (`sys.argv`)
- Tratamento de exceções (`RequestException`, `Timeout`)
- Correção de URLs
- Verificação de disponibilidade
- Processamento em lote

Consolida:
- `python3_def.py`
- `pratica.py`

---

### Python - Enumeração de Subdomínios
**Arquivo:** `python_subdomains.py`

Cobre:
- Brute force básico de subdomínios
- Listas de palavras comuns
- Requisições com timeout
- Tratamento de erros
- Salvamento em arquivo
- Validação com DNS (conceito)
- Enumerador completo

Consolida:
- `subd.py`

---

### Python - Funções Utilitárias
**Arquivo:** `funcoes.py`

Ainda existe como arquivo individual. Cobre:
- Operações com listas
- Operações com domínios
- Operações com dicionários
- Funções reutilizáveis

---

### Python - Automação de Sistema
**Arquivo:** `instaladorlinux_python3.py`

Ainda existe como arquivo individual. Cobre:
- Automação no Kali Linux
- Subprocess para executar comandos
- Cores ANSI
- Clone e atualização de repositórios
- Instalação de ferramentas

## 📊 Estatísticas

**Antes:**
- ~44 arquivos educacionais dispersos
- Muitas duplicatas
- Organização por tópico inconsistente

**Depois:**
- 6 arquivos consolidados em Bash (111KB)
- 3 arquivos consolidados em Python (55KB)
- ~166KB de conteúdo bem organizado
- Cada tema em um arquivo único
- Exemplos, explicações e boas práticas integradas
- 2 arquivos específicos preservados (funcoes.py, instaladorlinux_python3.py)

## 🎓 Como Usar

1. Escolha o tema que deseja aprender
2. Abra o arquivo correspondente (`bash_*.sh`)
3. Leia a PARTE 1 (conceitos)
4. Execute o script para ver os EXEMPLOS (PARTE 2)
5. Consulte a tabela de referência (PARTE 4)

## ✅ Próximos Passos

- [ ] Criar arquivo principal `README_EDUCACAO.md` com guia de estudo recomendado
- [ ] Melhorar `funcoes.py` (corrigir bugs e expandir)
- [ ] Criar exemplos interativos com entrada do usuário
- [ ] Adicionar testes automatizados para cada tema
- [ ] Criar repositório de wordlists para OSINT
