package multiverse.mars.effects;

import multiverse.mars.core.*;

public class StunEffect extends MarsEffect {
    public StunEffect(String name) {
	super(name);
	isPeriodic(false);
	isPersistent(true);
    }

    // add the effect to the object
    public void apply(EffectState state) {
	super.apply(state);
    }

    // remove the effect from the object
    public void remove(EffectState state) {
	super.remove(state);
    }

    // perform the next periodic pulse for this effect on the object
    public void pulse(EffectState state) {
	super.pulse(state);
    }
}