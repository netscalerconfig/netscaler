from AttributeList import AttributeList
from NSObject import NSObject
import json

class LBvServer(NSObject):
    def __init__(self, name, servicetype, IPAddress, port, Attributes=None):
        self.InitVersion("12.0")
        self._objecttype = "lbvserver"
        self.name = name
        self.servicetype = servicetype
        self.ipaddress = IPAddress
        self.port = port
        self.svc_bind = {} # service and service groups
        self.rsp_bind = {}
        self.rwp_bind = {}
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
                "appflowLog": "DISABLED",
                "Authentication": "OFF",
                "AuthenticationHost": "",
                "authn401": "OFF",
                "authnProfile": "",
                "authnVs": "",
                "backupLB": "ROUNDROBIN",
                "backupPersistence": 0,
                "backupVServer": "",
                "bypassAAAA": "NO",
                "cacheable": "NO",
                "cltTimeout": 180,
                "comment": "",
                "connfailover": "DISABLED",
                "cookieName": "",
                "dbProfileName": "",
                "dbsLb": "DISABLED",
                "disablePrimaryOnDown": "DISABLED",
                "dns64": "DISABLED",
                "dnsProfileName": "",
                "downStateFlush": "ENABLED",
                "healthThreshold": 0,
                "httpProfileName": "",
                "httpsRedirectUrl": "",
                "icmpVsrResponse": "PASSIVE",
                "insertVserverIPPort": "OFF",
                "l2Conn": "OFF",
                "lbMethod": "LEASTCONNECTION",
                "lbprofilename": "",
                "Listenpolicy": "",
                "Listenpriority": "",
                "m": "IP",
                "macmodeRetainvlan": "DISABLED",
                "maxAutoscaleMembers": 0,
                "minAutoscaleMembers": 0,
                "mssqlServerVersion": "",
                "mysqlCharacterSet": "",
                "mysqlProtocolVersion": "",
                "mysqlServerCapabilities": "",
                "mysqlServerVersion": "",
                "netProfile": "",
                "newServiceRequest": 0,
                "newServiceRequestIncrementInterval": 0,
                "oracleServerVersion": "",
                "persistAVPno": 1,
                "persistenceBackup": "NONE",
                "persistenceType": "NONE",
                "persistMask": "",
                "processLocal": "DISABLED",
                "push": "DISABLED",
                "pushLabel": "",
                "pushMultiClients": "NO",
                "pushVserver": "",
                "RecursionAvailable": "",
                "redirectFromPort": "",
                "redirectPortRewrite": "DISABLED",
                "redirectURL": "",
                "resRule": "",
                "retainConnectionsOnCluster": "NO",
                "RHIstate": "PASSIVE",
                "rtspNat": "OFF",
                "rule": "",
                "sessionless": "DISABLED",
                "skippersistency": "None",
                "soBackupAction": "",
                "soMethod": "NONE",
                "soPersistence": "DISABLED",
                "soPersistenceTimeOut": 0,
                "soThreshold": 0,
                "state" : "ENABLED",
                "tcpProfileName": "",
                "timeout": 0,
                "tosId": "",
                "trofsPersistence": "ENABLED",
                "v6persistmasklen": "128"
                })
            self.Attributes.comment.setquoted(True)

    def LocalAttributes(self):
        outstring  = " \"name\": {}, ".format(json.dumps(self.name))
        outstring += " \"servicetype\": {}, ".format(json.dumps(self.servicetype))
        outstring += " \"ipaddress\": {}, ".format(json.dumps(self.ipaddress))
        outstring += " \"port\": {}, ".format(json.dumps(self.port))
        return outstring

    def __str__(self):
        outstring = "add lb vserver " + self.name + " " + self.servicetype + " " + \
            self.ipaddress + " " + str(self.port) + " " + str(self.Attributes)
        for x in self.svc_bind:
            outstring += '\n'
            outstring += str(self.svc_bind[x])
        return outstring
