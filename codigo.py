import pyautogui
import time
#pyautogui é uma biblioteca que automatiza o mouse, o teclado e o computador.
#Para instalar só é digitar no terminal do vscode "pip install pyautogui"
#pyautogui.click
#pyautogui.write
#pyautogui.press - apertar 1 tecla
#pyautogui.hotkey - combinação de tecla
#pyautogui.scroll - rolar a tela

pyautogui.PAUSE = 0.5

# passo 1 - entrar no site
# abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

#entrar no link https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)

# passo 2 - fazer login
pyautogui.click(x=1129, y=476 )
pyautogui.hotkey("ctrl", "a")
pyautogui.write("kommungyoung@gmail.com")

# passar para o campo de senha
pyautogui.press("tab")
pyautogui.write("dorama")

pyautogui.click(x=1430, y=648)

time.sleep(3)

# passo 3 - Importar a base de dados
#pandas é um pacote de códigos para trabalhar com base de dados e volumes de dados seja csv, excel, sql...
#pip install pandas openpyxl numpy
#tabula ou PyPDF que consegue ler um pdf e transformar em uma base do pandas.
import pandas
# Caso o arquivo "produtos.csv" esteja em Downloads, por exemplo, e não dentro da pasta faz assim:
# tabela = pandas.read_csv("C://Users/marci/Downloads/produtos.csv")
tabela = pandas.read_csv("produtos.csv")

print(tabela)

# passo 4 - cadastrar o produto
# para cada linha da minha tabela
for linha in tabela.index:
    #código
    pyautogui.click(x=1117, y=343)

    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)

    #marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    pyautogui.write(marca)

    #tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    pyautogui.write(tipo)

    #categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.press("tab")
    pyautogui.write(categoria)

    #preço
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.press("tab")
    pyautogui.write(preco)

    #custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.press("tab")
    pyautogui.write(custo)

    #observação
    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter") 
    
    pyautogui.scroll(5000)

# passo 5 - repetir para todos os produtos, para todas as linhas da tabela