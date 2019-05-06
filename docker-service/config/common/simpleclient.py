from multiverse.server.util import *
from multiverse.simpleclient import *
from java.lang import *

loginType = 81

simpleClient = SimpleClient.getInstantiatingSimpleClient();

# LoginHandler
loginResponseHandler = LoginResponseHandler()
simpleClient.getDispatcher().registerHandler(loginType,
                                             loginResponseHandler)

# set up the login response handler to exit when it gets the msg
# this is useful for a monitoring script
# LoginResponseHandler.EXIT_ON_MSG = 1

Log.debug("completed simpleclient.py")
