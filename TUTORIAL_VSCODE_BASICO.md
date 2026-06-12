# Tutorial Básico de VS Code

## O que é o Visual Studio Code

O VS Code é um editor de código leve e extensível da Microsoft. Ele oferece:
- Edição de código com destaque de sintaxe
- Terminal integrado
- Debug embutido
- Git integrado
- Extensões para quase todas as linguagens e ferramentas

## Abrindo um projeto

1. Abra o VS Code.
2. Use `File > Open Folder...` para abrir a pasta do projeto.
3. Alternativamente, no terminal do sistema:
   ```bash
   code /caminho/para/pasta
   ```

## Interface principal

- Explorer: navega pelas pastas e arquivos do projeto.
- Search: busca texto em todos os arquivos.
- Source Control: integrações com Git.
- Run and Debug: configuração de depuração.
- Extensions: instala add-ons e suporte a linguagens.

## Atalhos básicos

- `Ctrl+P`: abrir arquivo rapidamente.
- `Ctrl+Shift+P`: abrir Command Palette.
- `Ctrl+Shift+N`: nova janela.
- `Ctrl+O`: abrir arquivo.
- `Ctrl+S`: salvar.
- `Ctrl+Shift+S`: salvar como.
- `Ctrl+W`: fechar aba.
- `Ctrl+K Ctrl+S`: atalhos de teclado.

## Navegação e edição

- `Ctrl+G`: ir para linha.
- `Ctrl+F`: buscar no arquivo.
- `Ctrl+H`: buscar e substituir.
- `Alt+Seta para cima/baixo`: mover linha.
- `Shift+Alt+Seta`: duplicar linha.
- `Ctrl+/`: comentar/descomentar a linha.

## Terminal integrado

1. Abra com `Ctrl+`` (Ctrl + backtick) ou `Terminal > New Terminal`.
2. Use o terminal integrado para rodar comandos do projeto, como `npm`, `python`, `git`.
3. Você pode ter vários terminais abertos e alternar entre eles.

## Extensões recomendadas

- `Python` (Microsoft)
- `Prettier - Code formatter`
- `ESLint`
- `Docker`
- `Live Server`
- `GitLens`
- `Bracket Pair Colorizer`

Para instalar: abra `Extensions` ou `Ctrl+Shift+X`, busque a extensão e clique em `Install`.

## Configurações básicas

1. Abra o arquivo de configurações com `Ctrl+Shift+P` e digite `Preferences: Open Settings (JSON)`.
2. Exemplo de ajustes úteis:
   ```json
   {
     "editor.tabSize": 2,
     "editor.fontFamily": "Fira Code, Consolas, 'Courier New', monospace",
     "editor.fontLigatures": true,
     "editor.formatOnSave": true,
     "files.exclude": {
       "**/.git": true,
       "**/.DS_Store": true
     },
     "terminal.integrated.fontSize": 13
   }
   ```

## Git no VS Code

- Use a aba `Source Control` para ver alterações.
- `git add`, `commit` e `push` podem ser feitos pela interface.
- O VS Code mostra diffs e conflitos de merge.

## Debug básico

1. Abra `Run and Debug` (`Ctrl+Shift+D`).
2. Crie ou use um `launch.json` para configurar sua aplicação.
3. Coloque breakpoints clicando na margem esquerda.
4. Inicie a depuração com `F5`.

## Dicas finais

- Use `Ctrl+K Z` para entrar em modo Zen.
- Use `Ctrl+Shift+M` para abrir o painel de problemas.
- Ative o `Auto Save` em `File > Auto Save` para salvar automaticamente.
- Use `Preferences: Open Keyboard Shortcuts` para personalizar atalhos.

## Referências rápidas

- Command Palette: `Ctrl+Shift+P`
- Abrir arquivo: `Ctrl+P`
- Terminal integrado: `Ctrl+`
- Alternar sidebar: `Ctrl+B`
- Multi-cursor: `Alt+Click`
