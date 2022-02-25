from api import HostifyAPI
import keyboard
import login
import time
import rich

#Only for testing, you can write session = "mysessionkey" to file named mySession.py so you dont have to log in every time
try:
    from mySession import session
except:
    session = login.getSession()

print("[DEBUG]", session)

client = HostifyAPI(session)

id = client.getUserNoSharedServices()[0]["id"]
#[print(i) for i in client.getMinecraftServerLogs(id)[-5:]]

log = client.getMinecraftServerLogs(id)

[print(i) for i in log]
keyboard.add_hotkey('s', lambda: client.minecraftServerControlStart(id))
keyboard.add_hotkey('e', lambda: client.minecraftServerControlStop(id))
keyboard.add_hotkey('r', lambda: client.minecraftServerControlRestart(id))
keyboard.add_hotkey('k', lambda: client.minecraftServerControlKill(id))

def invert(text):
    return "\x1b[0;30;47m"+text+"\x1b[0m"
shortcuts = "\r "+invert("S")+" - start, "+invert("E")+" - stop (end), "+invert("R")+" - restart, "+invert("K")+" - kill"

print(shortcuts, end="\r")

while True:
    time.sleep(3)
    cache = client.getMinecraftServerLogs(id)
    added = len([log.append(i) for i in cache[cache.index(log[-1]):]])
    
    if added>1:
        [print(i) for i in log[added*-1:]]
    while len(log) > 999:
        log.pop(0)
    print("\r"+shortcuts, end="\r")
