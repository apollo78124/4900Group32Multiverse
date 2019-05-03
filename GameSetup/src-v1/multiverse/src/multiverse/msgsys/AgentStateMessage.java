/********************************************************************

The Multiverse Platform is made available under the MIT License.

Copyright (c) 2012 The Multiverse Foundation

Permission is hereby granted, free of charge, to any person 
obtaining a copy of this software and associated documentation 
files (the "Software"), to deal in the Software without restriction, 
including without limitation the rights to use, copy, modify, 
merge, publish, distribute, sublicense, and/or sell copies 
of the Software, and to permit persons to whom the Software 
is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be 
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES 
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND 
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT 
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE 
OR OTHER DEALINGS IN THE SOFTWARE.

*********************************************************************/

package multiverse.msgsys;

import java.util.*;

public class AgentStateMessage extends Message
{
    public AgentStateMessage() {
    }

    public AgentStateMessage(int agentId, String agentName, String agentIP,
        int agentPort, int domainFlags)
    {
        msgType = MessageTypes.MSG_TYPE_AGENT_STATE;
        this.agentId = agentId;
        this.agentName = agentName;
        this.agentIP = agentIP;
        this.agentPort = agentPort;
        this.domainFlags = domainFlags;
    }

    public void setAdvertisements(List<MessageType> list)
    {
        advertisements = list;
    }

    public List<MessageType> getAdvertisements()
    {
        return advertisements;
    }

    int agentId;
    String agentName;
    String agentIP;
    int agentPort;
    int domainFlags;
    List<MessageType> advertisements = null;
    
    private static final long serialVersionUID = 1L;
}

