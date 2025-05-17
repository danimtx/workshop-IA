import streamlit as st

st.set_page_config(page_title="Generador de flujos de Apps", layout="centered")

st.title("Generador de flujos de Apps con IA")

idea = st.text_input("Describe tu idea de App: ")

if st.button("Generar flujo"):
    st.write("Aqui mostramos el flujo generado.")