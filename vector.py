from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

embeddings = OllamaEmbeddings(model='mxbai-embed-large')

PATH_DIR = './bulas'
db_location = './chrome_langchain_db'
add_documents = not os.path.exists(db_location)

# Ferramenta de split (pode ajustar o tamanho conforme necessário)
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,     # tamanho de cada pedaço
    chunk_overlap=100,  # sobreposição entre pedaços
)

if add_documents:
    documents = []
    ids = []
    i = 1
    for file in os.listdir(PATH_DIR):
        if os.path.isfile(os.path.join(PATH_DIR, file)):
            with open(os.path.join(PATH_DIR, file), 'r', encoding='utf-8') as archive:
                content = archive.read()

                # Criação de chunks
                chunks = text_splitter.create_documents([content])
                for chunk in chunks:
                    # Você pode adicionar metadados, como nome do arquivo
                    chunk.metadata['source'] = file
                    chunk.metadata['id'] = str(i)

                    documents.append(chunk)
                    ids.append(str(i))
                    i += 1

vector_store = Chroma(
    collection_name='bulas_de_remedios',
    persist_directory=db_location, 
    embedding_function=embeddings
    )

if add_documents:
   vector_store.add_documents(documents=documents, ids=ids)

retriever = vector_store.as_retriever(
   search_kwargs={'k': 3}
)