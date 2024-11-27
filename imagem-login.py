import pyautogui
import webbrowser
import time

# CRIAR UM METODO
def login_automatico(usuario,senha):
    # passo1 = Acessar o site
    webbrowser.open("login-html.html")
    time.sleep(1)
    # passo2 = mover o cursor até o input do e-mail
    campo_login = pyautogui.locateOnScreen("email.png", confidence=0.8)

    if campo_login:
        pyautogui.click(campo_login)
        pyautogui.write(usuario)
    else:
        print("Campo de email não encontrado")
        return
    # passo4 = press tab
    pyautogui.press("tab")
    # passo5 = digitar a senha
    pyautogui.write(senha)
    # passo6 = press enter
    pyautogui.press("tab")

    campo_entrar = pyautogui.locateOnScreen("entrar.png", confidence=0.8)

    if campo_entrar:
        pyautogui.click(campo_entrar)
    else:
        print("Botão de entrar não encontrado")
        return
    


login_automatico("teste@teste.com","123456")