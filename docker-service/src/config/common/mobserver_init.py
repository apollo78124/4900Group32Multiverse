from multiverse.mars import *
from multiverse.mars.core import *
from multiverse.mars.objects import *
from multiverse.mars.util import *
from multiverse.mars.plugins import *
from multiverse.mars.behaviors import *
from multiverse.msgsys import *
from multiverse.server.math import *
from multiverse.server.plugins import *
from multiverse.server.events import *
from multiverse.server.objects import *
from multiverse.server.engine import *
from multiverse.server.util import *
from java.lang import *

# this file gets run before the mobserver manager plugin gets
# registered.  these are the default multiverse behaviors
# if you want to add your own, add it to config/<world>/mobserver_init.py

#//////////////////////////////////////////////////////////////////
#//
#// standard npc behavior
#//
#//////////////////////////////////////////////////////////////////
WEObjFactory.registerBehaviorClass("BaseBehavior", "multiverse.server.engine.BaseBehavior")
WEObjFactory.registerBehaviorClass("CombatBehavior", "multiverse.mars.behaviors.CombatBehavior")
WEObjFactory.registerBehaviorClass("RadiusRoamBehavior", "multiverse.mars.behaviors.RadiusRoamBehavior")
WEObjFactory.registerBehaviorClass("PatrolBehavior", "multiverse.mars.behaviors.PatrolBehavior")
