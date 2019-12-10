import Pyro4

def startServer(host,name, registration):
    daemon = Pyro4.Daemon(host)
    nameserver = Pyro4.locateNS()
    for key in registration.keys():
        uri = daemon.register(registration[key])
        #This allows other remote objects to invoke
        nameserver.register(name+'_'+key, uri)
    daemon.requestLoop()

def getURI(objectName):
    nameserver = Pyro4.locateNS()
    uri = nameserver.lookup(objectName)
    return Pyro4.Proxy(uri)
