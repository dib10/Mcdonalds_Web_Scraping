from mcdonalds_scraping import raspagem_cardapio
import pandas as pd
from urls import categorias_urls

# DataFrame para armazenar todos os produtos
df_total = pd.DataFrame()

for categoria, url in categorias_urls.items():
    df = raspagem_cardapio(url, categoria)
    df_total = pd.concat([df_total, df], ignore_index=True)

df_total.to_csv('mcdonalds_menu_total.csv', index=False, encoding='utf-8-sig')
print(df_total)