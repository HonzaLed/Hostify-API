from api import HostifyAPI
import login

#Only for testing, you can write session = "mysessionkey" to file named mySession.py so you dont have to log in every time
try:
    from mySession import session
except:
    session = login.getSession()

print("[DEBUG]", session)

client = HostifyAPI(session)

id = client.getUserNoSharedServices()[0]["id"]
[print(i) for i in client.getMinecraftServerLogs(id)[-5:]]