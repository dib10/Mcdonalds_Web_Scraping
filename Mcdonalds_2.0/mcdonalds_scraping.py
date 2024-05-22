import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
# options.add_argument('--headless')
options.add_argument('window-size=400,800')

navegador = webdriver.Chrome(options=options)


sleep(1)

navegador.get('https://www.mcdonalds.com.br/cardapio')

# Verifique se a classe 'mcd-category-menu' existe na página
cardapio = navegador.find_element(By.CLASS_NAME, 'mcd-category-menu')
# Usar um seletor CSS mais específico
categorias = cardapio.find_elements(By.CSS_SELECTOR, '.column.is-narrow-mobile.is-narrow-tablet.is-12-desktop')

for categoria in categorias:
    if categoria.text == 'McLanche Feliz' or categoria.text == 'McOferta' or categoria.text == 'Méqui Box':
        continue
    categoria.click()
    sleep(2)




# Para pegar o html da página, descomente abaixo
# page_content = navegador.page_source
# site = BeautifulSoup(page_content, 'html.parser')
# print(site.prettify())








