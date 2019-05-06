package org.ea.service.events;

import multiverse.server.engine.*;
import org.ea.service.objects.*;
import multiverse.server.network.*;

public abstract class MarsEvent extends Event {
    public MarsEvent() {
	super();
    }

    public MarsEvent(MarsObject obj) {
	super();
	setObject(obj);
    }

    public MarsEvent(MVByteBuffer buf, ClientConnection con) {
	super(buf,con);
    }

}
