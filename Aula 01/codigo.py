import pyautogui
import time

# pyautogui.click > clica em algo
# pyautogui.write > escreve em algum lugar da tela
# pyautogui.press > aperta uma tecla
# pyautogui.hotkey > aperta em um atalho 

# Passo a Passo do programa
# Abrir o Navegador 
pyautogui.PAUSE = 1
pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")
pyautogui.press("Tab")
pyautogui.press("enter")
25.95               
# Abrir link
url = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.hotkey("ctrl", "l")
pyautogui.write(url)
pyautogui.press("enter")
time.sleep(1.5)

# Logar
pyautogui.click(x=3385,y=377)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("Tab")
pyautogui.write("senha")
pyautogui.press("enter")
time.sleep(2)
pyautogui.click(x=3693,y=365)

# Abrir base de dados
# pip install pandas openpyxl
import pandas as pd
tabela = pd.read_csv("produtos.csv")
print(tabela)

# Cadastrar produto
time.sleep(2)

for linha in tabela.index:
    # Codigo
    pyautogui.click(x=3463, y=256)
    codigo = str(tabela.loc[linha,'codigo'])
    pyautogui.write(codigo)
    pyautogui.press("Tab")

    # Marca
    marca = str(tabela.loc[linha,'marca'])
    pyautogui.write(marca)
    pyautogui.press("Tab")

    # Tipo
    tipo = str(tabela.loc[linha,'tipo'])
    pyautogui.write(tipo)
    pyautogui.press("Tab")

    # Custo
    custo = str(tabela.loc[linha,'custo'])
    pyautogui.write(custo)
    pyautogui.press("Tab")

    # Categoria
    categoria = str(tabela.loc[linha,'categoria'])
    pyautogui.write(categoria)
    pyautogui.press("Tab")

    # Preço
    preco = str(tabela.loc[linha,'preco_unitario'])
    pyautogui.write(preco)
    pyautogui.press("Tab")

    # OBS
    obs= str(tabela.loc[linha,'obs'])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("Tab")

    pyautogui.press("enter")
    pyautogui.scroll(5000)