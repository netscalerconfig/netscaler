from AttributeList import AttributeList
from NSObject import NSObject
import json

class CSPolicy(NSObject):
    def __init__(self, name, Attributes=None):
        self.InitVersion("12.0")
        self._objecttype = "cspolicy"
        self.name = name
        if Attributes is not None:
            for x in Attributes:
                self.Attributes[x] = Attributes[x]
        self._locked = True

    def InitVersion(self, version):
        if version == '12.0':
            self.__dict__['Attributes'] = AttributeList({
                "domain": "",
                "logAction": "",
                "url": "",
                "rule": "",
                "action": ""
                })
            self.Attributes.action.setquoted(True)
            self.Attributes.rule.setquoted(True)

    def LocalAttributes(self):
        outstring  = " \"name\": {}, ".format(json.dumps(self.name))
        return outstring

    def __str__(self):
        outstring = "add cs policy " + self.name + " " + \
            str(self.Attributes)
        return outstring
