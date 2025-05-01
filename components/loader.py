import pdfplumber
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

def split_text(page_content, name, i):
    text_splitter = RecursiveCharacterTextSplitter(
        separators=['.', ';', ',', '\n', ' '],
        chunk_size=400,
        chunk_overlap=40
    )

    docs = []
    chunks = text_splitter.split_text(page_content)
    pos = 0
    for chunk in chunks:
        doc = Document(
            page_content = chunk,
            metadata = {
                "id": f"{name}:{i}:{pos}",
                "document": name,
                "page": i,
                "position": pos
                }
        )

        pos += 1
        docs.append(doc)

    return docs

def load_document(file, name):
    with pdfplumber.open(file) as pdf:
        chunks = []
        images = []
        page_i = 0
        for page in pdf.pages:
            page_content = page.extract_text()
            page_picture = page.to_image(resolution=100).original
            chunks += split_text(page_content, name, page_i)
            images.append(page_picture)
            page_i += 1

        return chunks, images