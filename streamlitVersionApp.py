import streamlit as st

from modules.excel_loader import ExcelLoader
from modules.chunker import Chunker
from modules.embedder import Embedder
from modules.vectordb import VectorDB
from modules.retriever import Retriever
from modules.chatbot import ChatBot

st.set_page_config(
    page_title="Excel RAG Chatbot",
    page_icon="📊",
    layout="wide"
)
st.title("📊 Excel RAG Chatbot")
st.write(
    "Ask questions about your Employee Dataset."
)
@st.cache_resource
def initialize_chatbot():
    
    loader = ExcelLoader()
    df = loader.load_excel()
    chunker = Chunker(df)
    chunks = chunker.create_chunks()
    embedder = Embedder()
    embedded_chunks = embedder.generate_embeddings(chunks)
    db = VectorDB()

    db.create_collection()

    db.insert_chunks(embedded_chunks)

    retriever = Retriever(db)

    chatbot = ChatBot()

    return retriever, chatbot


retriever, chatbot = initialize_chatbot()


if "messages" not in st.session_state:

    st.session_state.messages = []


for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


query = st.chat_input("Ask your question...")


if query:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )

    with st.chat_message("user"):
        st.markdown(query)

    contexts = retriever.retrieve(query)

    answer = chatbot.ask(
        contexts,
        query
    )

    with st.chat_message("assistant"):
        st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )