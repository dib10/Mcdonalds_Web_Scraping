import streamlit as st
import pandas as pd
import plotly.express as px

# Carregue seus dados em um DataFrame
df = pd.read_csv('mcdonalds_nutricional.csv')

#título
st.title('〽️🍔 Os 10 produtos mais calóricos do cardápio do Mcdonalds')

# Remova a palavra 'kcal' da coluna 'Calorias'
df['Calorias'] = df['Calorias'].str.replace('kcal', '')

# Converta a coluna 'Calorias' para numérico
df['Calorias'] = pd.to_numeric(df['Calorias'], errors='coerce')

# Ordenando o DataFrame pela coluna 'Calorias' em ordem decrescente
df_sorted = df.sort_values('Calorias', ascending=False)

# Mostrando os 10 produtos mais calóricos
st.dataframe(df_sorted.head(10))

# Gráfico 
fig = px.bar(df_sorted.head(10), x='Produto', y='Calorias', color='Calorias', 
             color_continuous_scale=["#FFC72C", "#DA291C"])
fig.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig)

#Sanduíches de carne bovina mais calóricos
st.title(' 🐂 Sanduíches de carne bovina mais calóricos')

# Filtrando apenas os sanduíches de carne bovina
sanduiches = df_sorted[df_sorted['Categoria'] == 'Sanduíches de Carne Bovina']

# Mostrando todos os sanduíches de carne bovina
st.dataframe(sanduiches)

# Gráfico
fig = px.bar(sanduiches, x='Produto', y='Calorias', color='Calorias', 
             color_continuous_scale=["#FFC72C", "#DA291C"])
fig.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig)

#Brabos do Méqui

st.title('🍔 Brabos do Méqui mais calóricos')

# Filtrando apenas os Brabos do Méqui
brabos = df_sorted[df_sorted['Categoria'] == 'Brabos do Méqui']

# Mostrando todos os Brabos do Méqui
st.dataframe(brabos)

# Gráfico
fig = px.bar(brabos, x='Produto', y='Calorias', color='Calorias', 
             color_continuous_scale=["#FFC72C", "#DA291C"])
fig.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig)

#Família Tasty 

st.title('🍔 Família Tasty mais calórica')

# Filtrando apenas a Família Tasty
familia_tasty = df_sorted[df_sorted['Categoria'] == 'Família Tasty']

# Mostrando todos os itens da Família Tasty
st.dataframe(familia_tasty)

# Gráfico
fig = px.bar(familia_tasty, x='Produto', y='Calorias', color='Calorias', 
             color_continuous_scale=["#FFC72C", "#DA291C"])
fig.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig)



#Sanduíches de frango mais calóricos
st.title('🐔 Sanduíches de frango mais calóricos')

# Filtrando apenas os sanduíches de frango
sanduiches = df_sorted[df_sorted['Categoria'] == 'Sanduíches de Frango']  

# Mostrando todos os sanduíches de frango
st.dataframe(sanduiches)

# Gráfico
fig = px.bar(sanduiches, x='Produto', y='Calorias', color='Calorias', 
             color_continuous_scale=["#FFC72C", "#DA291C"])
fig.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig)

#Acompanhamentos
st.title('🍟 Acompanhamentos mais calóricos')

# Filtrando apenas os acompanhamentos
acompanhamentos = df_sorted[df_sorted['Categoria'] == 'Acompanhamentos']

# Mostrando todos os acompanhamentos
st.dataframe(acompanhamentos)

# Gráfico
fig = px.bar(acompanhamentos, x='Produto', y='Calorias', color='Calorias', 
             color_continuous_scale=["#FFC72C", "#DA291C"])
fig.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig)

#Sobremesas

st.title('🍨 Sobremesas mais calóricas')

# Filtrando apenas as sobremesas
sobremesas = df_sorted[df_sorted['Categoria'] == 'Sobremesas']

# Mostrando todas as sobremesas
st.dataframe(sobremesas)

# Gráfico
fig = px.bar(sobremesas, x='Produto', y='Calorias', color='Calorias', 
             color_continuous_scale=["#FFC72C", "#DA291C"])
fig.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig)

#Bebidas frias

st.title('🥤 Bebidas frias mais calóricas')

# Filtrando apenas as bebidas frias
bebidas_frias = df_sorted[df_sorted['Categoria'] == 'Bebidas Frias']

# Mostrando todas as bebidas frias
st.dataframe(bebidas_frias)

# Gráfico
fig = px.bar(bebidas_frias, x='Produto', y='Calorias', color='Calorias', 
             color_continuous_scale=["#FFC72C", "#DA291C"])
fig.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig)

#Bebidas quentes

st.title('☕️ Bebidas quentes mais calóricas')

# Filtrando apenas as bebidas quentes
bebidas_quentes = df_sorted[df_sorted['Categoria'] == 'Bebidas Quentes']

# Mostrando todas as bebidas quentes
st.dataframe(bebidas_quentes)

# Gráfico
fig = px.bar(bebidas_quentes, x='Produto', y='Calorias', color='Calorias', 
             color_continuous_scale=["#FFC72C", "#DA291C"])
fig.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig)

#Café da manhã

st.title('🍳 Café da manhã mais calórico')

# Filtrando apenas os itens do café da manhã

cafe_da_manha = df_sorted[df_sorted['Categoria'] == 'Café da Manhã']

# Mostrando todos os itens do café da manhã
st.dataframe(cafe_da_manha)

# Gráfico
fig = px.bar(cafe_da_manha, x='Produto', y='Calorias', color='Calorias', 
             color_continuous_scale=["#FFC72C", "#DA291C"])

fig.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig)


#McCafé


st.title('☕️ McCafé mais calórico')

# Filtrando apenas os itens do McCafé
mccafe = df_sorted[df_sorted['Categoria'] == 'McCafé']

# Mostrando todos os itens do McCafé
st.dataframe(mccafe)

# Gráfico
fig = px.bar(mccafe, x='Produto', y='Calorias', color='Calorias', 
             color_continuous_scale=["#FFC72C", "#DA291C"])
fig.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig)


