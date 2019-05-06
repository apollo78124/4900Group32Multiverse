from multiverse.mars.plugins import GroupPlugin

##
# Group Configuration File
##

# Register stats for group object to track and send to each client
GroupPlugin.RegisterStat("health")
GroupPlugin.RegisterStat("health-max")

# Set maximum group size
GroupPlugin.SetMaxGroupSize(8)
