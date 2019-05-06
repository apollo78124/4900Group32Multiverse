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
# registered.  add your custome behaviors here.
# you can see config/common/mobserver_init.py for the default values.

#//////////////////////////////////////////////////////////////////
#//
#// standard npc behavior
#//
#//////////////////////////////////////////////////////////////////
# example:
# WEObjFactory.registerBehaviorClass("BaseBehavior", "multiverse.server.engine.BaseBehavior")
