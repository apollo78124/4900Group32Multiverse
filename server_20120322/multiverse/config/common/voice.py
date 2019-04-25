from multiverse.msgsys import *
from multiverse.server.plugins import *
from multiverse.server.engine import *

False=0
True=1

voicePlugin = VoicePlugin();

Engine.registerPlugin(voicePlugin);
