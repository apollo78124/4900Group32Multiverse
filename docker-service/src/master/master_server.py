from multiverse.server.engine import *
from multiverse.server.util import *

ms = MasterServer.getMasterServer()
#ms.setTCPPort(9005)
#ms.setRDPPort(9010)

# Uncomment if you want to set a log level for this process
# that is different from the server's default log level
#Log.setLogLevel(1)
privKey = """===PUT MASTER SERVER PRIVATE ENCRYPTED KEY HERE==="""

SecureTokenManager.getInstance().initMaster(Base64.decode(privKey))
