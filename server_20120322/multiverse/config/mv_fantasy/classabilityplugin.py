from multiverse.mars import *
from multiverse.mars.core import *
from multiverse.mars.objects import *
from multiverse.mars.util import *
from multiverse.server.math import *
from multiverse.server.events import *
from multiverse.server.objects import *
from multiverse.server.engine import *
from multiverse.server.util import *
from multiverse.server.plugins import *

Log.debug("classabilityplugin.py: starting")
## For out SampleWorld demonstration we show how we can override elemnts of the ClassAbilityPlugin
##  so we can put in our own way of handling things like experience gain
class SampleWorldClassAbilityPlugin(ClassAbilityPlugin):
    def handlePlayerXp(self, target, attackers):
        # In SampleWorld we only want the first person who attacked the mob to get experience
        #  If that player is grouped, then their group also gets experience
        
        ##pull the xp value from the target
        xpval = int(target.getProperty(KILL_EXP_STAT));

        # Get first attacker - Type of CombatInfo
        attacker = CombatPlugin.getCombatInfo(attackers[0])
        
        # Check to see if the attacker is grouped
        if attacker.isGrouped():
            # Apply experience to all group members
            # Get list of group members
            groupMembers = GroupClient.GetGroupMemberOIDs(attackerOid);
            # Cycle through each Oid and update the player's xp stat with the xp val pulled form the target
            for playerOid in groupMembers:
                player = CombatPlugin.getCombatInfo(playerOid)
                player.statModifyBaseValue(EXPERIENCE_STAT, xpval);
                ClassAbilityClient.sendXPUpdate(playerOid, EXPERIENCE_STAT, player.statGetCurrentValue(EXPERIENCE_STAT));             
        else:
            # Not grouped so only the attacker gets xp
            attacker.statModifyBaseValue(EXPERIENCE_STAT, xpval);
            ClassAbilityClient.sendXPUpdate(attacker.getOwnerOid(), EXPERIENCE_STAT, attacker.statGetCurrentValue(EXPERIENCE_STAT));            
## Register our version or plugin
classesPlugin = Engine.registerPlugin(SampleWorldClassAbilityPlugin())
#classesPlugin = Engine.registerPlugin("multiverse.mars.plugins.ClassAbilityPlugin")
Log.debug("classabilityplugin.py: done")
