package org.ea.service.plugins;

import multiverse.server.plugins.*;
import multiverse.server.events.*;
import multiverse.server.network.*;

/**
 * handles client traffic to the rest of the servers
 */
public class MarsProxyPlugin extends ProxyPlugin {
    
    /**
     * process login message from the client.
     */
    protected boolean processLogin(
	ClientConnection con, AuthorizedLoginEvent loginEvent) {

        if (! super.processLogin(con, loginEvent))
	    return false;
        
        // Example: get the inventory

        return true;
    }

}
