import streamlit as st

st.set_page_config(page_title="Solemne II", layout="wide")

st.title("Solemne II - Taller de Programación")
st.write("App desplegada con GitHub + Streamlit Cloud ✅")

st.header("Entrada")
texto = st.text_input("Escribe algo")
st.write("Salida:", texto)
