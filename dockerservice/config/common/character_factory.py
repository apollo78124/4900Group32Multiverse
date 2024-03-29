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

displayContext = DisplayContext("human_female.mesh")
displayContext.addSubmesh(DisplayContext.Submesh("bodyShape-lib.0",
                                                 "human_female.skin_material"))
displayContext.addSubmesh(DisplayContext.Submesh("head_aShape-lib.0",
                                                 "human_female.head_a_material"))
displayContext.addSubmesh(DisplayContext.Submesh("hair_bShape-lib.0",
                                                 "human_female.hair_b_material"))

# default player template
player = Template("DefaultPlayer")

player.put(WorldManagerClient.NAMESPACE,
           WorldManagerClient.TEMPL_DISPLAY_CONTEXT,
           displayContext)

player.put(WorldManagerClient.NAMESPACE,
           WorldManagerClient.TEMPL_OBJECT_TYPE,
           ObjectTypes.player)

player.put(InventoryClient.NAMESPACE,
           InventoryClient.TEMPL_ITEMS,
           "")
ObjectManagerClient.registerTemplate(player)

# character factory
class SampleFactory (CharacterFactory):
    def createCharacter(self, worldName, uid, properties):
        name = properties.get("characterName");

	# Player start location
        loc = Point(-135343, 0, -202945)

        # Player start instance; assumes you have an instance named "default"
        instanceOid = InstanceClient.getInstanceOid("default")

        overrideTemplate = Template()

        if name:
            overrideTemplate.put(WorldManagerClient.NAMESPACE,
                WorldManagerClient.TEMPL_NAME, name)

        overrideTemplate.put(WorldManagerClient.NAMESPACE,
                WorldManagerClient.TEMPL_INSTANCE, Long(instanceOid))
        overrideTemplate.put(WorldManagerClient.NAMESPACE,
                WorldManagerClient.TEMPL_LOC, loc)

        # Initialize the player's instance restore stack
        restorePoint = InstanceRestorePoint("default", loc)
        restorePoint.setFallbackFlag(True)
        restoreStack = LinkedList()
        restoreStack.add(restorePoint)
        overrideTempate.put(Namespace.OBJECT_MANAGER,
               ObjectManagerClient.TEMPL_INSTANCE_RESTORE_STACK, restoreStack)
        overrideTempate.put(Namespace.OBJECT_MANAGER,
               ObjectManagerClient.TEMPL_CURRENT_INSTANCE_NAME, "default")

	# Make the player persistent (will be saved in database)
        overrideTemplate.put(Namespace.OBJECT_MANAGER,
            ObjectManagerClient.TEMPL_PERSISTENT, Boolean(True));

	# Create the player object
        objOid = ObjectManagerClient.generateObject(
                "DefaultPlayer", overrideTemplate)
        Log.debug("SampleFactory: generated obj oid=" + str(objOid))

        return objOid

sampleFactory = SampleFactory()
LoginPlugin.getCharacterGenerator().setCharacterFactory(sampleFactory);
