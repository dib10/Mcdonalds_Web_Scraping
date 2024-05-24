#Importações
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

#Configurando o Selenium
options = Options()
options.add_argument('window-size=400,800')

navegador = webdriver.Chrome(options=options)

sleep(1)

navegador.get('https://www.mcdonalds.com.br/cardapio/lancamentos')

cardapio = navegador.find_element(By.CLASS_NAME, 'mcd-category-menu')
categorias = cardapio.find_elements(By.CSS_SELECTOR, '.column.is-narrow-mobile.is-narrow-tablet.is-12-desktop')

ignorar_categoria = ['Nossos produtos','Lançamentos','McLanche Feliz', 'McOferta', 'Méqui Box']

index_categoria = 0
while True:
    cardapio = navegador.find_element(By.CLASS_NAME, 'mcd-category-menu')
    categorias = cardapio.find_elements(By.CSS_SELECTOR, '.column.is-narrow-mobile.is-narrow-tablet.is-12-desktop')

    if index_categoria >= len(categorias):
        break

    categoria = categorias[index_categoria]
    nome_categoria = categoria.text
    if nome_categoria in ignorar_categoria:
        index_categoria += 1
        continue
    categoria.click()
    sleep(0.5)

    div_dos_produtos = navegador.find_element(By.CLASS_NAME, 'columns.is-mobile.is-multiline.is-centered.is-gapless')
    produto_individual = navegador.find_elements(By.CSS_SELECTOR, '.mcd-category-detail__item')

    for i in range(len(produto_individual)):
        produto_individual = navegador.find_elements(By.CSS_SELECTOR, '.mcd-category-detail__item')
        produto_individual[i].click()
        sleep(0.5)

        obter_nome_do_produto = navegador.find_element(By.CSS_SELECTOR, '.mcd-product-detail__summary h1').text
        clicar_info_nutricional = navegador.find_element(By.CSS_SELECTOR, '.mcd-collapsable-item.mcd-collapsable-item--nutritional')
        clicar_info_nutricional.click()
        sleep(0.5)

        div_info_nutricional = navegador.find_element(By.CSS_SELECTOR, '.mcd-nutritional-information__summary')
        info_nutricionais_nomes = [p.text for p in div_info_nutricional.find_elements(By.TAG_NAME, 'p')]
        valores = [h3.text for h3 in div_info_nutricional.find_elements(By.TAG_NAME, 'h3')]

        info_nutricional = {info_nutricionais_nomes: valor for info_nutricionais_nomes, valor in zip(info_nutricionais_nomes, valores)}
        info_nutricional['Produto'] = obter_nome_do_produto
        info_nutricional['Categoria'] = nome_categoria

        print(info_nutricional)
        print('-----------------------------------')

        navegador.back()
        sleep(0.5)

    navegador.back()
    sleep(0.5)

    index_categoria += 1