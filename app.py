import streamlit as st
import pandas as pd
import plotly.express as px

hr = st.markdown("""
<hr>
""", unsafe_allow_html=True)

# Remova a palavra 'kcal' da coluna 'Calorias' e converta para numérico
df = pd.read_csv('mcdonalds_nutricional.csv')  # Certifique-se de ajustar o nome do arquivo CSV
df['Calorias'] = pd.to_numeric(df['Calorias'].str.replace('kcal', ''), errors='coerce')

# Ordenando o DataFrame pela coluna 'Calorias' em ordem decrescente
df_sorted = df.sort_values('Calorias', ascending=False)

st.markdown("""
<p style='font-size: 20px;'>
Impulsionado por café e código. 
Se você gostou do meu trabalho, considere <a href='https://buymeacoffee.com/dib10'>comprar um café para mim</a> ☕
</p>
<hr>
""", unsafe_allow_html=True)
# Título principal
st.title('🍔🍟 Cardápio Nutricional do McDonalds')

# Exibir o DataFrame completo
st.write(df)
st.markdown("<hr>", unsafe_allow_html=True)

# Função para exibir gráficos e dados
def exibir_categoria_com_grafico(titulo, categoria, colunas_para_exibir):
    st.title(titulo)
    categoria_df = df_sorted[df_sorted['Categoria'] == categoria]
    # Selecione apenas as colunas que você deseja exibir
    categoria_df = categoria_df[colunas_para_exibir]
    # Exiba o DataFrame sem índices
    st.write(categoria_df.set_index('Produto'))
    fig = px.bar(categoria_df, x='Produto', y='Calorias', color='Calorias', color_continuous_scale=["#FFC72C", "#DA291C"])
    fig.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig)
    st.markdown("<hr>", unsafe_allow_html=True)

# Título principal
st.title('〽️🍔 Os 10 produtos mais calóricos do cardápio do McDonalds')

# Filtrando os dados para exibir apenas as colunas necessárias
df_filtrado = df_sorted[['Categoria', 'Produto', 'Calorias']]

# Exibindo os 10 produtos mais calóricos
st.write(df_filtrado.head(10).set_index('Produto'))
# Gráfico dos 10 produtos mais calóricos
fig = px.bar(df_sorted.head(10), x='Produto', y='Calorias', color='Calorias', color_continuous_scale=["#FFC72C", "#DA291C"])
fig.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig)
st.markdown("<hr>", unsafe_allow_html=True)


# Exibindo categorias
exibir_categoria_com_grafico('🐂 Sanduíches de carne bovina mais calóricos', 'Sanduíches de Carne Bovina', ['Produto', 'Calorias'])
exibir_categoria_com_grafico('🍔 Brabos do Méqui mais calóricos', 'Brabos do Méqui', ['Produto', 'Calorias'])
exibir_categoria_com_grafico('🍔 Família Tasty mais calórica', 'Família Tasty', ['Produto', 'Calorias'])
exibir_categoria_com_grafico('🐔 Sanduíches de frango mais calóricos', 'Sanduíches de Frango', ['Produto', 'Calorias'])
exibir_categoria_com_grafico('🍟 Acompanhamentos mais calóricos', 'Acompanhamentos', ['Produto', 'Calorias'])
exibir_categoria_com_grafico('🍨 Sobremesas mais calóricas', 'Sobremesas', ['Produto', 'Calorias'])
exibir_categoria_com_grafico('🥤 Bebidas frias mais calóricas', 'Bebidas Frias', ['Produto', 'Calorias'])
exibir_categoria_com_grafico('☕️ Bebidas quentes mais calóricas', 'Bebidas Quentes', ['Produto', 'Calorias'])
exibir_categoria_com_grafico('🍳 Café da manhã mais calórico', 'Café da Manhã', ['Produto', 'Calorias'])
exibir_categoria_com_grafico('☕️ McCafé mais calórico', 'McCafé', ['Produto', 'Calorias'])

# Adicionando nota de rodapé
st.markdown("""
Impulsionado por ☕ e código. Feito com carinho por Caio Dib
""")
