import streamlit as st
import pandas as pd
# Configurar matplotlib para que funcione en entornos sin interfaz gráfica
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
# URLs de los archivos CSV (reemplaza TU_USUARIO por tu usuario real de GitHub)
base_url = "https://raw.githubusercontent.com/TU_USUARIO/Dashboard-ChocolateExport/main/"
clientes_url = base_url + "clientes.csv"
mercados_url = base_url + "mercados.csv"
exportaciones_url = base_url + "exportaciones.csv"
barreras_url = base_url + "barreras.csv"
# Cargar los datos
clientes = pd.read_csv(clientes_url)
mercados = pd.read_csv(mercados_url)
exportaciones = pd.read_csv(exportaciones_url)
barreras = pd.read_csv(barreras_url)
# Título del Dashboard
st.title("Dashboard Interactivo de Exportaciones de Chocolates")
# Filtro de país
paises = exportaciones["País"].unique()
pais_seleccionado = st.selectbox("Selecciona un país para ver los detalles", paises)
# Mostrar datos de clientes
st.subheader("Clientes")
clientes_filtrados = clientes[clientes["País"] == pais_seleccionado]
st.dataframe(clientes_filtrados)
# Mostrar datos de exportaciones
st.subheader("Exportaciones de Chocolates")
exportaciones_filtradas = exportaciones[exportaciones["País"] == pais_seleccionado]
fig, ax = plt.subplots()
ax.bar(["Exportaciones"], exportaciones_filtradas["Exportaciones (USD millones)"], color='#2E86C1')
ax.set_ylabel("Exportaciones (USD millones)")
ax.set_title(f"Exportaciones de Chocolates en {pais_seleccionado}")
st.pyplot(fig)
# Mostrar datos de mercados
st.subheader("Segmentos de Mercado")
mercados_filtrados = mercados[mercados["País"] == pais_seleccionado]
st.dataframe(mercados_filtrados)
# Mostrar barreras de entrada
st.subheader("Barreras de Entrada")
barreras_filtradas = barreras[barreras["País"] == pais_seleccionado]
st.dataframe(barreras_filtradas)
# Análisis Comparativo
st.subheader("Análisis Comparativo")
# Agrupar por país si hay varios segmentos por país
mercado_total = mercados.groupby("País")["Tamaño del Mercado (USD millones)"].sum().reset_index()
fig2, ax2 = plt.subplots(figsize=(8, 5))
ax2.bar(mercado_total["País"], mercado_total["Tamaño del Mercado (USD millones)"], color='#F39C12')
ax2.set_xlabel("País")
ax2.set_ylabel("Tamaño del Mercado (USD millones)")
ax2.set_title("Comparación de Tamaños de Mercado")
plt.xticks(rotation=45)
st.pyplot(fig2)
