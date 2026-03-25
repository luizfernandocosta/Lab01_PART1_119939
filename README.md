# Lab01_PART1_119939

Este projeto usa **uv** como gerenciador de pacotes.

## Pre requisitos

- Python **3.14** ou superior
- `uv` instalado na sua maquina

Para instalar as dependencias do projeto, utilize o comando:
    
    `uv sync`

## Rodando o projeto

1. Crie um arquivo `.env` na raiz do projeto com as seguintes variaveis:
    - KAGGLE_API_KEY=
    - DB_USER=
    - DB_PASSWORD=
    - DB_HOST=
    - DB_NAME=

Para criar um api token no Kaggle, vai em: https://www.kaggle.com/settings, clique em "Generate New Token", debaixo da secao de API e copie o token gerado.

2. Execute o comando:
   uv run python -m src.main

Arquitetura:
   O projeto pega a fonte dentro do Kaggle, passa pelo script do python, salva dentro de um arquivo .parquet e entao salva dentro do postgres

A pasta service contem cada layer do projeto (raw, silver e gold), cada uma tratando os dados diferentemente.

A pasta config contem metodos para mapeamento das variaveis de ambiente para o projeto.

A pasta dataclass contem as dataclasses utilizadas no projeto.

E o main.py e o arquivo principal para rodar o projeto.

| Coluna | Descricao |
|--------|-----------|
|movie_id|ID do filme do TMDB|
|title|Titulo do filme|
|vote_average|Media dos votos|
|vote_count|Contagem dos votos|
|status|Status do filme|
|release_date|Data de lancamento|
|revenue|Receita do filme|
|runtime|Duracao do filme|
|adult|Se o filme e de adulto ou nao|
|backdroppath|Caminho da imagem do filme|
|budget|Orcamento do filme|
|homepage|Site do filme|
|imdb_id|ID do IMDb|
|originallanguage|Linguagem original|
|originaltitle|Titulo original|
|overview|Descricao do filme|
|popularity|Popularidade do filme|
|poster_path|Caminho do poster do filme|
|tagline|tags do filme|
|genres|generos do filme|
|productin_companies|Empresas que produziram o filme|
|production_countries|Paises que produziram|
|spoken_languages|Linguas faladas no filme|
|keywords|Keywords do filme|