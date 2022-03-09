#!/usr/bin/env python
# coding: utf-8

# # Automação de Sistemas e Processos com Python
# 
# ### Desafio:
# 
# Todos os dias, o nosso sistema atualiza as vendas do dia anterior.
# O seu trabalho diário, como analista, é enviar um e-mail para a diretoria, assim que começar a trabalhar, com o faturamento e a quantidade de produtos vendidos no dia anterior
# 
# E-mail da diretoria: seugmail+diretoria@gmail.com<br>
# Local onde o sistema disponibiliza as vendas do dia anterior: https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing
# 
# Para resolver isso, vamos usar o pyautogui, uma biblioteca de automação de comandos do mouse e do teclado

# In[31]:


# pip install pyautogui pyperclip
import pyautogui
import pyperclip
from time import sleep

pyautogui.PAUSE = 0.5

# Passo 1 - Entrar no sistema da empresa
def acess():
    pyautogui.hotkey('ctrl', 't')
    pyperclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    sleep(7.5)
    navigate()

# Passo 2 - Navegar no sistema
def navigate():
    pyautogui.click(x = 188, y = 219, clicks = 2)
    sleep(7.5)
    export()

# Passo 3 - Exportar a base de dados
def export():
    pyautogui.click(x = 758, y = 158, clicks = 2)
    pyautogui.click(x = 645, y = 359, clicks = 2)
    
acess()

# pyautogui.press('win')
# pyautogui.write('chrome')
# pyautogui.press('enter')


# ### Vamos agora ler o arquivo baixado para pegar os indicadores
# 
# - Faturamento
# - Quantidade de Produtos

# In[32]:


# Passo 4 - Calcular indicadores (Faturamente e quantidade de produtos vendidos)
# pip install pandas, numpy e openpyxl
import pandas as pd


def read():
    tabela = pd.read_excel(r'C:/Users/Athirson/Downloads/jupyter/vendas-dez.xlsx')
    display(tabela)
    calc()

def calc():
    faturamento = tabela['Valor Final'].sum()
    quantidade = tabela['Quantidade'].sum()
    write()
    
def write():
    print(f'Faturamento = R$ {faturamento:.2f}')
    print(f'Quantidade = R$ {quantidade:.2f}')
    
read()


# In[36]:


# Passo 5 - Enviar email

def acess():
    pyautogui.hotkey('ctrl', 't')
    pyperclip.copy('https://mail.google.com/mail/u/0/#inbox')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    sleep(7.5)
    send_to()
    
def send_to():
    pyautogui.click(x=94, y=187, clicks=2)
    sleep(7.5)
    pyautogui.write('Athirsonplayer2@gmail.com')
    sleep(1)
    pyautogui.press('tab')
    sleep(5)
    write_title()
    
def write_title():
    pyautogui.press('tab')
    pyautogui.write('Relatorio de vendas')
    sleep(3)
    write_text()
    
def write_text():
    pyautogui.press('tab')
    text = f'''
    Prezados, bom dia
    
    O faturamento de ontem foi de R$ {faturamento:.2f}
    E a quantidade de produtos vendidos foi de: {quantidade}
    
    Abs
    Athirson Silva
    '''
    pyperclip.copy(text)
    pyautogui.hotkey('ctrl', 'v')
    sleep(0.5)
    pyautogui.hotkey('ctrl', 'enter')
    
def get_file():
    pyautogui.click(x=537, y=739, clicks=2)
    sleep(1)
    pyautogui.click(x=272, y=239, clicks=2)
    sleep(1)
    pyautogui.click(x=257, y=209, clicks=2)
    sleep(1)

    
    
    
    
acess()


# In[34]:


pyautogui.press('win') 
pyautogui.write('chrome')
pyautogui.press('enter')


# ### Vamos agora enviar um e-mail pelo gmail

# In[35]:


sleep(5)
pyautogui.position()


# #### Use esse código para descobrir qual a posição de um item que queira clicar
# 
# - Lembre-se: a posição na sua tela é diferente da posição na minha tela

# In[ ]:




