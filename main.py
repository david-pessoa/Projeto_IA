import streamlit as st
from components.loader import load_document
from components.models.vector_store import add_data, retrieving_data, clean_data
from components.prompt import results_template
from components.models.text_generation import write_message

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
        answer = write_message(input)
        st.markdown(answer)

    add_message("assistant", answer)