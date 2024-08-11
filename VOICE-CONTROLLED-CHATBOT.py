from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from time import sleep
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By

# import pathlib
# ScriptDir = pathlib.Path().absolute()
import pyttsx3
import speech_recognition as sr
import warnings
warnings.simplefilter('ignore')




def speak(text):
    engine = pyttsx3.init()
    # voices = engine.getProperty('voices')  #use to get sound type
    Id = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
    engine.setProperty('voice', Id)
    print("")
    print(f"==> Jarvis AI :  {text}")
    print("")

    engine.say(text=text)
    engine.runAndWait()

    
    # for voice in voices:        #use for getting voice name
    #     print(voice.id)     
    #     print(voice.name)



def speechrecognition():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 1;
        audio = r.listen(source, 0, 8)

    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='en')
        print(f"==> Sachin : {query}")
        return query.lower()

    except:
        return ""


url = "https://flowgpt.com/chat"
edge_options = Options()
user_agent = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2"
edge_options.add_argument(f"user-agent={user_agent}")
# edge_options.add_argument('--profile-directory=Default')
# edge_options.add_argument("--headless=new")
# edge_options.add_argument(f'user-data-dir={ScriptDir}\\edgedata')
edge_service = Service(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=edge_service, options=edge_options)
driver.maximize_window()
driver.get(url=url)
# sleep(10)


ChatNumber = 3

def Popupremover():
    Xpath = '/html/body/div[3]/div[3]/div/section/button'
    driver.find_element(by=By.XPATH,value=Xpath).click()
    


def Websiteopener():
    while True:
        try:
            xPath='/html/body/div[3]/div[3]/div/section/button'
            driver.find_element(by=By.XPATH,value=xPath)
            break

        except:
            pass


def QuerySender(Query):
    XpathInput = '/html/body/div[1]/div/main/div[3]/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div[2]/div[3]/div/textarea'
    XpathSenderButton = '/html/body/div[1]/div/main/div[3]/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div[2]/div[3]/button'


    driver.find_element(by=By.XPATH,value=XpathInput).send_keys(Query)
    sleep(1)
    driver.find_element(by=By.XPATH,value=XpathSenderButton).click()
    sleep(1)


def Reasultscrapper():
    global ChatNumber
    ChatNumber = str(ChatNumber)
    Xpath=f"/html/body/div[1]/div/main/div[3]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div/div[{ChatNumber}]/div/div/div/div[1]/div"
    Text = driver.find_element(by=By.XPATH,value=Xpath).text
    ChatNumbernew = int(ChatNumber) + 2
    ChatNumber = ChatNumbernew
    return Text

def waitfortheanswer():
    sleep(3)
    xpath='/html/body/div[1]/main/div[3]/div/div[2]/div/div[3]/div[2]/div/div[2]/div[1]/div/button'
    while True:
        try:
            driver.find_element(by=By.XPATH,value=xpath)
        except:
            break

Websiteopener()
sleep(3)
Popupremover()


while True:
    Query = speechrecognition()
    if len(str(Query))<3:
        pass

    elif Query==None:
        pass

    else :
        QuerySender(Query=Query)
        waitfortheanswer()
        Text = Reasultscrapper()
        speak(Text)
    
