from AttributeList import AttributeList
from NSObject import NSObject
import json
import socket

class RadiusAction(NSObject):
    def __init__(self, name, server, radkey, Attributes=None):
        self.InitVersion("12.0")
        self._objecttype = "radiusAction"
        self.name = name
        self.server = server
        self.radkey = radkey
        if Attributes is not None:
            for x in Attributes:
                self.Attributes[x] = Attributes[x]
        self._locked = True

    def InitVersion(self, version):
        if version == '12.0':
            self.__dict__['Attributes'] = AttributeList({
                "accounting": "OFF",
                "authentication": "ON",
                "authservRetry": 3,
                "authTimeout": 3,
                "callingstationid": "DISABLED",
                "defaultAuthenticationGroup": "",
                "ipAttributeType": "",
                "ipVendorID": "",
                "passEncoding": "pap",
                "pwdAttributeType": "",
                "pwdVendorID": "",
                "radAttributeType": "",
                "radGroupSeparator": "",
                "radGroupsPrefix": "",
                "radNASid": "",
                "radNASip": "DISABLED",
                "radVendorID": "",
                "serverPort": "1812",
                })
            self.Attributes.defaultAuthenticationGroup.setquoted(True)
            self.Attributes.radGroupSeparator.setquoted(True)
            self.Attributes.radGroupsPrefix.setquoted(True)
            self.Attributes.radNASid.setquoted(True)

    def LocalAttributes(self):
        outstring  = " \"name\": {}, ".format(json.dumps(self.name))
        outstring += " \"server\": {}, ".format(json.dumps(self.server))
        return outstring

    def __str__(self):
        if self.is_ip(self.server):
            server = "-serverIP {}".format(self.server)
        else:
            server = "-serverName {}".format(self.server)

        outstring = "add authentication radiusAction {} {} -radKey \"{}\" {}"\
            .format(self.name, server, self.radkey, str(self.Attributes))
        return outstring



