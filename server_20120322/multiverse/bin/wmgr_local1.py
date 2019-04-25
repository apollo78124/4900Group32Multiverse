from multiverse.mars import *
from multiverse.server.worldmgr import *
from multiverse.mars.objects import *
from multiverse.mars.util import *
from multiverse.server.math import *
from multiverse.server.events import *
from multiverse.server.objects import *
from multiverse.server.engine import *
from multiverse.server.util import *
from multiverse.msgsys import *

# Uncomment if you want to set a log level for this process
# that is different from the server's default log level
#Log.setLogLevel(1)

#Engine.msgSvrHostname = "localhost"
#Engine.msgSvrPort = 20374

Engine.setBasicInterpolatorInterval(5000)

# set the world geometry for this server
worldGeo = Geometry.maxGeometry()
World.setGeometry(worldGeo)

localGeo = Geometry.maxGeometry()
if (Engine.getProperty("multiverse.dualworldmanagers") == "1"):
    Log.debug("wmgr_local1.py: using dual world manager config")
    localGeo = Geometry(-2147483647, -2, -2147483647, 2147483647)

World.setLocalGeometry(localGeo)

World.perceiverRadius = 100 * 1000
#QuadTree.setMaxObjects(3)
World.setLocTolerance(20000)

World.setDefaultPermission(MarsPermissionFactory())
