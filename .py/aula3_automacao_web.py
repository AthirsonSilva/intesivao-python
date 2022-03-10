#!/usr/bin/env python
# coding: utf-8

# # Automação Web e Busca de Informações com Python
# 
# #### Desafio: 
# 
# Trabalhamos em uma importadora e o preço dos nossos produtos é vinculado a cotação de:
# - Dólar
# - Euro
# - Ouro
# 
# Precisamos pegar na internet, de forma automática, a cotação desses 3 itens e saber quanto devemos cobrar pelos nossos produtos, considerando uma margem de contribuição que temos na nossa base de dados.
# 
# Base de Dados: https://drive.google.com/drive/folders/1KmAdo593nD8J9QBaZxPOG1yxHZua4Rtv?usp=sharing
# 
# Para isso, vamos criar uma automação web:
# 
# - Usaremos o selenium
# - Importante: baixar o webdriver

# In[10]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Criar a navegador
browser = webdriver.Chrome()

# Entrar no google
browser.get('https://www.google.com/')

# Encontrar o input
browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação dólar')
browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

# Selecionar cotação do dólar
dolar = browser.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(dolar)

# Encontrar o input
browser.get('https://www.google.com/')
browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação euro')
browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

# Selecionar cotação do euro
euro = browser.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(euro)

# Encontrar o input
browser.get('https://www.melhorcambio.com/ouro-hoje')

# Selecionar cotação do ouro
gold = browser.find_element(By.XPATH, '//*[@id="comercial"]').get_attribute("value")
gold = gold.replace(",", ".")
print(gold)

browser.quit()


# ### Agora vamos atualiza a nossa base de preços com as novas cotações

# - Importando a base de dados

# In[11]:


# Importando a base de dados
import pandas as pd

table = pd.read_excel('../data_bases/Produtos.xlsx')
display(table)


# - Atualizando os preços e o cálculo do Preço Final

# In[12]:


# Passo 5: Recalcular o preço de cada produto
# atualizar a cotação
# nas linhas onde na coluna "Moeda" = Dólar
table.loc[table["Moeda"] == "Dólar", "Cotação"] = float(dolar)
table.loc[table["Moeda"] == "Euro", "Cotação"] = float(euro)
table.loc[table["Moeda"] == "Ouro", "Cotação"] = float(gold)

# atualizar o preço base reais (preço base original * cotação)
table["Preço de Compra"] = table["Preço Original"] * table["Cotação"]

# atualizar o preço final (preço base reais * Margem)
table["Preço de Venda"] = table["Preço de Compra"] * table["Margem"]

# tabela["Preço de Venda"] = tabela["Preço de Venda"].map("R${:.2f}".format)

display(table)


# ### Agora vamos exportar a nova base de preços atualizada

# In[13]:


# Passo 6: Salvar os novos preços dos produtos
table.to_excel("Produtos Novo.xlsx", index=False)

