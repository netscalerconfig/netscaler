from .AttributeList import AttributeList
from .NSObject import NSObject
import json

class CSvServer(NSObject):
    def __init__(self, name, servicetype, IPAddress, port, Attributes=None):
        self.InitVersion("12.0")
        self._objecttype = "cs vserver"
        self.name = name
        self.servicetype = servicetype
        self.ipaddress = IPAddress
        self.port = port
        self.csdefault = None
        self.csp_bind = {} # service and service groups
        self.rsp_bind = {}
        self.rwp_bind = {}
        self.comment_list = []
        if Attributes is not None:
            for x in Attributes:
                self.Attributes[x] = Attributes[x]
        self._locked = True

    def InitVersion(self, version):
        if version == '12.0':
            self.__dict__['Attributes'] = AttributeList({
                "range": "",
                "IPPattern": "",
                "IPMask": "",
                "targetType": "",
                "appflowLog": "DISABLED",
                "Authentication": "OFF",
                "AuthenticationHost": "",
                "authn401": "OFF",
                "authnProfile": "",
                "authnVs": "",
                "backupVServer": "",
                "cacheable": "NO",
                "caseSensitive": "ON",
                "cltTimeout": 180,
                "comment": "",
                "dbProfileName": "",
                "dbsLb": "DISABLED",
                "disablePrimaryOnDown": "DISABLED",
                "dnsProfileName": "",
                "dnsRecordType": "",
                "downStateFlush": "ENABLED",
                "httpProfileName": "",
                "icmpVsrResponse": "PASSIVE",
                "insertVserverIPPort": "OFF",
                "l2Conn": "OFF",
                "Listenpolicy": "",
                "Listenpriority": "",
                "mssqlServerVersion": "",
                "mysqlCharacterSet": "",
                "mysqlProtocolVersion": "",
                "mysqlServerCapabilities": "",
                "mysqlServerVersion": "",
                "netProfile": "",
                "oracleServerVersion": "",
                "persistenceId": "",
                "presedence": "RULE",
                "push": "DISABLED",
                "pushLabel": "",
                "pushMultiClients": "NO",
                "pushVserver": "",
                "redirectPortRewrite": "DISABLED",
                "redirectURL": "",
                "RHIstate": "PASSIVE",
                "rtspNat": "OFF",
                "soBackupAction": "",
                "soMethod": "NONE",
                "soPersistence": "DISABLED",
                "soPersistenceTimeOut": 0,
                "soThreshold": 0,
                "state" : "ENABLED",
                "tcpProfileName": "",
                "td": 0
                })
            self.Attributes.comment.setquoted(True)

    def LocalAttributes(self):
        outstring  = " \"name\": {}, ".format(json.dumps(self.name))
        outstring += " \"servicetype\": {}, ".format(json.dumps(self.servicetype))
        outstring += " \"ipaddress\": {}, ".format(json.dumps(self.ipaddress))
        outstring += " \"port\": {}, ".format(json.dumps(self.port))
        return outstring

    def setCSDefault(self, vs):
        self.__dict__['csdefault'] = vs

    def __str__(self):
        outstring = ""
        if len(self.comment_list) > 0:
            outstring += '\n##### the following cs vserver has comments'
            for x in self.comment_list:
                outstring += '\n# ' + x
            outstring += '\n'
        outstring += "add cs vserver " + self.name + " " + self.servicetype + " " + \
            self.ipaddress + " " + str(self.port) + " " + str(self.Attributes)
        if self.csdefault is not None:
            outstring += '\n' + str(self.csdefault)
        for x in self.csp_bind:
            outstring += '\n' + str(self.csp_bind[x])
        return outstring
