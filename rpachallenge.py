import pyautogui
import webbrowser
import time

# CRIAR UM METODO
def login_automatico(nome, sobrenome, empresa, cargo, endereco, mail, telefone):
    # passo1 = Acessar o site
    webbrowser.open("https://www.rpachallenge.com/")
    time.sleep(4)
    
    firstName = pyautogui.locateOnScreen("firstname.png", confidence=0.8)

    if firstName:
        pyautogui.click(firstName)
        pyautogui.write(nome)
    else:
        print("Campo de nome não encontrado")
        return
    

    lastName = pyautogui.locateOnScreen("lastname.png", confidence=0.8)
    if lastName:
        pyautogui.click(lastName)
        pyautogui.write(sobrenome)
    else:
        print("Campo de sobrenome não encontrado")
        return
    

    companyname = pyautogui.locateOnScreen("companyname.png", confidence=0.8)
    if empresa:
        pyautogui.click(companyname)
        pyautogui.write(empresa)
    else:
        print("Campo de empresa não encontrado")
        return
    

login_automatico("John", "Smith", "IT Solutions", "Analyst", "98 North Road", "jsmith@itsolutions.co.uk", "40716543298")