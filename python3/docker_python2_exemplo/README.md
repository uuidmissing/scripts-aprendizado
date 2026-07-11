# Mini projeto Docker com Python 2

Este exemplo mostra como rodar um script antigo em Python 2 dentro de um container Docker.

## Estrutura

- `Dockerfile`: define a imagem do container
- `app.py`: script de exemplo em Python 2
- `docker-compose.yml`: facilita a execução

## Como executar

### Opção 1: com Docker

```bash
docker build -t python2-mini .
docker run --rm -it python2-mini
```

### Opção 2: com Docker Compose

```bash
docker compose up --build
```

## O que aprender aqui

- O `Dockerfile` define o ambiente.
- O `COPY . /app` envia os arquivos para dentro do container.
- O `WORKDIR /app` define onde o código será executado.
- O `docker run` executa o container.
- O `docker compose` organiza a execução para você.

## Observação

Este exemplo usa `raw_input`, que existe em Python 2. Em Python 3, esse comando foi substituído por `input`.
