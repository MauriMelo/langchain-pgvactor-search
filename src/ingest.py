import os
from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_postgres import PGVector
from langchain_text_splitters import RecursiveCharacterTextSplitter
load_dotenv()

PDF_PATH = os.getenv("PDF_PATH")

def get_pdf_data(PDF_PATH):
    docs = PyPDFLoader(PDF_PATH).load()
    splits = RecursiveCharacterTextSplitter(
        chunk_size=1000, 
        chunk_overlap=150, 
        add_start_index=False,
    ).split_documents(docs)

    if not splits:
        raise SystemExit("No documents to ingest.")

    enriched = []
    for doc in splits:
        metadata = {}
        for k, v in doc.metadata.items():
            if v not in ("", None):
                metadata[k] = v

        doc = Document(
            page_content=doc.page_content,
            metadata=metadata
        )
        enriched.append(doc)
    return enriched


def ingest_pdf():   
    documents = get_pdf_data(PDF_PATH)
    print(f"Number of documents to ingest: {len(documents)}")

    embeddings = OpenAIEmbeddings(model=os.getenv("OPENAI_EMBEDDING_MODEL"))

    ids = [f"{doc.metadata.get('producer')}-{k}" for k, doc in enumerate(documents)]

    store = PGVector(
        embeddings=embeddings,
        collection_name=os.getenv("PG_VECTOR_COLLECTION_NAME"),
        connection=os.getenv("DATABASE_URL"),
        use_jsonb=True
    )

    store.add_documents(documents=documents, ids=ids)


if __name__ == "__main__":
    ingest_pdf()