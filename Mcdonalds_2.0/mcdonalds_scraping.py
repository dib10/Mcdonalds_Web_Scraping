import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.by import By
################### CONFIGURANDO O SELENIUM ###################

options = Options()
# options.add_argument('--headless')
options.add_argument('window-size=400,800')

navegador = webdriver.Chrome(options=options)


sleep(1)

navegador.get('https://www.mcdonalds.com.br/cardapio/lancamentos')


################### CONFIGURANDO O SELENIUM ###################

###################  Navegando e clicando nas categorias do cardápio, obs: as categorias ficam num menu lateral esquerdo e não some ################### 

# Verifique se a classe 'mcd-category-menu' existe na página
cardapio = navegador.find_element(By.CLASS_NAME, 'mcd-category-menu')
# Usar um seletor CSS mais específico
categorias = cardapio.find_elements(By.CSS_SELECTOR, '.column.is-narrow-mobile.is-narrow-tablet.is-12-desktop')

ignorar_categoria = ['McLanche Feliz', 'McOferta', 'Méqui Box'] #adicione aqui as categorias que você quer ignorar

# for categoria in categorias:
#     if categoria.text in ignorar_categoria:
#         continue
#     categoria.click()
#     sleep(2)


################### Navegando e clicando nas categorias do cardápio, obs: as categorias ficam num menu lateral esquerdo e não some ###################


################### Após clicar nas categorias, devemos percorrer cada item e clicar nele ################


div_dos_produtos = navegador.find_element(By.CLASS_NAME, 'columns.is-mobile.is-multiline.is-centered.is-gapless')

# Obter a lista de produtos
produto_individual = navegador.find_elements(By.CSS_SELECTOR, '.mcd-category-detail__item')

# Clicando em cada produto e obtendo dados
for i in range(len(produto_individual)):
    # Reobter a lista de produtos
    produto_individual = navegador.find_elements(By.CSS_SELECTOR, '.mcd-category-detail__item')
    # Clicar no produto
    produto_individual[i].click()
    sleep(2)
    # Encontrar o local que clica para abrir as informações nutricionais 

    # Obter o nome do produto
    obter_nome_do_produto = navegador.find_element(By.CSS_SELECTOR, '.mcd-product-detail__summary h1').text
    
    clicar_info_nutricional = navegador.find_element(By.CSS_SELECTOR, '.mcd-collapsable-item.mcd-collapsable-item--nutritional')
    
    # Clicando no botao de informações nutricionais
    clicar_info_nutricional.click()
    
    sleep(2)
    
    # Obter as informações nutricionais
    div_info_nutricional = navegador.find_element(By.CSS_SELECTOR, '.mcd-nutritional-information__summary')
    
    # Encontrar todas as tags <p> e <h3> dentro da div
    info_nutricionais_nomes = [p.text for p in div_info_nutricional.find_elements(By.TAG_NAME, 'p')]
    valores = [h3.text for h3 in div_info_nutricional.find_elements(By.TAG_NAME, 'h3')]
    
    # Criar um dicionário com as info_nutricionais_nomes e valores
    info_nutricional = {info_nutricionais_nomes: valor for info_nutricionais_nomes, valor in zip(info_nutricionais_nomes, valores)}
    
    # Adicionar o nome do produto ao dicionário
    info_nutricional['Produto'] = obter_nome_do_produto
    
    print(info_nutricional)
    print('-----------------------------------')
    
    # Voltar para a página anterior
    navegador.back()
    sleep(2)



# Para pegar o html da página, descomente abaixo
# page_content = navegador.page_source
# site = BeautifulSoup(page_content, 'html.parser')
# print(site.prettify())