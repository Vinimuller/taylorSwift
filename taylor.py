from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import requests
import schedule
import time
from datetime import datetime
import playsound

chrome_options = Options()

xpathBTN = "/html/body/div/section[2]/div/div[3]/a[3]/div/div[3]"
xpathBTNVIP = "/html/body/div/section[2]/div/div[3]/a[4]/div/div[3]"
xpathCard = '/html/body/div/section[2]/div/div[3]/a[3]'
TOKEN = "6436678943:AAHYfEqwJ0MRV6J74TZEjAAqdKNQeO9kurU"
chat_id = "-4030736931"
now = datetime.now().strftime("%D %H:%M:%S")
current_time = datetime.now().strftime("%D %H:%M:%S")
lastTime = datetime.now()

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(chrome_options, service=servico)


def sendSignal(lastTime):
    dt = datetime.now()
    delta = (dt - lastTime)
    if(delta > 30):
        lastTime = datetime.now()
        sendMessage("I'm still alive")

def sendMessage(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    print(message)
    requests.get(url).json() # this sends the message

def runBot():
    now = datetime.now()
    current_time = datetime.now().strftime("%D %H:%M:%S")
    print()
    print(str(current_time) + " Running... \n")
    servico = Service(ChromeDriverManager().install())
    navegador.get("https://www.taylorswifttheerastour.com.br/")

    xpathBTN = "/html/body/div/section[2]/div/div[3]/a[3]/div/div[3]"
    xpathBTNVIP = "/html/body/div/section[2]/div/div[3]/a[4]/div/div[3]"
    btn = navegador.find_element('xpath', xpathBTN)
    btnVip = navegador.find_element('xpath', xpathBTNVIP)

    print(type(btn))    

    btnAtributes = navegador.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', btn)
    btnVipAtributes = navegador.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', btnVip)

    if((str(btn.get_attribute("data-hover-text")) != 'ESGOTADO') or (str(btnVip.get_attribute("data-hover-text")) != 'ESGOTADO ')):
        message = "SOMETHING HAS CHANGED!!! \nClick to check:\nhttps://www.taylorswifttheerastour.com.br/\n" + current_time 
        sendMessage(message)
    else:
        print("nothing has changed")

    navegador.quit()
    print("\nDone")


def runBot2():
    current_time = datetime.now().strftime("%D %H:%M:%S")
    print(str(current_time) + " Running... \n")

    navegador.get("https://www.taylorswifttheerastour.com.br/")
    hrefCard = navegador.find_element('xpath', xpathCard).get_attribute('href')
    navegador.get(hrefCard)

    if(navegador.current_url != 'https://taylor-swift-sp.sales.ticketsforfun.com.br/#errors/eventNotFound'):
        message = "LINK MUDOU!!!\nClick to check:\n" + navegador.current_url + "\n" + current_time 
        sendMessage(message)
        schedule.clear()
        playsound.playsound("morningalarm.mp3", block=True)
        time.sleep(30*60)
        sendMessage("getting back to my duty, sir")
        schedule.every(1).minutes.do(runBot2)
    else:
        print("Ainda sendo redirecionado")
    
    # navegador.quit()
    print("\nDone")

def runBot3():
    current_time = datetime.now().strftime("%D %H:%M:%S")
    print("\n" + str(current_time) + " Running...")

    navegador.get("https://www.taylorswifttheerastour.com.br/")
    hrefCard = navegador.find_element('xpath', xpathCard).get_attribute('href')
    navegador.get(hrefCard)
    
    # check if redirects to error
    if("eventNotFound" not in navegador.current_url):
        
        # check if it is in a queue
        while("queue" in navegador.current_url):
            time.sleep(1)

        tckAvailable = navegador.find_elements(By.CLASS_NAME, "tickets-available")
        if(tckAvailable):
            print("Ingressos disponiveis")
            
            message = "INGRESSO DISPONIVEL!!!\nClick to check:\n" + navegador.current_url + "\n" + current_time 
            sendMessage(message)
            playsound.playsound("morningalarm.mp3", block=True)
            # time.sleep(15*60)
            
            sendMessage("getting back to my duty, sir 🫡")
        else:
            print("Ingressos Esgotados")
    else:
        print("Redirected to error page")

# sendMessage("it's been a pleasure serving with you, sir 🫡")

while True:
    runBot3()
    time.sleep(1*60)



    # <div class="tickets-available"><div class="msg-text"><!----><div>