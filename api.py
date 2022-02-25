import requests

class HostifyAPI:
    def __init__(self, session, gqlAddress="https://gql.hostify.cz/gql"):
        self.address = gqlAddress
        self.cookies = {"session": session}
        if self.getLoggedIn():
            self.getShortAccount()
            print("[INFO] Logged in as", self.account["username"])
        else:
            raise Exception("[ERROR] Could not log in, please try again!")
    def __makeRequest(self, data, method="POST"):
        if method == "POST":
            r = requests.post(self.address, cookies=self.cookies, json=data)
        if method == "GET":
            r = requests.post(self.address, cookies=self.cookies)
        try:
            return r.json()
        except BaseException as err:
            print("[ERROR] Error while parsing JSON from request:", err)
            return r.text
    ## API endpoints starts here
    def getLoggedIn(self):
        data = {"operationName":"loggedIn","variables":{},"query":"query loggedIn {\n  loggedIn\n}\n"}
        r = self.__makeRequest(data)
        return r["data"]["loggedIn"]

    def getShortAccount(self):
        data = {"operationName":"getShortAccount","variables":{},"query":"query getShortAccount {\n  account {\n    ...ShortUser\n    __typename\n  }\n}\n\nfragment ShortUser on User {\n  id\n  username\n  email\n  credit\n  activated\n  shortid\n  hash\n  role\n  agreements {\n    vop\n    gdpr\n    __typename\n  }\n  __typename\n}\n"}
        r = self.__makeRequest(data)
        self.account = r["data"]["account"]

    def getAlerts(self):
        data = {"operationName":"getAlerts","variables":{},"query":"query getAlerts {\n  alerts {\n    id\n    type\n    message\n    start\n    __typename\n  }\n}\n"}
        r = self.__makeRequest(data)
        return r["data"]["alerts"]

    def getUserServices(self):
        data = {"operationName":"getUserServices","variables":{},"query":"query getUserServices {\n  account {\n    services {\n      id\n      name\n      type\n      shared\n      __typename\n    }\n    __typename\n  }\n}\n"}
        r = self.__makeRequest(data)
        return r["data"]["account"]["services"]

    def getUserNoSharedServices(self):
        services = self.getUserServices()
        cache = []
        for service in services:
            if not service["shared"]:
                cache.append(service)
        return cache

    def getAllServers(self):
        data = {"operationName":"getAllServers","variables":{},"query":"query getAllServers {\n  minecraftServers {\n    ...FullMinecraftServer\n    __typename\n  }\n}\n\nfragment FullMinecraftServer on MinecraftServer {\n  id\n  name\n  ip\n  port\n  dns\n  eula\n  jar\n  expires\n  shared\n  status\n  ownedBy\n  favicon\n  dedicated {\n    hostname\n    __typename\n  }\n  permissions {\n    read\n    write\n    __typename\n  }\n  storage {\n    used\n    reserved\n    __typename\n  }\n  package {\n    ram\n    __typename\n  }\n  players {\n    online\n    max\n    list\n    __typename\n  }\n  version {\n    type\n    version\n    image\n    __typename\n  }\n  resources {\n    type\n    tps\n    __typename\n  }\n  __typename\n}\n"}
        r = self.__makeRequest(data)
        return r["data"]["minecraftServers"]

    def getShortMinecraftServer(self, id):
        data = {"operationName":"getShortMinecraftServer","variables":{"id":id},"query":"query getShortMinecraftServer($id: ID!) {\n  minecraftServer(id: $id) {\n    ...GlobalMinecraftServer\n    __typename\n  }\n}\n\nfragment GlobalMinecraftServer on MinecraftServer {\n  id\n  name\n  locked\n  teamspeakActive\n  permissions {\n    read\n    write\n    __typename\n  }\n  dedicated {\n    hostname\n    __typename\n  }\n  __typename\n}\n"}
        r = self.__makeRequest(data)
        return r["data"]["minecraftServer"]

    def getMinecraftServerDashboard(self, id):
        data = {"operationName":"getMinecraftServerDashboard","variables":{"id":id},"query":"query getMinecraftServerDashboard($id: ID!) {\n  minecraftServer(id: $id) {\n    ...MinecraftServerDashboard\n    __typename\n  }\n}\n\nfragment MinecraftServerDashboard on MinecraftServer {\n  id\n  name\n  ip\n  port\n  dns\n  expires\n  status\n  jar\n  eula\n  shared\n  ownedBy\n  alerts {\n    type\n    message\n    __typename\n  }\n  resources {\n    cpu\n    ram\n    tps\n    type\n    __typename\n  }\n  package {\n    ram\n    __typename\n  }\n  storage {\n    used\n    reserved\n    __typename\n  }\n  players {\n    online\n    max\n    list\n    __typename\n  }\n  commands {\n    id\n    name\n    command\n    custom\n    __typename\n  }\n  __typename\n}\n"}
        r = self.__makeRequest(data)
        return r["data"]["minecraftServer"]

    def getMinecraftServerLogs(self, id):
        data = {"operationName":"getMinecraftServerLogs","variables":{"id":id},"query":"query getMinecraftServerLogs($id: ID!) {\n  minecraftServer(id: $id) {\n    logs\n    __typename\n  }\n}\n"}
        r = self.__makeRequest(data)
        return r["data"]["minecraftServer"]["logs"]

    def minecraftServerControlRestart(self, id):
        data = {"operationName":"minecraftServerControlRestart","variables":{"id":id},"query":"mutation minecraftServerControlRestart($id: ID!) {\n  minecraftServerControlRestart(id: $id)\n}\n"}
        r = self.__makeRequest(data)
        try:
            return r["data"]["minecraftServerControlRestart"]
        except:
            return False

    def minecraftServerControlKill(self, id):
        data = {"operationName":"minecraftServerControlKill","variables":{"id":id},"query":"mutation minecraftServerControlKill($id: ID!) {\n  minecraftServerControlKill(id: $id)\n}\n"}
        r = self.__makeRequest(data)
        try:
            return r["data"]["minecraftServerControlKill"]
        except:
            return False

    def minecraftServerControlStop(self, id):
        data = {"operationName":"minecraftServerControlStop","variables":{"id":id},"query":"mutation minecraftServerControlStop($id: ID!) {\n  minecraftServerControlStop(id: $id)\n}\n"}
        r = self.__makeRequest(data)
        try:
            return r["data"]["minecraftServerControlStop"]
        except:
            return False

    def minecraftServerControlStart(self, id):
        data = {"operationName":"minecraftServerControlStart","variables":{"id":id},"query":"mutation minecraftServerControlStart($id: ID!) {\n  minecraftServerControlStart(id: $id)\n}\n"}
        r = self.__makeRequest(data)
        try:
            return r["data"]["minecraftServerControlStart"]
        except:
            return False
