import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Solemne II", layout="wide")

st.title("Solemne II - Taller de Programación")
st.write("Consumo de datos desde datos.gob.cl (ODEPA)")

# --- API ODEPA ---
RESOURCE_ID = "7f8f1255-a13b-4233-aad0-631054a8a025"
URL = "https://datos.gob.cl/api/3/action/datastore_search"

params = {
    "resource_id": RESOURCE_ID,
    "limit": 1000
}

response = requests.get(URL, params=params)
data = response.json()

records = data["result"]["records"]
df = pd.DataFrame(records)

st.subheader("Vista previa de los datos")
st.dataframe(df.head())
