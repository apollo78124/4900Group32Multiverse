package org.ea.service.objects;

import multiverse.msgsys.*;

import java.util.*;

public class DeliveryQuestState extends QuestState {
    public DeliveryQuestState() {
    }

    public DeliveryQuestState(MarsQuest quest,
                              Long playerOid) {
        super(quest, playerOid);
    }

    public List<String> getObjectiveStatus() {
        return new LinkedList<String>();
    }

    /**
     * called when a mob is killed that the player is getting credit for
     */
    public void handleDeath(MarsMob mobKilled) {
//         if (completed()) {
//             return;
//         }
    }

    String mobName = null;
    int count = 0;
    int currentCount = 0;

    public void activate() {
        // TODO Auto-generated method stub
        
    }

    public void deactivate() {
        // TODO Auto-generated method stub
        
    }

    public void handleMessage(Message msg, int flags) {
        // TODO Auto-generated method stub
        //return false;
    }

    private static final long serialVersionUID = 1L;
}
