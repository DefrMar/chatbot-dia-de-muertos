import streamlit as st
from motor_inferencia import inferir


st.set_page_config(
    page_title="Chatbot Día de Muertos",
    page_icon="💀",
    layout="centered"
)

st.title("💀 Chatbot Día de Muertos")

st.write(
    "Soy un sistema experto enfocado exclusivamente "
    "en el Día de Muertos."
)

if "mensajes" not in st.session_state:
    st.session_state.mensajes = []

for mensaje in st.session_state.mensajes:
    with st.chat_message(mensaje["rol"]):
        st.write(mensaje["contenido"])

pregunta = st.chat_input("Escribe tu pregunta...")

if pregunta:

    st.session_state.mensajes.append({
        "rol": "user",
        "contenido": pregunta
    })

    with st.chat_message("user"):
        st.write(pregunta)

    respuesta = inferir(pregunta)

    st.session_state.mensajes.append({
        "rol": "assistant",
        "contenido": respuesta
    })

    with st.chat_message("assistant"):
        st.write(respuesta)