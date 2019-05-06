from multiverse.server.plugins import *
from multiverse.server.objects import *
from multiverse.server.engine import *


template = Template("mv_fantasy template")
template.put(Namespace.INSTANCE, InstanceClient.TEMPL_WORLD_FILE_NAME, "$WORLD_DIR/mv_fantasy.mvw")
template.put(Namespace.INSTANCE, InstanceClient.TEMPL_INIT_SCRIPT_FILE_NAME, "$WORLD_DIR/instance_load.py")

rc = InstanceClient.registerInstanceTemplate(template);

overrideTemplate = Template("mv_fantasy");
overrideTemplate.put(Namespace.INSTANCE, InstanceClient.TEMPL_INSTANCE_NAME, "default")

rc = InstanceClient.createInstance("mv_fantasy template", overrideTemplate);
Log.debug("startup_instance.py: createInstance result=" + str(rc))

Engine.getPlugin("Instance").setPluginAvailable(True)

