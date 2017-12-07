from .AttributeList import AttributeList
from .NSObject import NSObject
import json
import socket

class TacacsAction(NSObject):
    def __init__(self, name, server, tacacssecret, Attributes=None):
        self.InitVersion("12.0")
        self._objecttype = "tacacsAction"
        self.name = name
        self.server = server
        self.tacacssecret = tacacssecret
        if Attributes is not None:
            for x in Attributes:
                self.Attributes[x] = Attributes[x]
        self._locked = True

    def InitVersion(self, version):
        if version == '12.0':
            self.__dict__['Attributes'] = AttributeList({
                "accounting": "OFF",
                "Attribute1": "",
                "Attribute10": "",
                "Attribute11": "",
                "Attribute12": "",
                "Attribute13": "",
                "Attribute14": "",
                "Attribute15": "",
                "Attribute16": "",
                "Attribute2": "",
                "Attribute3": "",
                "Attribute4": "",
                "Attribute5": "",
                "Attribute6": "",
                "Attribute7": "",
                "Attribute8": "",
                "Attribute9": "",
                "auditFailedCmds": "OFF",
                "authorization": "OFF",
                "authTimeout": 3,
                "defaultAuthenticationGroup": "",
                "groupAttrName": "",
                "serverPort": "49"
                })
            self.Attributes.Attribute1.setquoted(True)
            self.Attributes.Attribute10.setquoted(True)
            self.Attributes.Attribute11.setquoted(True)
            self.Attributes.Attribute12.setquoted(True)
            self.Attributes.Attribute13.setquoted(True)
            self.Attributes.Attribute14.setquoted(True)
            self.Attributes.Attribute15.setquoted(True)
            self.Attributes.Attribute16.setquoted(True)
            self.Attributes.Attribute2.setquoted(True)
            self.Attributes.Attribute3.setquoted(True)
            self.Attributes.Attribute4.setquoted(True)
            self.Attributes.Attribute5.setquoted(True)
            self.Attributes.Attribute6.setquoted(True)
            self.Attributes.Attribute7.setquoted(True)
            self.Attributes.Attribute8.setquoted(True)
            self.Attributes.Attribute9.setquoted(True)
            self.Attributes.defaultAuthenticationGroup.setquoted(True)
            self.Attributes.groupAttrName.setquoted(True)

    def LocalAttributes(self):
        outstring  = " \"name\": {}, ".format(json.dumps(self.name))
        outstring += " \"server\": {}, ".format(json.dumps(self.server))
        return outstring

    def __str__(self):
        outstring = "add authentication tacacsAction {} -serverIP {} -tacacssecret \"{}\" {}"\
            .format(self.name, self.server, self.tacacssecret, str(self.Attributes))
        return outstring




