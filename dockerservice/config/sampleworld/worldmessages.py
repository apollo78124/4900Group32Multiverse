from java.util import *
from java.lang import *
from multiverse.msgsys import *

#
# This python file creates a world-specific message catalog, and 
# contains definitions for world-specific message  types, if 
# your world makes use of them.  Not all worlds actually
# need to define their own message types, but if if your world does
# need world-specific message types, they must be added to your 
# world-specific message catalog by listing them in this file
#

#
# Create the world message catalog.  Multiverse reserves message numbers
# from 1 through 500; the world-specific catalog defined below allocates
# message type numbers from the range 501-1000.
#
worldMessageCatalog = MessageCatalog.addMsgCatalog("worldMessageCatalog", 501, 500);

#
# Add your world-specific messages here.  Each call to addMsgTypeTranslation
# adds the message type which is the second argument to the world message
# catalog.  Each message type must be defined in YourWorldModule by a call
# to MessageType.intern(message_type_string);
# 
#MessageCatalog.addMsgTypeTranslation(worldMessageCatalog, YourWorldModule.MSG_TYPE_YOUR_MESSAGE_TYPE)
