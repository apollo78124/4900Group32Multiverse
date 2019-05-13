package multiverse.mars.abilities;

import multiverse.mars.core.*;

public class EffectAbility extends MarsAbility {
    public EffectAbility(String name) {
        super(name);
    }

    public MarsEffect getActivationEffect() { return activationEffect; }
    public void setActivationEffect(MarsEffect effect) { this.activationEffect = effect; }
    protected MarsEffect activationEffect = null;

    public MarsEffect getChannelEffect() { return channelEffect; }
    public void setChannelEffect(MarsEffect effect) { this.channelEffect = effect; }
    protected MarsEffect channelEffect = null;

    public MarsEffect getActiveEffect() { return activeEffect; }
    public void setActiveEffect(MarsEffect effect) { this.activeEffect = effect; }
    protected MarsEffect activeEffect = null;

    public void completeActivation(State state) {
        super.completeActivation(state);
        MarsEffect.applyEffect(activationEffect, state.getObject(), state.getTarget());
    }

    public void pulseChannelling(State state) {
        super.pulseChannelling(state);
        MarsEffect.applyEffect(channelEffect, state.getObject(), state.getTarget());
    }

    public void pulseActivated(State state) {
        super.pulseActivated(state);
        MarsEffect.applyEffect(activeEffect, state.getObject(), state.getTarget());
    }
}