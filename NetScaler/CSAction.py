from AttributeList import AttributeList
from NSObject import NSObject
import json

class CSAction(NSObject):
    def __init__(self, name, Attributes=None):
        self.InitVersion("12.0")
        self._objecttype = "csaction"
        self.name = name
        if Attributes is not None:
            for x in Attributes:
                self.Attributes[x] = Attributes[x]
        self._locked = True

    def InitVersion(self, version):
        if version == '12.0':
            self.__dict__['Attributes'] = AttributeList({
                "comment": "",
                "targetLBVserver": "",
                "targetVserver": "",
                "targetVserverExpr": ""
                })
            self.Attributes.comment.setquoted(True)

    def LocalAttributes(self):
        outstring  = " \"name\": {}, ".format(json.dumps(self.name))
        return outstring

    def __str__(self):
        outstring = "add cs action " + self.name + " " + \
            str(self.Attributes)
        return outstring
