# Importações
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd

# Configurando o Selenium
options = Options()
options.add_argument('window-size=400,800')

navegador = webdriver.Chrome(options=options)
# Não altere o tempo de espera, pois o site pode crashar
sleep(0.5)

# Passando a URL do cardápio. Obs:. Você deve passar a url do primeiro elemento da categoria que aparece no cardápio, nesse caso, são os lançamentos.
navegador.get('https://www.mcdonalds.com.br/cardapio/lancamentos')

# Identificando onde fica o cardápio com categorias
cardapio = navegador.find_element(By.CLASS_NAME, 'mcd-category-menu')
# Encontrando o nome de cada categoria
categorias = cardapio.find_elements(By.CSS_SELECTOR, '.column.is-narrow-mobile.is-narrow-tablet.is-12-desktop') 

# Lista de categorias que não deve ser percorrida, adicione aqui as categorias que não deseja obter os produtos
ignorar_categoria = ['Nossos produtos','Lançamentos','McLanche Feliz', 'McOferta', 'Méqui Box']

# Criando dataframe para armazenar as informações nutricionais
df = pd.DataFrame()
index_categoria = 0
while True: # Enquanto houver categorias para percorrer
    cardapio = navegador.find_element(By.CLASS_NAME, 'mcd-category-menu') 
    categorias = cardapio.find_elements(By.CSS_SELECTOR, '.column.is-narrow-mobile.is-narrow-tablet.is-12-desktop')
    # Se já percorreu todas as categorias, sair do loop, pois não há mais categorias para percorrer
    if index_categoria >= len(categorias):
        break
    
    categoria = categorias[index_categoria]
    nome_categoria = categoria.text
    # Se a categoria estiver na lista de categorias a ser ignorada, passar para a próxima categoria
    if nome_categoria in ignorar_categoria: 
        index_categoria += 1
        continue
    categoria.click()
    sleep(0.5)
    # Encontrando os produtos da categoria
    div_dos_produtos = navegador.find_element(By.CLASS_NAME, 'columns.is-mobile.is-multiline.is-centered.is-gapless')
    # Encontrando os produtos individualmente
    produto_individual = navegador.find_elements(By.CSS_SELECTOR, '.mcd-category-detail__item')

    for i in range(len(produto_individual)):
        produto_individual = navegador.find_elements(By.CSS_SELECTOR, '.mcd-category-detail__item')
        produto_individual[i].click() # i representa o índice do produto na lista de produtos da categoria
        # sleep(1)

        # Extraindo nome do produto
        obter_nome_do_produto = navegador.find_element(By.CSS_SELECTOR, '.mcd-product-detail__summary h1').text
        clicar_info_nutricional = navegador.find_element(By.CSS_SELECTOR, '.mcd-collapsable-item.mcd-collapsable-item--nutritional')
        clicar_info_nutricional.click()
        # sleep(1)

        # Identificando informações nutricionais
        div_info_nutricional = navegador.find_element(By.CSS_SELECTOR, '.mcd-nutritional-information__summary')
        # a tag p contém o nome da informação nutricional e a tag h3 contém o valor
        info_nutricionais_nomes = [p.text for p in div_info_nutricional.find_elements(By.TAG_NAME, 'p')]
        valores = [h3.text for h3 in div_info_nutricional.find_elements(By.TAG_NAME, 'h3')]

        # Criando um dicionário com as informações nutricionais
        info_nutricional = {
            'Categoria': nome_categoria,
            'Produto': obter_nome_do_produto
        }
        for nome, valor in zip(info_nutricionais_nomes, valores):
            info_nutricional[nome] = valor

        df = pd.concat([df, pd.DataFrame([info_nutricional])], ignore_index=True)

        # print(info_nutricional)
        # print('-----------------------------------')

        navegador.back()
        # sleep(1)

    navegador.back()
    # sleep(1)

    index_categoria += 1

# Gerando um arquivo CSV com as informações nutricionais
df.to_csv('mcdonalds_nutricional.csv', index=False, encoding='utf-8-sig')
