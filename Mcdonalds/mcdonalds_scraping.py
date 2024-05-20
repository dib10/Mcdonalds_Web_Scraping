import re
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

def raspagem_cardapio(url, categoria):
    # Iniciando o driver do Selenium
    driver = webdriver.Firefox()  # aqui eu uso o driver do Firefox, mas você pode usar o do Chrome também

    driver.get(url)  # Acessando a URL

    html = driver.page_source  # Código fonte da página para o BeautifulSoup

    driver.quit()  # Fechar o navegador após a raspagem

    site = BeautifulSoup(html, 'html.parser')  # Parse do Html -> transformando o código numa estrutura mais fácil de manipular

    cardapio = site.find('div', attrs={'class': 'flickity-slider'})  # Encontramos o elemento que possui o cardápio em formato de slider

    dados = []  # Lista para armazenar os dados

    # Capturar informações do primeiro produto na página, pois o slider é de produtos relacioandos ao primeiro produto
    primeiro_produto = site.find('div', class_='mcd-product-detail__summary')

    if primeiro_produto:
        # Extrair informações do primeiro produto
        nome_primeiro_produto = primeiro_produto.find('h1').get_text(strip=True)
        calorias_primeiro_produto = primeiro_produto.find('h5').get_text(strip=True)

        # Adicionar os dados do primeiro produto à lista com a categoria correta
        dados.append({'Categoria': categoria, 'Nome do Produto': nome_primeiro_produto, 'Calorias': calorias_primeiro_produto})

    # Se o slider estiver presente, iterar sobre os produtos nele
    if cardapio:
        # Percorrer todas as divs externas
        for div_externa in cardapio.find_all('div', attrs={'class': 'mcd-related-product__title'}):
            # Encontrar a div interna dentro da div externa
            div_interna = div_externa.find_next('div', attrs={'class': 'mcd-related-product__calories is-hidden-touch'})

            # Extrair o texto completo da div externa
            texto_div_externa = div_externa.get_text(strip=True)

            # Extrair o texto da div interna
            texto_calorias = div_interna.get_text(strip=True) if div_interna else ''

            # Subtrair o texto das calorias do texto completo para obter apenas o nome do lanche/produto
            nome_produto = texto_div_externa.replace(texto_calorias, '').strip()

            # Adicionar os dados à lista
            dados.append({'Categoria': categoria, 'Nome do Produto': nome_produto, 'Calorias': texto_calorias})

    # Criar um DataFrame do pandas com os dados
    df = pd.DataFrame(dados)

    return df
