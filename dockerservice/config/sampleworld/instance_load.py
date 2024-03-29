
from java.lang import Long
from multiverse.server.plugins import *
from multiverse.server.objects import *


instance = Instance.current()
instanceOid = Instance.currentOid()


wolfMarker = instance.getMarker("wolfmarker").clone()
wolfMarker.getPoint().setY(0)
spawnData = SpawnData()
spawnData.setFactoryName("WolfFactory")
spawnData.setInstanceOid(Long(instanceOid))
spawnData.setLoc(wolfMarker.getPoint())
spawnData.setNumSpawns(3)
spawnData.setSpawnRadius(20000)
spawnData.setRespawnTime(60000)
spawnData.setCorpseDespawnTime(30000)
MobManagerClient.createSpawnGenerator(spawnData)


zombieMarker = instance.getMarker("zombiemarker").clone()
zombieMarker.getPoint().setY(0)
spawnData = SpawnData()
spawnData.setFactoryName("ZombieFactory")
spawnData.setInstanceOid(Long(instanceOid))
spawnData.setLoc(zombieMarker.getPoint())
spawnData.setNumSpawns(2)
spawnData.setSpawnRadius(30000)
spawnData.setRespawnTime(60000)
spawnData.setCorpseDespawnTime(30000)
MobManagerClient.createSpawnGenerator(spawnData)


npc1Marker = instance.getMarker("npcmarker").clone()
npc1Marker.getPoint().setY(0)
spawnData = SpawnData()
spawnData.setFactoryName("Npc1Factory")
spawnData.setInstanceOid(Long(instanceOid))
spawnData.setLoc(npc1Marker.getPoint())
spawnData.setOrientation(npc1Marker.getOrientation())
spawnData.setNumSpawns(1)
spawnData.setSpawnRadius(1)
spawnData.setRespawnTime(5000)
spawnData.setCorpseDespawnTime(0)
MobManagerClient.createSpawnGenerator(spawnData)


npc2Marker = instance.getMarker("npcmarker").clone()
npc2Marker.getPoint().setY(0)
npc2Marker.getPoint().add(3000, 0, 0)
spawnData = SpawnData()
spawnData.setFactoryName("Npc2Factory")
spawnData.setInstanceOid(Long(instanceOid))
spawnData.setLoc(npc2Marker.getPoint())
spawnData.setOrientation(npc2Marker.getOrientation())
spawnData.setNumSpawns(1)
spawnData.setSpawnRadius(1)
spawnData.setRespawnTime(5000)
spawnData.setCorpseDespawnTime(0)
MobManagerClient.createSpawnGenerator(spawnData)

soldierTrainerMarker = instance.getMarker("npcmarker").clone()
soldierTrainerMarker.getPoint().setY(0)
soldierTrainerMarker.getPoint().add(6000, 0, 0)
spawndata = SpawnData()
spawnData.setFactoryName("SoldierTrainerFactory")
spawnData.setInstanceOid(Long(instanceOid))
spawnData.setLoc(soldierTrainerMarker.getPoint())
spawnData.setOrientation(soldierTrainerMarker.getOrientation())
spawnData.setNumSpawns(1)
spawnData.setSpawnRadius(1)
spawnData.setRespawnTime(5000)
spawnData.setCorpseDespawnTime(0)
MobManagerClient.createSpawnGenerator(spawnData)
