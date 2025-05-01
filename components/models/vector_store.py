from langchain_huggingface.embeddings import HuggingFaceEmbeddings
import faiss
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS

model_name = "alfaneo/jurisbert-base-portuguese-sts"
#model_name = "neuralmind/bert-base-portuguese-cased"
embeddings = HuggingFaceEmbeddings(model_name=model_name)
index = faiss.IndexFlatL2(768)
vector_store = FAISS(
    embedding_function=embeddings,
    index=index,
    docstore=InMemoryDocstore(),
    index_to_docstore_id={}
)

def add_data(chunks):
    ids = [chunks[i].metadata['id'] for i in range(len(chunks))]
    vector_store.add_documents(documents=chunks, ids=ids)

def extract_metadata(chunk):
    file = chunk.metadata["document"]
    page = chunk.metadata["page"]
    pos = chunk.metadata["position"]
    return file, page, pos

def retrieving_data(query, n_results):
    results = vector_store.max_marginal_relevance_search(query=query,k=n_results)
    return results

def clean_data():
    vector_store.index.reset()
    vector_store.docstore = InMemoryDocstore()
    vector_store.index_to_docstore_id = {}