from java.util import *
from java.lang import *
from multiverse.mars import *
from multiverse.mars.core import *
from multiverse.mars.objects import *
from multiverse.mars.util import *
from multiverse.mars.plugins import *
from multiverse.msgsys import *
from multiverse.server.math import *
from multiverse.server.plugins import *
from multiverse.server.events import *
from multiverse.server.objects import *
from multiverse.server.engine import *
from multiverse.server.util import *

Log.debug("extensions_proxy.py: Loading...")

class WaveCommand (ProxyPlugin.CommandParser):
    def parse(self, cmdEvent):
        playerOid = cmdEvent.getObjectOid()
        Log.debug("/wave: oid=" + str(playerOid))
        AnimationClient.playSingleAnimation(playerOid, "wave")
    
class BoastCommand (ProxyPlugin.CommandParser):
    def parse(self, cmdEvent):
        playerOid = cmdEvent.getObjectOid()
        Log.debug("/boast: oid=" + str(playerOid))
        AnimationClient.playSingleAnimation(playerOid, "boast")
    
class CryCommand (ProxyPlugin.CommandParser):
    def parse(self, cmdEvent):
        playerOid = cmdEvent.getObjectOid()
        Log.debug("/cry: oid=" + str(playerOid))
        AnimationClient.playSingleAnimation(playerOid, "cry")
    
class LaughCommand (ProxyPlugin.CommandParser):
    def parse(self, cmdEvent):
        playerOid = cmdEvent.getObjectOid()
        Log.debug("/laugh: oid=" + str(playerOid))
        AnimationClient.playSingleAnimation(playerOid, "laugh")

proxyPlugin.registerCommand("/wave", WaveCommand())      
proxyPlugin.registerCommand("/boast", BoastCommand())
proxyPlugin.registerCommand("/cry", CryCommand())
proxyPlugin.registerCommand("/laugh", LaughCommand())

Log.debug("extensions_proxy.py: LOADED")
