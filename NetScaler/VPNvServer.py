from .AttributeList import AttributeList
from .NSObject import NSObject
import json

class VPNvServer(NSObject):
    def __init__(self, name, servicetype, IPAddress, port, Attributes=None):
        self.InitVersion("12.0")
        self._objecttype = "vpnvserver"
        self.name = name
        self.servicetype = servicetype
        self.ipaddress = IPAddress
        self.port = port
        if Attributes is not None:
            for x in Attributes:
                self.Attributes[x] = Attributes[x]
        self._locked = True

    def InitVersion(self, version):
        if version == '12.0':
            self.__dict__['Attributes'] = AttributeList({
                "appflowLog": "DISABLED",
                "authentication": "ON",
                "authnProfile": "",
                "cginfraHomePageRedirect": "ENABLED",
                "comment": "",
                "deploymentType": "NONE",
                "deviceCert": "OFF",
                "doubleHop": "DISABLED",
                "downStateFlush": "ENABLED",
                "dtls": "OFF",
                "httpProfileName": "",
                "icaOnly": "OFF",
                "icaProxySessionMigration": "OFF",
                "icmpVsrResponse": "PASSIVE",
                "l2Conn": "OFF",
                "LinuxEPAPluginUpgrade": "",
                "Listenpolicy": "NONE",
                "loginOnce": "OFF",
                "logoutOnSmartcardRemoval": "OFF",
                "MacEPAPluginUpgrade": "",
                "maxAAAUsers": 0,
                "maxLoginAttempts": 0,
                "netProfile": "",
                "pcoipVserverProfileName": "",
                "rdpServerProfileName": "",
                "RHIstate": "PASSIVE",
                "state": "ENABLED",
                "tcpProfileName": "",
                "vserverFqdn": "",
                "WindowsEPAPluginUpgrade": "",
                })
            self.Attributes.comment.setquoted(True)

    def LocalAttributes(self):
        outstring  = " \"name\": {}, ".format(json.dumps(self.name))
        outstring += " \"servicetype\": {}, ".format(json.dumps(self.servicetype))
        outstring += " \"ipaddress\": {}, ".format(json.dumps(self.ipaddress))
        outstring += " \"port\": {}, ".format(json.dumps(self.port))
        return outstring

    def __str__(self):
        outstring = "add vpn vserver " + self.name + " " + self.servicetype + " " + \
            self.ipaddress + " " + str(self.port) + " " + \
            str(self.Attributes)
        return outstring





