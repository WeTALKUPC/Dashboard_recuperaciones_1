import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título del dashboard
st.title("Dashboard de Cumplimiento por Feriado y Programa")

# Cargar el archivo Excel directamente desde el repositorio
DATA_URL = "https://github.com/WeTALKUPC/Dashboard_recuperaciones_1/blob/main/RECUPERACIONES%20FERIADOS%20V1.xlsx"
df = pd.read_excel(DATA_URL)

# Mostrar vista previa de los datos
st.subheader("Vista previa de los datos")
st.write(df.head())

# Lista de feriados
feriados = df.columns[2:-1]

# Selector de feriado
feriado = st.selectbox("Selecciona un feriado:", feriados)

# Lista de programas
programas = df["PROGRAMA"].unique()
programa = st.selectbox("Selecciona un programa:", ["TODOS"] + list(programas))

# Limpiar los datos
df[feriado] = df[feriado].str.strip().str.upper()

# Filtrar por programa
if programa != "TODOS":
    df = df[df["PROGRAMA"] == programa]

# Calcular el porcentaje de cumplimiento
cumplimiento = df[feriado].value_counts(normalize=True) * 100

# Mostrar gráfico
st.subheader(f"Cumplimiento para {feriado} ({programa})")
st.bar_chart(cumplimiento)

# Descargar datos filtrados
st.subheader("Descargar datos filtrados")
csv = df.to_csv(index=False)
st.download_button(
    label="Descargar CSV",
    data=csv,
    file_name="datos_filtrados.csv",
    mime="text/csv",
)

