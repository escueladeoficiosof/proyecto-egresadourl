import os
from openai import OpenAI
import streamlit as st

# Configurar la clave API de OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Título de la aplicación
st.title("Consulta sobre Egresados")

# Entrada de texto para la pregunta
pregunta = st.text_input("Escribe tu pregunta:")

# Función para consultar OpenAI
def consultar_openai(pregunta):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Eres un asistente útil."},
            {"role": "user", "content": pregunta}
        ]
    )
    return response.choices[0].message.content

# Botón para enviar la pregunta
if st.button("Enviar"):
    if pregunta.strip() == "":
        st.warning("Por favor, ingresa una pregunta.")
    else:
        respuesta = consultar_openai(pregunta)
        st.write("Respuesta:")
        st.write(respuesta)