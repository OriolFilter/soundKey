import keyboard
import pygetwindow as gw
# import pyscreenshot as ImageGrab #No primordial
from playsound import playsound
import threading


imgFolder="img/"
soundFolder="sound/"

character="ivern"

# spell1="q"
# spell2="w"
# spell3="e"
# spell4="r"
#
# summon1="d"
# summon2="f"

alternativeKeysArry=["space"]
summonDic={"f":"flash","i":"ignite","s":"smite"}

spellArry=[
    ["q","Q"],#s1
    ["w","W"],#s2
    ["e","E"],#s3
    ["r","R"]#s4
]
summonArry=[
    ["d","f"],#s1
    ["f","s"]#s2
]

exit="shift+esc"

# windowsName="Discord" #test
# windowsName="Discord"
windowsName="League of Legends (TM) Client"

close=False

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
        # print(link)
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


# print(spellArry[0][0])
# x=0

for key,spellL in spellArry:
    keyboard.add_hotkey(key, spell, args=spellL)
    for altKey in alternativeKeysArry:
        keyboard.add_hotkey(key + "+"+altKey, spell, args=spellL)
    # print(key)

for key,summL in summonArry:
    keyboard.add_hotkey(key, summoner, args=summL)
    for altKey in alternativeKeysArry:
        keyboard.add_hotkey(key + "+"+altKey, summoner, args=summL)
    # # print(key,summL)

# keyboard.add_hotkey("d", spell, args="f")


while not close:
    try:
        keyboard.wait(exit)
        close=True
    except: pass

# keyboard.add_hotkey(summon1, summoner, args=("f"))


