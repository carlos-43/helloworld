import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write con mi df')
st.write('Hola')

st.write(2025)

df_mio = pd.DataFrame({
    'Nombre': ['Ana', 'Luis', 'Carlos', 'Marta'],
    'Edad': [23, 35, 29, 41],
    'Ciudad': ['Madrid', 'Bogotá', 'CDMX', 'Lima']
})
st.write(df_mio)

st.write('Este es mi df:', df_mio, '.')

df_numerico = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['x', 'y', 'tamaño']
)
grafico = alt.Chart(df_numerico).mark_circle().encode(
    x='x', y='y', size='tamaño', color='tamaño', tooltip=['x', 'y', 'tamaño']
)
st.write(grafico)
