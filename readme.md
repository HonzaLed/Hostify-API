## Hostify API
This is Hostify API wrapper written in Python.  
You can use it to control your minecraft servers, get logs, monitor CPU, RAM and SSD usage.  

#! DISCLAIMER !  
This can get your Hostify.cz account banned  
This program won't be receiving updates anymore  
This repo is archived, you can still use it, but at your own risk!!!   

### How to use it
The API is located in file ```api.py```, but in order to work, you need to get Hostify session key.  
You can get the session key by calling the ```getSession``` function from file ```login.py``` like so:
````
import login
sessionKey = login.getSession()
````
That will open your web browser using library named ```selenium```, it will redirect you to login page, when you log in, the browser will be closed and the session will be returned from the function

Then you can initialize the API using the following code:
````
from api import HostifyAPI
client = HostifyAPI(sessionKey)
````
You can then access all the methods from HostifyAPI class.  
You can get all your servers and print all the IDs by calling the ```client.getAllServers``` function like so:
````
servers = client.getAllServers()
for server in servers:
    print(server["id"])
````
Or if you want to restart your server, you can do it with this code:
````
client.minecraftServerControllRestart(serverId)
````
All the control functions are:
````
client.minecraftServerControllStart(serverId)
client.minecraftServerControllStop(serverId)
client.minecraftServerControllRestart(serverId)
client.minecraftServerControllKill(serverId)
````
