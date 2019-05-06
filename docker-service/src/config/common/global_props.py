from multiverse.mars import *
from multiverse.mars.objects import *
from multiverse.mars.core import *
from multiverse.mars.util import *
from multiverse.server.math import *
from multiverse.server.util import *
from multiverse.server.events import *
from multiverse.server.objects import *
from multiverse.server.engine import *

True=1
False=0

# define the standard mob equippable slots
defaultSlots = MarsEquipInfo("default")
defaultSlots.addEquipSlot(MarsEquipSlot.PRIMARYWEAPON)

World.addTheme("mars.toc")

# Change to False to allow flying/swimming (with page up/down)
World.FollowsTerrainOverride = True
