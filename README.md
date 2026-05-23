# Desafio MBA Engenharia de Software com IA - Full Cycle

## Como executar o projeto


### 1. Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com base no arquivo `.env.example`:

```bash
cp .env.example .env
```
Edite o arquivo `.env` e preencha os valores necessários, especialmente o `OPENAI_API_KEY` e ajuste o caminho do `PDF_PATH` se necessário.

### 2. Subir o banco de dados com Docker Compose

```bash
docker-compose up -d
```
Isso irá iniciar um container PostgreSQL com a extensão pgvector habilitada.

### 3. Instalar as dependências Python

Recomenda-se o uso de um ambiente virtual:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 4. Adicionar o PDF para ingestão

Coloque o arquivo PDF desejado na raiz do projeto e ajuste o caminho em `PDF_PATH` no `.env`.

### 5. Ingerir o PDF no banco de dados vetorial

```bash
python src/ingest.py
```
Esse comando irá processar o PDF e armazenar os embeddings no banco de dados PostgreSQL.

### 6. Executar o chat de perguntas e respostas

```bash
python src/chat.py
```
Digite sua pergunta quando solicitado. O sistema irá buscar a resposta baseada no conteúdo do PDF ingerido.

---

## Resumo das variáveis de ambiente (`.env`)

- `DATABASE_URL`: URL de conexão com o PostgreSQL (ex: `postgresql+psycopg://postgres:postgres@localhost:5432/rag`)
- `PG_VECTOR_COLLECTION_NAME`: Nome da coleção vetorial (ex: `gpt5_collection`)
- `PDF_PATH`: Caminho do PDF a ser ingerido (ex: `document.pdf`)
- `OPENAI_MODEL_NAME`: Nome do modelo OpenAI para chat (ex: `gpt-5-nano`)
- `OPENAI_API_KEY`: Chave de API da OpenAI
- `OPENAI_EMBEDDING_MODEL`: Modelo de embedding da OpenAI (ex: `text-embedding-3-small`)

---

## Observações

- Certifique-se de que o banco de dados está rodando antes de executar os scripts Python.
- O projeto utiliza a extensão pgvector para armazenar embeddings no PostgreSQL.
- O arquivo `requirements.txt` lista todas as dependências necessárias.

