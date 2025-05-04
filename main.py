import streamlit as st
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

# Preparação do modelo
model = OllamaLLM(model="llama3.2")

template = '''
    Você é um assistente de saúde virtual que entende de remédios e conhece a bula de todos eles

    Aqui estão as bulas relevantes, elas são fontes confiáveis: {bulas}
    Esta é a pergunta que você deve responder: {pergunta}
'''

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def write_answer(pergunta):
    bulas = retriever.invoke(pergunta)
    return chain.invoke({'bulas': bulas, 'pergunta': pergunta})


# Configuração da página
st.set_page_config(
    page_title="MedicineAI",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded",
    )

# Título
st.markdown("# MedicineAI")

# Iniciar conversa
if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "assistant",
        "content": "Olá, como posso te ajudar?"
        }]

# Mostrar conversa
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Adicionar mensagens
def add_message(role, content):
    st.session_state.messages.append({
        "role": role,
        "content": content
        })

# Entrada
if input := st.chat_input("Digite algo"):
    with st.chat_message("user"):
        st.markdown(input)

    add_message("user", input)

# Saída
if st.session_state.messages[-1]["role"] == "user": # Verificar se a última mensagem foi do usuário

    with st.chat_message("assistant"):
        st.spinner("A IA está pensando...")
        answer = write_answer(input)
        st.markdown(answer)

    
    add_message("assistant", answer)