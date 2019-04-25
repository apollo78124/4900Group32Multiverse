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
        AnimationClient.playSingleAnimation(playerOid,
                                            "wave")
    
class BowCommand (ProxyPlugin.CommandParser):
    def parse(self, cmdEvent):
        playerOid = cmdEvent.getObjectOid()
        Log.debug("/bow: oid=" + str(playerOid))
        AnimationClient.playSingleAnimation(playerOid,
                                            "bow")
    
class ClapCommand (ProxyPlugin.CommandParser):
    def parse(self, cmdEvent):
        playerOid = cmdEvent.getObjectOid()
        Log.debug("/clap: oid=" + str(playerOid))
        AnimationClient.playSingleAnimation(playerOid,
                                            "clap")
    
class CryCommand (ProxyPlugin.CommandParser):
    def parse(self, cmdEvent):
        playerOid = cmdEvent.getObjectOid()
        Log.debug("/cry: oid=" + str(playerOid))
        AnimationClient.playSingleAnimation(playerOid,
                                            "cry")
 
class LaughCommand (ProxyPlugin.CommandParser):
    def parse(self, cmdEvent):
        playerOid = cmdEvent.getObjectOid()
        Log.debug("/laugh: oid=" + str(playerOid))
        AnimationClient.playSingleAnimation(playerOid,
                                            "laugh")
    
class CheerCommand (ProxyPlugin.CommandParser):
    def parse(self, cmdEvent):
        playerOid = cmdEvent.getObjectOid()
        Log.debug("/cheer: oid=" + str(playerOid))
        AnimationClient.playSingleAnimation(playerOid,
                                            "cheer")
    
class NoCommand (ProxyPlugin.CommandParser):
    def parse(self, cmdEvent):
        playerOid = cmdEvent.getObjectOid()
        Log.debug("/no: oid=" + str(playerOid))
        AnimationClient.playSingleAnimation(playerOid,
                                            "disagree")
    
class PointCommand (ProxyPlugin.CommandParser):
    def parse(self, cmdEvent):
        playerOid = cmdEvent.getObjectOid()
        Log.debug("/point: oid=" + str(playerOid))
        AnimationClient.playSingleAnimation(playerOid,
                                            "point")
    
class ShrugCommand (ProxyPlugin.CommandParser):
    def parse(self, cmdEvent):
        playerOid = cmdEvent.getObjectOid()
        Log.debug("/shrug: oid=" + str(playerOid))
        AnimationClient.playSingleAnimation(playerOid,
                                            "shrug")
        
proxyPlugin.registerCommand("/wave", WaveCommand())      
proxyPlugin.registerCommand("/bow", BowCommand())
proxyPlugin.registerCommand("/clap", ClapCommand())
proxyPlugin.registerCommand("/cry", CryCommand())
proxyPlugin.registerCommand("/laugh", LaughCommand())
proxyPlugin.registerCommand("/cheer", CheerCommand())
proxyPlugin.registerCommand("/no", NoCommand())
proxyPlugin.registerCommand("/point", PointCommand())
proxyPlugin.registerCommand("/shrug", ShrugCommand())

proxyPlugin.addProxyExtensionHook("proxy.INSTANCE_ENTRY", InstanceEntryProxyHook())
proxyPlugin.addProxyExtensionHook("proxy.GENERATE_OBJECT", GenerateObjectProxyHook())

Log.debug("extensions_proxy.py: LOADED")
