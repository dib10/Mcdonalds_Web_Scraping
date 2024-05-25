#Configurando Selenium e importações

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
