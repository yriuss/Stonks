# -*- coding: utf-8 -*-
"""
IMPORTANTE:
    instale os modulos: selenium,pyautogui,pyperclip

@author: Adriel Filipe
"""

import time
from selenium import webdriver
import pyautogui as p
import pyperclip as pc
from datetime import datetime
import os.path as path

def abrir_browser(chromedriver_path):
    
    options = webdriver.ChromeOptions()
    
    preferences = {"download.prompt_for_download": False,
                   "download.default_directory": r"C:\stock",
                   "download.directory_upgrade": True,
                   "profile.default_content_settings.popups": 0,
                   "profile.default_content_settings_values.notifications": 2,
                   "profile.default_content_settings_values.automatic_downloads": 1
                  }
    
    options.add_experimental_option("prefs",preferences)
    
    driver = webdriver.Chrome(executable_path = chromedriver_path,
                              options = options)
    
    return driver


def pegar_cotacao(url,nome_arquivo):
    chromedriver_path = "C:\webdrives\chromedriver.exe"
    
    ultimo_preco = retornar_ultimo_preco(nome_arquivo)
    if (ultimo_preco == ''):
        ultimo_preco = -1
    driver = abrir_browser(chromedriver_path)
    
    driver.get(url)
    p.doubleClick(p.Point(98,573))
    p.hotkey("ctrl","c")
    agora = str(datetime.now())
    time.sleep(1)
    
    preco_atual = pc.paste()
    
    preco_atual = preco_atual.replace(',','.')
    
    preco_atual = ''.join(preco_atual)
    
    
    
    if(float(ultimo_preco) != float(preco_atual)):
        armazenar_cotacao(nome_arquivo, preco_atual,agora)
    
    driver.quit()
    
def retornar_ultimo_preco(nome_arquivo):
    arquivo = open(nome_arquivo,'r')
    linha = arquivo.readline()
    count = 0
    ultimo_preco = []
    for i in linha:
        if(i == ' '):
            count = count+1
            
        if(count == 2):
            ultimo_preco.append(i)
    return ''.join(ultimo_preco)
    
def armazenar_cotacao(nome_arquivo,cotacao,agora):
    arquivo = open(nome_arquivo,'a')
    arquivo.write(agora+' ')
    arquivo.write(cotacao+'\n')
    arquivo.close
    return

if(not path.isfile('dolar.txt')):
    open('dolar.txt','w')

if(not path.isfile('wege.txt')):
    open('wege.txt','w')

while(datetime.now().hour < 17):
    url = "https://finance.yahoo.com/quote/usdbrl=X?ltr=1"
    pegar_cotacao(url, 'dolar.txt')
    
    url = "https://finance.yahoo.com/quote/WEGE3.SA/"
    pegar_cotacao(url, 'wege.txt')
print("Programa executado!")
