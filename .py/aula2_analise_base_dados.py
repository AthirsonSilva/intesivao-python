#!/usr/bin/env python
# coding: utf-8

# # Análise de Dados com Python
# 
# ### Desafio:
# 
# Você trabalha em uma empresa de telecom e tem clientes de vários serviços diferentes, entre os principais: internet e telefone.
# 
# O problema é que, analisando o histórico dos clientes dos últimos anos, você percebeu que a empresa está com Churn de mais de 26% dos clientes.
# 
# Isso representa uma perda de milhões para a empresa.
# 
# O que a empresa precisa fazer para resolver isso?
# 
# Base de Dados: https://drive.google.com/drive/folders/1T7D0BlWkNuy_MDpUHuBG44kT80EmRYIs?usp=sharing <br>
# Link Original do Kaggle: https://www.kaggle.com/radmirzosimov/telecom-users-dataset

# In[6]:


import pandas as pd

# Passo 1 - importar a base de dados para o python
table = pd.read_csv('../data_bases/telecom_users.csv')

# Passo 2 - Visualizar base de dados
def view_db(table):
    return table.drop("Unnamed: 0", axis = 1)
    
table = view_db(table)


# In[8]:


# Passo 3 - Tratamento de dados
def process_db(table):
    table['TotalGasto'] = pd.to_numeric(table['TotalGasto'], errors = 'coerce')
    table = table.dropna(how = 'all', axis = 1)
    table = table.dropna(how = 'any', axis = 0)
    table = table.drop_duplicates()
    return table
    
table = process_db(table) 


# In[20]:


# Passo 4 - Análise inicial 
def analysis_db(table):
    print(table['Churn'].value_counts())
    print(table['Churn'].value_counts(normalize=True).map('{:.1%}'.format))
    
analysis_db(table)


# In[19]:


# Passo 5 - Análise detalhada
import plotly.express as px

def draw_graphic(table):
    # Criar gráfico
    for column in table.columns:
        graphic = px.histogram(table, x = column, color = 'Churn')
        # Exibir gráfico 
        graphic.show()
    
draw_graphic(table)


# In[18]:


display(table)


# In[67]:





# ### Conclusões e Ações

# - Clientes tem muitas chances de cancelas nos primeiros mese 
#     - 
#     - 
