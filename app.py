import streamlit as st
from openai import OpenAI

# Configura tu clave de API de OpenAI
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

# Leer el contenido del archivo PDF previamente extraído
with open("contenido_pdf.txt", "r", encoding="utf-8") as file:
    pdf_text = file.read()

# Título de la aplicación
st.markdown("<h1 style='text-align: center;'>Consultoría para Egresados  Escuela de Oficios</h1>", unsafe_allow_html=True)


# Caja de texto para ingresar la pregunta
import streamlit as st

# Título principal


# Inicializar el estado de la pregunta
if "pregunta" not in st.session_state:
    st.session_state["pregunta"] = ""  # Inicializa el estado de la pregunta

# Cuadro de texto para ingresar la pregunta
pregunta = st.text_input("Escribe tu pregunta :", value=st.session_state["pregunta"], key="input_pregunta")

# Botón de "Borrar"
if st.button("Borrar"):
    st.session_state["pregunta"] = ""  # Limpia el estado de la pregunta

# Botón para enviar la pregunta
if st.button("Enviar"):
    if pregunta.lower() == "salir":
        st.write("Gracias por usar el sistema. ¡Hasta luego!")
    else:
        # Aquí va la lógica para procesar la pregunta y generar una respuesta
        respuesta = f"Respuesta a: {pregunta}"
        st.write(respuesta)

        # Función para hacer preguntas a la IA
        prompt = f"Basándote en el siguiente texto:\n\n{pdf_text}\n\nResponde a la siguiente pregunta: {pregunta}"
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un asistente útil que responde preguntas basadas en un texto proporcionado."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,  # Aumenta este valor si necesitas respuestas más largas
            temperature=0.7
        )
        respuesta = response.choices[0].message.content.strip()
        st.write(f"**Respuesta:** {respuesta}")