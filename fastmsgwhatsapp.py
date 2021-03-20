import webbrowser
from time import sleep
import pyautogui as py


time = int(input("number of message you want to send: "))

positionserch = 195, 217
positionclick = 198, 370
positionmsg = 780, 970
search = input("enter name of target: ")
msg = input("whats the message: ")
url = 'https://web.whatsapp.com/'
webbrowser.open(url)
sleep(18)
py.click(positionserch)
sleep(1)
py.write(search)
sleep(1)
py.click(positionclick)
sleep(2)
for i in range(time):
    py.click(positionmsg)
    py.write(msg)
    py.press('enter')
