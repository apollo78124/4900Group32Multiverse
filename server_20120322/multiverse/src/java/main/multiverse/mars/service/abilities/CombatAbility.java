package java.main.multiverse.mars.service.abilities;

import multiverse.server.util.*;
import multiverse.mars.core.*;
import multiverse.mars.plugins.CombatPlugin;
import java.util.*;

public class CombatAbility extends MarsAbility {
    public CombatAbility(String name) {
        super(name);
    }

    public Map<String, Object> resolveHit(State state) { //BCIT Map<String,Object>
	return new HashMap<String, Object>(); //BCIT Map<String,Object>
    }

    public MarsEffect getActivationEffect() { return activationEffect; }
    public void setActivationEffect(MarsEffect effect) { this.activationEffect = effect; }
    protected MarsEffect activationEffect = null;

    public void completeActivation(State state) {
        super.completeActivation(state);

        //Add attacker to target's list of attackers
        CombatPlugin.addAttacker(state.getTarget().getOid(), state.getObject().getOid());
        state.getObject().setCombatState(true);        
        
	Map<String, Object> params = resolveHit(state); //BCIT Map<String,Object>
	Log.debug("CombatAbility.completeActivation: params=" + params);
        MarsEffect.applyEffect(activationEffect, state.getObject(), state.getTarget(), params);
    }
}