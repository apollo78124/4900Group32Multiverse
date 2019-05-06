from multiverse.server.plugins import *
from multiverse.server.objects import *
from multiverse.server.util import Log
from java.lang import Long


instance = Instance.current()
instanceOid = Instance.currentOid()


tele1Loc = instance.getMarker("village_tele").getPoint()
tele1Dest = instance.getMarker("swamp_tele_dest").getPoint()

spawnData = SpawnData()
spawnData.setFactoryName("Tele1Factory")
spawnData.setInstanceOid(Long(instanceOid))
spawnData.setLoc(tele1Loc)
spawnData.setNumSpawns(1)
spawnData.setSpawnRadius(0)
spawnData.setRespawnTime(1000)
spawnData.setCorpseDespawnTime(0)
MobManagerClient.createSpawnGenerator(spawnData)


tele2Loc = instance.getMarker("swamp_tele").getPoint()
tele2Dest = instance.getMarker("village_tele_dest").getPoint()

spawnData = SpawnData()
spawnData.setFactoryName("Tele2Factory")
spawnData.setInstanceOid(Long(instanceOid))
spawnData.setLoc(tele2Loc)
spawnData.setNumSpawns(1)
spawnData.setSpawnRadius(0)
spawnData.setRespawnTime(1000)
spawnData.setCorpseDespawnTime(0)
MobManagerClient.createSpawnGenerator(spawnData)


wolfLoc = instance.getMarker("village_mob_1").getPoint().clone()
wolfLoc.setY(0)

spawnData = SpawnData()
spawnData.setFactoryName("WolfFactory")
spawnData.setInstanceOid(Long(instanceOid))
spawnData.setLoc(wolfLoc)
spawnData.setNumSpawns(10)
spawnData.setSpawnRadius(80000)
spawnData.setRespawnTime(60000)
spawnData.setCorpseDespawnTime(30000)
MobManagerClient.createSpawnGenerator(spawnData)


zombieLoc = instance.getMarker("village_mob_2").getPoint().clone()
zombieLoc.setY(0)

spawnData = SpawnData()
spawnData.setFactoryName("ZombieFactory")
spawnData.setInstanceOid(Long(instanceOid))
spawnData.setLoc(zombieLoc)
spawnData.setNumSpawns(1)
spawnData.setSpawnRadius(10000)
spawnData.setRespawnTime(60000)
spawnData.setCorpseDespawnTime(30000)
MobManagerClient.createSpawnGenerator(spawnData)


crocLoc = instance.getMarker("swamp_mob_2").getPoint().clone()
crocLoc.setY(0)

spawnData = SpawnData()
spawnData.setFactoryName("CrocFactory")
spawnData.setInstanceOid(Long(instanceOid))
spawnData.setLoc(crocLoc)
spawnData.setNumSpawns(5)
spawnData.setSpawnRadius(20000)
spawnData.setRespawnTime(60000)
spawnData.setCorpseDespawnTime(30000)
MobManagerClient.createSpawnGenerator(spawnData)


braxLoc = instance.getMarker("swamp_mob_1").getPoint().clone()
braxLoc.setY(0)

spawnData = SpawnData()
spawnData.setFactoryName("BraxFactory")
spawnData.setInstanceOid(Long(instanceOid))
spawnData.setLoc(braxLoc)
spawnData.setNumSpawns(5)
spawnData.setSpawnRadius(30000)
spawnData.setRespawnTime(60000)
spawnData.setCorpseDespawnTime(30000)
MobManagerClient.createSpawnGenerator(spawnData)


npc1Loc = instance.getMarker("village_npc_1").getPoint().clone()
npc1Loc.setY(0)

spawnData = SpawnData()
spawnData.setFactoryName("npc1Factory")
spawnData.setInstanceOid(Long(instanceOid))
spawnData.setLoc(npc1Loc)
spawnData.setNumSpawns(1)
spawnData.setSpawnRadius(1)
spawnData.setRespawnTime(1000)
spawnData.setCorpseDespawnTime(0)
MobManagerClient.createSpawnGenerator(spawnData)


npc2Loc = instance.getMarker("village_npc_2").getPoint().clone()
npc2Loc.setY(0)

spawnData = SpawnData()
spawnData.setFactoryName("npc2Factory")
spawnData.setInstanceOid(Long(instanceOid))
spawnData.setLoc(npc2Loc)
spawnData.setNumSpawns(1)
spawnData.setSpawnRadius(1)
spawnData.setRespawnTime(1000)
spawnData.setCorpseDespawnTime(0)
MobManagerClient.createSpawnGenerator(spawnData)


npc3Loc = instance.getMarker("village_npc_3").getPoint()
# don't set Y coord to 0 because this guy is in a building

spawnData = SpawnData()
spawnData.setFactoryName("npc3Factory")
spawnData.setInstanceOid(Long(instanceOid))
spawnData.setLoc(npc3Loc)
spawnData.setNumSpawns(1)
spawnData.setSpawnRadius(1)
spawnData.setRespawnTime(1000)
spawnData.setCorpseDespawnTime(0)
MobManagerClient.createSpawnGenerator(spawnData)

Log.debug("done with instance_load.py")

