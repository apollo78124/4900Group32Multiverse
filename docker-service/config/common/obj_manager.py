from multiverse.mars import *
from multiverse.mars.objects import *
from multiverse.mars.core import *
from multiverse.mars.events import *
from multiverse.mars.util import *
from multiverse.mars.plugins import *
from multiverse.server.plugins import *
from multiverse.server.math import *
from multiverse.server.events import *
from multiverse.server.objects import *
from multiverse.server.engine import *
from java.lang import *

objectManager = ObjectManagerPlugin()

# Register TemplateHook if defined.  This guarantees that templates are
# defined with the ObjectManagerPlugin because subsequent plugins depend
# on the templates.
#
try:
    objectManager.registerActivateHook(TemplateHook())
except NameError:
    pass

Engine.registerPlugin(objectManager)

Engine.registerPlugin("multiverse.mars.plugins.MarsInventoryPlugin")
