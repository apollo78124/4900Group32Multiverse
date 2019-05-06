from multiverse.server.engine import *
from multiverse.mars.plugins import *
from multiverse.mars.objects import *

wmgr = MarsWorldManagerPlugin()

Engine.registerPlugin(wmgr)
