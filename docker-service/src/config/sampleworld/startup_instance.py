from multiverse.server.plugins import *
from multiverse.server.objects import *
from multiverse.server.engine import *


template = Template("sampleworld template")
template.put(Namespace.INSTANCE, InstanceClient.TEMPL_WORLD_FILE_NAME, "$WORLD_DIR/$WORLD_NAME.mvw")
template.put(Namespace.INSTANCE, InstanceClient.TEMPL_INIT_SCRIPT_FILE_NAME, "$WORLD_DIR/instance_load.py")

rc = InstanceClient.registerInstanceTemplate(template)

overrideTemplate = Template()
overrideTemplate.put(Namespace.INSTANCE, InstanceClient.TEMPL_INSTANCE_NAME, "default")

rc = InstanceClient.createInstance("sampleworld template", overrideTemplate)
Log.debug("startup_instance.py: createInstance result=" + str(rc))



template = Template("bigbrother template")
template.put(Namespace.INSTANCE, InstanceClient.TEMPL_WORLD_FILE_NAME, "$WORLD_DIR/bigbrother.mvw")

rc = InstanceClient.registerInstanceTemplate(template)

overrideTemplate = Template("bigbrother")
overrideTemplate.put(Namespace.INSTANCE, InstanceClient.TEMPL_INSTANCE_NAME, "bigbrother")

rc = InstanceClient.createInstance("bigbrother template", overrideTemplate)
Log.debug("startup_instance.py: createInstance result=" + str(rc))



template = Template("frontier template")
template.put(Namespace.INSTANCE, InstanceClient.TEMPL_WORLD_FILE_NAME, "$WORLD_DIR/frontier.mvw")

rc = InstanceClient.registerInstanceTemplate(template)

overrideTemplate = Template("frontier")
overrideTemplate.put(Namespace.INSTANCE, InstanceClient.TEMPL_INSTANCE_NAME, "frontier")

rc = InstanceClient.createInstance("frontier template", overrideTemplate)
Log.debug("startup_instance.py: createInstance result=" + str(rc))


template = Template("video template")
template.put(Namespace.INSTANCE, InstanceClient.TEMPL_WORLD_FILE_NAME, "$WORLD_DIR/video.mvw")

rc = InstanceClient.registerInstanceTemplate(template)

overrideTemplate = Template("video")
overrideTemplate.put(Namespace.INSTANCE, InstanceClient.TEMPL_INSTANCE_NAME, "video")

rc = InstanceClient.createInstance("video template", overrideTemplate)
Log.debug("startup_instance.py: createInstance result=" + str(rc))

Engine.getPlugin("Instance").setPluginAvailable(True)

