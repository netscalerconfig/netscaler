from AttributeList import AttributeList
from NSObject import NSObject
import json

class Service(NSObject):
    def __init__(self, name, server, servicetype, port, Attributes=None):
        self.InitVersion("12.0")
        self._objecttype = "service"
        self.name = name
        self.server = server
        self.servicetype = servicetype
        self.port = port
        if Attributes is not None:
            for x in Attributes:
                self.Attributes[x] = Attributes[x]
        self._locked = True

    def InitVersion(self, version):
        if version == '12.0':
            self.__dict__['Attributes'] = AttributeList({
                "accessDown": "NO",
                "appflowLog": "ENABLED",
                "cacheable": "NO",
                "cacheType": "",
                "cip": "",
                "CKA": "NO",
                "clearTextPort": "",
                "cltTimeout": 180,
                "CMP": "NO",
                "comment": "",
                "CustomServerID": "",
                "dnsProfileName": "",
                "downStateFlush": "ENABLED",
                "hashId": "",
                "healthMonitor": "YES",
                "httpProfileName": "",
                "maxBandwidth": 0,
                "maxClient": 0,
                "maxReq": 0,
                "monConnectionClose": "NONE",
                "monThreshold": 0,
                "netProfile": "",
                "pathMonitor": "NO",
                "pathMonitorIndv": "NO",
                "processLocal": "DISABLED",
                "rtspSessionidRemap": "OFF",
                "sp": "ON",
                "state": "ENABLED",
                "svrTimeout": 360,
                "TCPB": "NO",
                "tcpProfileName": "",
                "td": 0,
                "useproxyport": "YES",
                "usip": "NO"
                })
            self.Attributes.comment.setquoted(True)

    def LocalAttributes(self):
        outstring  = " \"name\": {}, ".format(json.dumps(self.name))
        outstring += " \"server\": {}, ".format(json.dumps(self.server))
        outstring += " \"servicetype\": {}, ".format(json.dumps(self.servicetype))
        outstring += " \"port\": {}, ".format(json.dumps(self.port))
        return outstring

    def __str__(self):
        outstring = "add service " + self.name + " " + self.server + " " + \
            self.servicetype + " " + str(self.port) + " " + str(self.Attributes)
        return outstring
