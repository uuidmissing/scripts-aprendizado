# Guia Unificado de Git

Este documento consolida o conteúdo dos arquivos Git existentes no diretório `git/` e remove duplicações. Ele traz os passos básicos, exemplos e comandos úteis em um só lugar.

---

## 1. Começando com Git

### Iniciar um repositório Git

```bash
git init
```

Isso cria a pasta oculta `.git/` e habilita o versionamento no diretório atual.

### Verificar status

```bash
git status
```

Mostra arquivos modificados, em stage e não rastreados.

### Verificar histórico

```bash
git log
```
```

### Listar e criar branches

```bash
git branch
git checkout -b minha-branch
```

---

## 2. Configurações iniciais do Git

### Configurar nome e e-mail global

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
```

### Escopos de configuração

- `--system`: afeta todos os usuários e repositórios do sistema.
- `--global`: afeta o usuário atual em todos os repositórios.
- `--local`: afeta apenas o repositório atual.

Prioridade: Local > Global > System

---

## 3. Fluxo básico de commits

### Adicionar arquivos ao stage

```bash
git add arquivo.txt
git add .
```

### Criar commit

```bash
git commit -m "Mensagem do commit"
```

### Exemplo completo de fluxo

```bash
git add .
git commit -m "Commit inicial"
```

---

## 4. Conectar ao GitHub e enviar código

### Adicionar remoto

```bash
git remote add origin https://github.com/usuario/repositorio.git
```

### Atualizar remoto existente

```bash
git remote set-url origin https://github.com/usuario/repositorio.git
```

### Enviar código

```bash
git push -u origin main
```

(use `master` se essa for a branch principal do seu repositório)

---

## 5. Configurar `.gitignore`

### Exemplo de `.gitignore`

```gitignore
.env
*.log
logs/
node_modules/
__pycache__/
*.pyc
*.tmp
*.swp
*.bak
*.pem
*.key
secrets.txt
dist/
build/
.vscode/
.idea/
*.code-workspace
```

Esse arquivo impede que arquivos sensíveis, caches e builds sejam versionados.

---

## 6. Git Credential Manager e helpers de credencial

### Instalar o Git Credential Manager no Linux

```bash
sudo apt update
sudo apt install -y wget git curl libcurl4 libexpat1 gettext gnupg
GCM_VERSION="2.4.1"
wget https://github.com/GitCredentialManager/git-credential-manager/releases/download/v${GCM_VERSION}/gcm-linux_amd64.${GCM_VERSION}.deb -O gcm.deb
sudo dpkg -i gcm.deb
rm gcm.deb
git config --global credential.helper manager
```

### Configurar `manager-core`

```bash
git config --global credential.helper manager-core
git config --global credential.helper
```

### Usar token com segurança

O GitHub não permite mais senha em `git push`. Use personal access token (PAT) e configure um helper para não digitar o token toda hora.

### Apagar credenciais salvas

```bash
git credential-manager erase
```

### Desabilitar helper

```bash
git config --global --unset credential.helper
```

---

## 7. `git pull` com merge padrão

### Definir merge como comportamento padrão

```bash
git config --global pull.rebase false
```

### Fluxo recomendado

```bash
git add .
git commit -m "Mensagem do commit"
git pull origin main
git push origin main
```

### Se ocorrer conflito

1. Resolva os conflitos nos arquivos indicados.
2. Use `git add nome_do_arquivo`.
3. Finalize com `git commit`.
4. Envie com `git push origin main`.

---

## 8. Criar um novo histórico de commits no GitHub

### Passos para criar branch orphan e novo histórico

```bash
git checkout --orphan new-main
git add -A
git commit -m "historico novo"
git branch -D main
git branch -m main
git push origin main --force-with-lease
git push --set-upstream origin main
```

Essa sequência cria um novo histórico limpo e substitui a branch principal.

---

## 9. Scripts úteis e exemplos

### Inicializar repositório e subir para remoto

Um script pode ajudar a automatizar:

- `git init`
- criar ou atualizar `.gitignore`
- configurar `user.name` e `user.email`
- fazer `git add .`
- fazer `git commit`
- configurar remoto e fazer `git push -u origin <branch>`

### Alterar configuração local de usuário em múltiplos repositórios

Use `git config --file "$REPO/.git/config" user.name "Seu Nome"` e `git config --file "$REPO/.git/config" user.email "seu@email.com"`.

---

## 10. Erros comuns e dicas

- Sempre confirme se `git status` está limpo antes de fazer `git pull`.
- Se o repositório remoto já existir, use `git remote set-url origin ...`.
- Use `git config --list` para verificar se seu nome e e-mail estão corretos.
- Para ver arquivos ignorados: `git ls-files --others --ignored --exclude-standard`.

---

## Referências rápidas

- `git status`
- `git add .`
- `git commit -m "msg"`
- `git push -u origin main`
- `git pull origin main`
- `git config --global user.name "Nome"`
- `git config --global user.email "email@exemplo.com"`

---

### Observação

Os scripts existentes em `git/` foram lidos para criar este documento unificado, que agora reúne informações de:
- `commitresetter.txt`
- `credentialhelperinstall.sh`
- `criando_git2`
- `criando_um_git`
- `erros_do_gitpull.txt`
- `exemplo_de_gitignore`
- `GMC_GitCredencialManager.txt`
- `revisao_git`
- `set_git_user.sh`
