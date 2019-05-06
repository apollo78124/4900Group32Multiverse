package org.ea.service.behaviors;

import java.util.concurrent.*;

import multiverse.msgsys.*;
import multiverse.server.engine.*;
import multiverse.server.objects.*;
import multiverse.server.math.*;
import multiverse.server.util.*;

public class RadiusRoamBehavior extends Behavior implements MessageCallback, Runnable {
    public RadiusRoamBehavior() {
	super();
    }

    public RadiusRoamBehavior(SpawnData data) {
	super(data);
	setCenterLoc(data.getLoc());
	setRadius(data.getSpawnRadius());
    }

    public void initialize() {
        SubjectFilter filter = new SubjectFilter(obj.getOid());
        filter.addType(Behavior.MSG_TYPE_EVENT);
        eventSub = Engine.getAgent().createSubscription(filter, this);
    }

    public void activate() {
	activated = true;
        startRoam();
    }

    public void deactivate() {
	lock.lock();
	try {
	    activated = false;
	    if (eventSub != null) {
                Engine.getAgent().removeSubscription(eventSub);
		eventSub = null;
	    }
	}
	finally {
	    lock.unlock();
	}
    }

    public void handleMessage(Message msg, int flags) {
	if (activated == false) {
	    return; //return true;
	}
        if (msg.getMsgType() == Behavior.MSG_TYPE_EVENT) {
	    String event = ((Behavior.EventMessage)msg).getEvent();
	    if (event.equals(BaseBehavior.MSG_EVENT_TYPE_ARRIVED)) {
		Engine.getExecutor().schedule(this, lingerTime, TimeUnit.MILLISECONDS);
	    }
        }
        //return true;
    }

    public void setCenterLoc(Point loc) {
	centerLoc = loc;
    }
    public Point getCenterLoc() {
	return centerLoc;
    }
    protected Point centerLoc = null;

    public void setRadius(int radius) {
	this.radius = radius;
    }
    public int getRadius() {
	return radius;
    }
    protected int radius = 0;

    public void setLingerTime(long time) {
        lingerTime = time;
    }
    public long getLingerTime() {
        return lingerTime;
    }
    protected long lingerTime = 5000;

    public void setMovementSpeed(int speed) {
        this.speed = new Integer(speed);
    }
    public int getMovementSpeed() {
        return speed.intValue();
    }
    protected Integer speed = new Integer(3000);

    protected void startRoam() {
        nextRoam();
    }

    protected void nextRoam() {
        Point roamPoint = Points.findNearby(centerLoc, radius);
        Engine.getAgent().sendBroadcast(new BaseBehavior.GotoCommandMessage(obj, roamPoint, speed));
    }

    public void run() {
	if (activated == false) {
	    return;
	}
        nextRoam();
    }

    Long eventSub = null;

    protected boolean activated = false;

    private static final long serialVersionUID = 1L;
}
