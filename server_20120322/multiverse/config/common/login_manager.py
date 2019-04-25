from multiverse.mars import *
from multiverse.mars.objects import *
from multiverse.mars.util import *
from multiverse.server.math import *
from multiverse.server.events import *
from multiverse.server.objects import *
from multiverse.server.engine import *
from multiverse.server.util import *
from multiverse.msgsys import *

# test master key
pubkey = """AAAAAAAAAAwAAAADRFNBMIIBuDCCASwGByqGSM44BAEwggEfAoGBAP1/U4EddRIpUt9KnC7s5Of2
            EbdSPO9EAMMeP4C2USZpRV1AIlH7WT2NWPq/xfW6MPbLm1Vs14E7gB00b/JmYLdrmVClpJ+f6AR7
            ECLCT7up1/63xhv4O1fnxqimFQ8E+4P208UewwI1VBNaFpEy9nXzrith1yrv8iIDGZ3RSAHHAhUA
            l2BQjxUjC8yykrmCouuEC/BYHPUCgYEA9+GghdabPd7LvKtcNrhXuXmUr7v6OuqC+VdMCz0HgmdR
            WVeOutRZT+ZxBxCBgLRJFnEj6EwoFhO3zwkyjMim4TwWeotUfI0o4KOuHiuzpnWRbqN/C/ohNWLx
            +2J6ASQ7zKTxvqhRkImog9/hWuWfBpKLZl6Ae1UlZAFMO/7PSSoDgYUAAoGBALJagda9mnhVzF1Z
            +p0XcU9uzzjtNe+J3MoYiioRKlXlk3KV1oX+L3uj27bBnZHWYe6hi7pN9aex+AjC7FjnPtyyBE+F
            v7HHp1/YOcVqn2oq9VglOSJV/qhn+FVaRCF5s9tYPyyIVvwMi0oLZgNysRRrVoqpHfmftqbYFhYo
            EfYp"""

SecureTokenManager.getInstance().registerMasterPublicKey(Base64.decode(pubkey))

# production master key id=1
pubkey = """AAAAAAAAAAEAAAADRFNBMIIBuDCCASwGByqGSM44BAEwggEfAoGBAP1/U4EddRIpUt9KnC7s5Of2
            EbdSPO9EAMMeP4C2USZpRV1AIlH7WT2NWPq/xfW6MPbLm1Vs14E7gB00b/JmYLdrmVClpJ+f6AR7
            ECLCT7up1/63xhv4O1fnxqimFQ8E+4P208UewwI1VBNaFpEy9nXzrith1yrv8iIDGZ3RSAHHAhUA
            l2BQjxUjC8yykrmCouuEC/BYHPUCgYEA9+GghdabPd7LvKtcNrhXuXmUr7v6OuqC+VdMCz0HgmdR
            WVeOutRZT+ZxBxCBgLRJFnEj6EwoFhO3zwkyjMim4TwWeotUfI0o4KOuHiuzpnWRbqN/C/ohNWLx
            +2J6ASQ7zKTxvqhRkImog9/hWuWfBpKLZl6Ae1UlZAFMO/7PSSoDgYUAAoGBAI1obFDPxAHhfzeY
            pMSxJhplwKldDVBpG3TNAj18FaoqMsWq2mjI1VN2i9jLjhhbl7DgFIWvXBqaJ8BO75uGMQL+uEvl
            GQaQ7ClgGpWn0YLxUd1Hja+Q7SmKnkWmrhMYiq84O/2GP6hTfmidVd7STy3PoXuSf50Ph2tumuai
            UyZ5"""

SecureTokenManager.getInstance().registerMasterPublicKey(Base64.decode(pubkey))

Engine.registerPlugin("multiverse.mars.plugins.MarsLoginPlugin")
