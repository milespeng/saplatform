import platform
try:
    from app_constant import *
except:
    pass

if platform.node() == "Whaley-PC1":
    from base import *
    from product import *
elif platform.node() == "Whaley-PC1.local":
    from base import *
    from dev import *
else:
    from base import *
    from test import *
