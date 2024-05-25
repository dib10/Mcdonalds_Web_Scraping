import streamlit as st
import pandas as pd
import plotly.express as px

# Carregue seus dados em um DataFrame
df = pd.read_csv('mcdonalds_nutricional.csv')

# Remova a palavra 'kcal' da coluna 'Calorias' e converta para numérico
df['Calorias'] = pd.to_numeric(df['Calorias'].str.replace('kcal', ''), errors='coerce')

# Ordenando o DataFrame pela coluna 'Calorias' em ordem decrescente
df_sorted = df.sort_values('Calorias', ascending=False)

# Função para exibir gráficos e dados
def exibir_categoria(titulo, categoria):
    st.title(titulo)
    categoria_df = df_sorted[df_sorted['Categoria'] == categoria]
    st.dataframe(categoria_df)
    fig = px.bar(categoria_df, x='Produto', y='Calorias', color='Calorias', 
                 color_continuous_scale=["#FFC72C", "#DA291C"])
    fig.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig)

# Título principal
st.title('〽️🍔 Os 10 produtos mais calóricos do cardápio do McDonalds')

# Mostrando os 10 produtos mais calóricos
st.dataframe(df_sorted.head(10))

# Gráfico dos 10 produtos mais calóricos
fig = px.bar(df_sorted.head(10), x='Produto', y='Calorias', color='Calorias', 
             color_continuous_scale=["#FFC72C", "#DA291C"])
fig.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig)

# Exibindo categorias
exibir_categoria('🐂 Sanduíches de carne bovina mais calóricos', 'Sanduíches de Carne Bovina')
exibir_categoria('🍔 Brabos do Méqui mais calóricos', 'Brabos do Méqui')
exibir_categoria('🍔 Família Tasty mais calórica', 'Família Tasty')
exibir_categoria('🐔 Sanduíches de frango mais calóricos', 'Sanduíches de Frango')
exibir_categoria('🍟 Acompanhamentos mais calóricos', 'Acompanhamentos')
exibir_categoria('🍨 Sobremesas mais calóricas', 'Sobremesas')
exibir_categoria('🥤 Bebidas frias mais calóricas', 'Bebidas Frias')
exibir_categoria('☕️ Bebidas quentes mais calóricas', 'Bebidas Quentes')
exibir_categoria('🍳 Café da manhã mais calórico', 'Café da Manhã')
exibir_categoria('☕️ McCafé mais calórico', 'McCafé')
