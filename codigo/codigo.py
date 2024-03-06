# Passo a Passo do projeto
# Passo 1: entrar no sistema da empresa
    #https://dlp.hashtagtreinamentos.com/python/intensivao/login
#pip install pyautogui
import pyautogui
import pandas

# Abrir o navegador
#pyautogui.hotkey() -> combinação de tecla
pyautogui.PAUSE = 1.0
pyautogui.press("win")
pyautogui.write("firefox")
pyautogui.press("enter") 

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)

pyautogui.press("enter")

# Passo 2: fazer login
pyautogui.click(x=777, y=404)
pyautogui.write("emailtest@gmail.com")
pyautogui.press("tab")
pyautogui.write("123456789")
pyautogui.press("tab")
pyautogui.press("enter")

# Passo 3: Importar a base de dados 
# install pandas numpy openpyxl
arquivo = pandas.read_csv("produtos.csv")
# print(arquivo)

# Passo 4: Cadastrar produto
# para cada linha na tabela
for linha in arquivo.index:
    # clicar no campo
    pyautogui.click(x=879, y=288)

    # codigoCAHA000251  Hashtag Camisa  1   25.0    11.0        

    pyautogui.write(arquivo.loc[linha, "codigo"])
    pyautogui.press("tab")

    # marca
    pyautogui.write(arquivo.loc[linha, "marca"])
    pyautogui.press("tab")

    # tipo
    pyautogui.write(arquivo.loc[linha, "tipo"])
    pyautogui.press("tab")

    # categoria
    pyautogui.write(str(arquivo.loc[linha, "categoria"]))
    pyautogui.press("tab")

    # preço
    pyautogui.write(str(arquivo.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    # custo
    pyautogui.write(str(arquivo.loc[linha, "custo"]))
    pyautogui.press("tab")

    # obs
    obs = arquivo.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(arquivo.loc[linha, "obs"])
    pyautogui.press("tab")

    # enviar
    pyautogui.press("enter")
    pyautogui.scroll(5000)

# Passo 5: Repetir o processo de cadastro até acabar