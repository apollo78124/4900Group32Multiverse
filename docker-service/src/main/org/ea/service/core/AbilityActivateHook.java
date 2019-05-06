package org.ea.service.core;

import multiverse.server.util.*;
import org.ea.service.objects.*;
import org.ea.service.plugins.*;

/**
 * an activate hook for items that trigger abilities
 * when the item is activated, the mob uses the ability
 */
public class AbilityActivateHook implements ActivateHook {
    public AbilityActivateHook() {
	super();
    }

    public AbilityActivateHook(MarsAbility ability) {
	super();
        setAbilityName(ability.getName());
    }

    public AbilityActivateHook(String abilityName) {
	super();
        setAbilityName(abilityName);
    }

    public void setAbilityName(String abilityName) {
        if (abilityName == null) {
            throw new RuntimeException("AbilityActivateHook.setAbility: bad ability");
        }
	this.abilityName = abilityName;
    }
    public String getAbilityName() {
	return abilityName;
    }
    public String abilityName = null;

    public MarsAbility getAbility() {
	if (abilityName == null)
	    return null;
	return Mars.AbilityManager.get(abilityName);
    }

    public boolean activate(Long activatorOid, MarsItem item, Long targetOid) {
	if (Log.loggingDebug)
            Log.debug("AbilityActivateHook.activate: activator=" + activatorOid + " item=" + item + " ability=" + abilityName + " target=" + targetOid);
        CombatClient.startAbility(abilityName, activatorOid, targetOid, item.getOid());
	return true;
    }

    private static final long serialVersionUID = 1L;
}
