import streamlit as st
from openai import OpenAI

modelo_ia = OpenAI(api_key="sua chave aqui")

st.write("# Chatbot com IA")



# Criar histórico do chat
if "lista_chat" not in st.session_state:
    st.session_state["lista_chat"] = []

# Mostrar histórico na tela sempre
for msg in st.session_state["lista_chat"]:
    st.chat_message(msg["role"]).write(msg["content"])

# Input do usuário
texto_usuario = st.chat_input("Digite sua mensagem")

if texto_usuario:
    # Mostrar mensagem do usuário
    st.chat_message("user").write(texto_usuario)
    mensagem_usuario = {"role": "user", "content": texto_usuario}
    st.session_state["lista_chat"].append(mensagem_usuario)

    # Resposta da IA 

    resposta_ia = modelo_ia.chat.completions.create(
        messages=st.session_state["lista_chat"],
        model="gpt-4o"
    )
    print(resposta_ia.choices[0].message.content)
    texto_resposta_ia = resposta_ia.choices[0].message.content

    st.chat_message("assistant").write(texto_resposta_ia)
    mensagem_ia = {"role": "assistant", "content": texto_resposta_ia}
    st.session_state["lista_chat"].append(mensagem_ia)

# Debug do histórico (opcional)
# st.write(st.session_state["lista_chat"])
