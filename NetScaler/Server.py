from .AttributeList import AttributeList
from .NSObject import NSObject
import json

class Server(NSObject):

    def __init__(self, name, IPAddress, Attributes=None):
        self.InitVersion("12.0")
        self._objecttype = "server"
        self.name = name
        self.IPAddress = IPAddress
        if Attributes is not None:
            for x in Attributes:
                self.Attributes[x] = Attributes[x]
        self._locked = True

    def InitVersion(self, version):
        if version == '12.0':
            self.__dict__['Attributes'] = AttributeList({
                "domainResolveRetry": 0,
                "IPv6Address"       : "NO",
                "translationIp"     : "",
                "translationMask"   : "",
                "state"             : "ENABLED",
                "comment"           : ""
                })
            self.Attributes.comment.setquoted(True)

    def LocalAttributes(self):
        outstring = " \"name\": {}, ".format(json.dumps(self.name))
        outstring += " \"IPAddress\": {}, ".format(json.dumps(self.IPAddress))
        return outstring

    def __str__(self):
        outstring = "add server " + self.name + " " + \
            self.IPAddress + " " + str(self.Attributes)
        return outstring
