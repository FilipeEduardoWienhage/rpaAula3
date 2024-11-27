import webbrowser
import pyautogui
import time

# criar um método
def login_automatico(usuario, senha):
    # Passo 1 = acessar o site
    # Passo 2 = mover o cursor até o imput do e-mail
    # Passo 3 = Digitar o e-mail
    # Passo 4 = Press tab
    # Passo 5 = Digitar a senha
    # Passo 6 = press enter

    webbrowser.open('login-html.html')
    time.sleep(2)
    X = 669
    Y = 274
    pyautogui.click(X,Y)
    

    pyautogui.write(usuario)
    pyautogui.press('tab')
    pyautogui.write(senha)
    pyautogui.press('enter')



login_automatico("teste@teste.com", "1234")