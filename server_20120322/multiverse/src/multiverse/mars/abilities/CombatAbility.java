package multiverse.mars.abilities;

import multiverse.server.util.*;
import multiverse.mars.core.*;
import multiverse.mars.plugins.CombatPlugin;
import java.util.*;

public class CombatAbility extends MarsAbility {
    public CombatAbility(String name) {
        super(name);
    }

    public Map resolveHit(State state) {
	return new HashMap();
    }

    public MarsEffect getActivationEffect() { return activationEffect; }
    public void setActivationEffect(MarsEffect effect) { this.activationEffect = effect; }
    protected MarsEffect activationEffect = null;

    public void completeActivation(State state) {
        super.completeActivation(state);

        //Add attacker to target's list of attackers
        CombatPlugin.addAttacker(state.getTarget().getOid(), state.getObject().getOid());
        state.getObject().setCombatState(true);        
        
	Map params = resolveHit(state);
	Log.debug("CombatAbility.completeActivation: params=" + params);
        MarsEffect.applyEffect(activationEffect, state.getObject(), state.getTarget(), params);
    }
}