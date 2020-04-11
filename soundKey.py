import keyboard
import pygetwindow as gw
# import pyscreenshot as ImageGrab #No primordial
from playsound import playsound
import threading


imgFolder="img/"
soundFolder="sound/"

character="ivern"

spell1="q"
spell2="w"
spell3="e"
spell4="r"

summon1="d"
summon2="f"
summonDic={"f":"flash","i":"ignite","s":"smite"}

exit="esc"

# windowsName="Discord" #test
windowsName="League of Legends (TM) Client"



def checkActiveWindow():
    try:
        window = (gw.getWindowsWithTitle(windowsName)[0])
        if window.isActive == True:
            return True
        else:
            return False
    except IndexError:
        print("Window '"+windowsName+"' was not found!")
        return False

def spell(S=None,D="spells/"): #S
    if checkActiveWindow() and checkSpellUp():
        link=soundFolder+D+character+S+".mp3"
        bkgPlay = threading.Thread(target=playsound, args=(link,))
        bkgPlay.start()

def summoner(S=None,D="summoners/"): #Summoner #Directory
    if checkActiveWindow() and checkSpellUp():
        link=soundFolder+D+summonDic[S]+".mp3"
        bkgPlay = threading.Thread(target=playsound, args=(link,))
        bkgPlay.start()

def test(s):
    pass

def checkSpellUp(S=None):
    if True:
        return True
    else: return False

def checkSummonerUp(S=None):
    if True:
        return True
    else: return False

keyboard.add_hotkey(spell1, spell,args="Q")
keyboard.add_hotkey(spell2, spell,args="W")
keyboard.add_hotkey(spell3, spell,args="E")
keyboard.add_hotkey(spell4, spell,args="R")
keyboard.add_hotkey(summon1, summoner, args=("f"))
keyboard.add_hotkey(summon2, summoner, args=("s"))

keyboard.wait(exit)
