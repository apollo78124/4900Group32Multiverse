package java.main.multiverse.mars.service.core;

import multiverse.mars.objects.*;
import java.io.*;

/**
 * used with marsitems - this gets called when a user activates this
 * item
 */
public interface ActivateHook extends Serializable {

    /**
     * returns whether the item was successfully activated
     */
    public boolean activate(Long activator, MarsItem item, Long target);
}
