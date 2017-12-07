from .AttributeList import AttributeList
from .NSObject import NSObject
import json

class ServiceGroup(NSObject):
    def __init__(self, name, servicetype, Attributes=None):
        self.InitVersion("12.0")
        self._objecttype = "servicegroup"
        self.name = name
        self.servicetype = servicetype
        self.server_bind = {}
        if Attributes is not None:
            for x in Attributes:
                self.Attributes[x] = Attributes[x]
        self._locked = True

    def InitVersion(self, version):
        if version == '12.0':
            self.__dict__['Attributes'] = AttributeList({
                "appflowLog": "ENABLED",
                "autoScale": "DISABLED",
                "memberPort": "",
                "cacheable": "NO",
                "cacheType": "",
                "cip": "",
                "CKA": "NO",
                "cltTimeout": 180,
                "CMP": "NO",
                "comment": "",
                "downStateFlush": "ENABLED",
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
        outstring += " \"servicetype\": {}, ".format(json.dumps(self.servicetype))
        return outstring

    def __str__(self):
        outstring = "add servicegroup " + self.name + " " + \
            self.servicetype + " " + str(self.Attributes)
        for x in self.server_bind:
            outstring += '\n' + str(self.server_bind[x])
        return outstring
