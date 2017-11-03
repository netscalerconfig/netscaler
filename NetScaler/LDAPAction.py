from AttributeList import AttributeList
from NSObject import NSObject
import json
import socket

class LDAPAction(NSObject):
    def __init__(self, name, server, Attributes=None):
        self.InitVersion("12.0")
        self._objecttype = "ldapAction"
        self.name = name
        self.server = server
        if Attributes is not None:
            for x in Attributes:
                self.Attributes[x] = Attributes[x]
        self._locked = True

    def InitVersion(self, version):
        if version == '12.0':
            self.__dict__['Attributes'] = AttributeList({
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
                "authentication": "ENABLED",
                "authTimeout": "3",
                "defaultAuthenticationGroup": "",
                "followReferrals": "OFF",
                "maxLDAPReferrals": 1,
                "groupAttrName": "",
                "groupNameIdentifier": "",
                "groupSearchAttribute": "",
                "ldapBase": "",
                "ldapBindDn": "",
                "ldapHostname": "",
                "ldapLoginName": "",
                "nestedGroupExtraction": "OFF",
                "maxNestingLevel": 2,
                "groupSearchSubAttribute": "",
                "groupSearchFilter": "",
                "OTPSecret": "",
                "passwdChange": "DISABLED",
                "referralDNSLookup": "A-REC",
                "msSRVRecordlocation": "",
                "requireUser": "YES",
                "searchFilter": "",
                "secType": "PLAINTEXT",
                "serverPort": "389",
                "ssoNameAttribute": "",
                "subAttributeName": "",
                "svrType": "AD",
                "validateServerCert": "NO"
                })
            self.Attributes.Attribute1.setquoted(True)
            self.Attributes.Attribute2.setquoted(True)
            self.Attributes.Attribute3.setquoted(True)
            self.Attributes.Attribute4.setquoted(True)
            self.Attributes.Attribute5.setquoted(True)
            self.Attributes.Attribute6.setquoted(True)
            self.Attributes.Attribute7.setquoted(True)
            self.Attributes.Attribute8.setquoted(True)
            self.Attributes.Attribute9.setquoted(True)
            self.Attributes.Attribute10.setquoted(True)
            self.Attributes.Attribute11.setquoted(True)
            self.Attributes.Attribute12.setquoted(True)
            self.Attributes.Attribute13.setquoted(True)
            self.Attributes.Attribute14.setquoted(True)
            self.Attributes.Attribute15.setquoted(True)
            self.Attributes.Attribute16.setquoted(True)
            self.Attributes.defaultAuthenticationGroup.setquoted(True)
            self.Attributes.groupAttrName.setquoted(True)
            self.Attributes.groupNameIdentifier.setquoted(True)
            self.Attributes.groupSearchAttribute.setquoted(True)
            self.Attributes.ldapBase.setquoted(True)
            self.Attributes.ldapBindDn.setquoted(True)
            self.Attributes.ldapHostname.setquoted(True)
            self.Attributes.ldapLoginName.setquoted(True)
            self.Attributes.groupSearchSubAttribute.setquoted(True)
            self.Attributes.groupSearchFilter.setquoted(True)
            self.Attributes.OTPSecret.setquoted(True)
            self.Attributes.msSRVRecordlocation.setquoted(True)
            self.Attributes.searchFilter.setquoted(True)
            self.Attributes.ssoNameAttribute.setquoted(True)
            self.Attributes.subAttributeName.setquoted(True)

    def LocalAttributes(self):
        outstring  = " \"name\": {}, ".format(json.dumps(self.name))
        outstring += " \"server\": {}, ".format(json.dumps(self.server))
        return outstring

    def __str__(self):
        if self.is_ip(self.server):
            server = "-serverIP {}".format(self.server)
        else:
            server = "-serverName {}".format(self.server)

        outstring = "add authentication ldapAction " + self.name + " " + server + " " + \
            str(self.Attributes)
        return outstring


