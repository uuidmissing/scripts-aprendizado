# Docker e containers para executar scripts antigos em Python 2

## O que é Docker?

Docker é uma ferramenta para criar e rodar containers, que são ambientes isolados e leves.

Um container é parecido com uma máquina virtual, mas mais leve, porque compartilha o kernel do sistema operacional hospedeiro.

### Vantagens principais
- isolamento do ambiente;
- reproduzibilidade;
- evita conflitos entre dependências;
- facilita rodar softwares antigos sem mexer no sistema principal.

## Diferença entre container e máquina virtual

- Máquina virtual: mais pesada, roda um sistema operacional completo.
- Container: mais leve, roda processos isolados com menos overhead.

Para scripts antigos, containers são muito úteis porque você consegue criar um ambiente específico para rodar aquele código sem interferir no seu sistema atual.

## Como Docker ajuda com Python 2

Se você tem scripts muito antigos escritos para Python 2, pode criar um container com uma imagem que tenha Python 2 instalado.

Assim:
- o ambiente fica isolado;
- você não precisa instalar Python 2 diretamente no host;
- evita problemas com bibliotecas e versões diferentes.

## Exemplo prático: criar um container com Python 2

### 1. Instalar Docker

No Linux, normalmente o processo é algo como:

```bash
sudo apt update
sudo apt install docker.io docker-compose-plugin
```

Depois, habilite e inicie o serviço:

```bash
sudo systemctl enable docker
sudo systemctl start docker
```

### 2. Criar um diretório para o projeto

```bash
mkdir -p ~/python2-old-script
cd ~/python2-old-script
```

### 3. Criar um arquivo chamado `Dockerfile`

```dockerfile
FROM python:2.7-slim

WORKDIR /app
COPY . /app

CMD ["python", "script.py"]
```

### 4. Criar um script de exemplo

Crie um arquivo `script.py`:

```python
print("Olá do Python 2")
```

### 5. Construir a imagem

```bash
docker build -t python2-old-env .
```

### 6. Rodar o container

```bash
docker run --rm python2-old-env
```

## Melhor prática: montar o diretório local no container

Se você quiser editar arquivos no host e executar dentro do container, use volume:

```bash
docker run --rm -it -v "$PWD":/app -w /app python:2.7-slim bash
```

Depois, dentro do container:

```bash
python script.py
```

## Exemplo com um script antigo

Se seu script chama `python2` ou usa sintaxe antiga do Python 2, basta rodar:

```bash
docker run --rm -it -v "$PWD":/app -w /app python:2.7-slim python script.py
```

## Docker Compose

Se o ambiente ficar maior, você pode usar Docker Compose para organizar melhor.

Exemplo de `docker-compose.yml`:

```yaml
services:
  python2:
    image: python:2.7-slim
    working_dir: /app
    volumes:
      - .:/app
    command: python script.py
```

Rodando:

```bash
docker compose up
```

## Cuidados importantes

- Python 2 está descontinuado e muitos pacotes antigos não funcionam mais.
- Alguns scripts podem depender de bibliotecas específicas.
- Sempre teste em um ambiente isolado antes de rodar em produção.

## Quando usar Docker

Use Docker quando:
- você precisa executar um script muito antigo;
- quer evitar alterar o sistema principal;
- precisa manter um ambiente reprodutível para testes.

## Resumo

Docker permite criar um ambiente isolado para rodar Python 2 sem poluir o seu sistema.

A ideia geral é:
1. criar uma imagem com Python 2;
2. montar o projeto no container;
3. executar o script ali.

Se quiser, o próximo passo pode ser criar um exemplo completo com:
- `Dockerfile`;
- `docker-compose.yml`;
- um script antigo em Python 2;
- instruções para rodar no Kali.
