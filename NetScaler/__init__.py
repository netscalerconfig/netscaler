from .Attribute import Attribute
from .AttributeList import AttributeList
from .Server import Server
from .Service import Service
from .ServiceGroup import ServiceGroup
from .LBvServer import LBvServer
from .CSvServer import CSvServer
from .VPNvServer import VPNvServer
from .CSAction import CSAction
from .LDAPAction import LDAPAction
from .RadiusAction import RadiusAction
from .TacacsAction import TacacsAction
from .CertAction import CertAction
from .Policy import Policy
from .Config import Config

conf = Config()

def NewConfig():
    return Config()