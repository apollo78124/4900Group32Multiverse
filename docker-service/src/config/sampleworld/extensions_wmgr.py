from multiverse.server.engine import *
from multiverse.mars.plugins import *
from multiverse.mars.objects import *

wmgr.registerRegionTrigger("instanceEntry", InstanceEntryRegionTrigger())

trigger = MessageRegionTrigger(MessageRegionTrigger.TARGET_MODE)
trigger.setPropertyExclusions(wmgr.getPropertyExclusions())
props = HashMap()
props.put("specialProperty","specialValue")
trigger.setMessageProperties(props);
wmgr.registerRegionTrigger("enterMessage", trigger)

trigger = MessageRegionTrigger(MessageRegionTrigger.TARGET_MODE)
trigger.setPropertyExclusions(wmgr.getPropertyExclusions())
props = HashMap()
props.put("specialProperty","specialValue")
trigger.setMessageProperties(props);
wmgr.registerRegionTrigger("leaveMessage", trigger)

