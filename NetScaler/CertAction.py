from .AttributeList import AttributeList
from .NSObject import NSObject
import json

class CertAction(NSObject):
    def __init__(self, name, Attributes=None, version=None):
        if version is None:
            self._version = '12.0'
        else:
            self._version = version
        self.InitVersion()
        self._objecttype = "certAction"
        self.name = name
        if Attributes is not None:
            for x in Attributes:
                self.Attributes[x] = Attributes[x]
        self._locked = True

    def InitVersion(self):
        if self._version == '12.0':
            self.__dict__['Attributes'] = AttributeList({
                "defaultAuthenticationGroup": "",
                "groupNameField": "",
                "twoFactor": "OFF",
                "userNameField": ""
                })
            self.Attributes.defaultAuthenticationGroup.setquoted(True)
            self.Attributes.groupNameField.setquoted(True)
            self.Attributes.userNameField.setquoted(True)

    def LocalAttributes(self):
        outstring  = " \"name\": {}, ".format(json.dumps(self.name))
        return outstring

    def __str__(self):
        outstring = "add authentication certAction {} {}"\
            .format(self.name, str(self.Attributes))
        return outstring




