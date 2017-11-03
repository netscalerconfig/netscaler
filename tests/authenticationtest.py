#!/usr/bin/python

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import NetScaler as ns
import unittest


class TestAttribute(unittest.TestCase):

    def test_01_tacacsbasic(self):
        nameact = 'tacacsact'
        namepol = 'tacacspol'
        server = '10.0.1.98'
        tacacssecret = 'asdf'
        attrs = None
        config1 = ns.NewConfig()
        config1.add_auth_tacacsaction(nameact, server, tacacssecret, attrs)
        config1.add_auth_tacacspolicy(namepol, { 'rule': 'true', 'action': nameact})
        expectedout = \
            'add authentication tacacsAction {} '.format(nameact) + \
            '-serverIP {} '.format(server) + \
            '-tacacssecret "{}" '.format(tacacssecret) + \
            '\n' + \
            'add authentication tacacspolicy {} '.format(namepol) + \
            '-action {} '.format(nameact) + \
            '-rule "{}" \n'.format('true')

        self.assertEqual(str(config1), expectedout)

    def test_02_tacacsadvanced(self):
        nameact = 'tacacsact'
        namepol = 'tacacspol'
        server = '10.0.1.98'
        tacacssecret = 'asdf'
        attrs = {
            "accounting": "ON",
            "Attribute1": "asdf",
            "Attribute10": "asdf",
            "Attribute11": "asdf",
            "Attribute12": "asdf",
            "Attribute13": "asdf",
            "Attribute14": "asdf",
            "Attribute15": "asdf",
            "Attribute16": "asdf",
            "Attribute2": "asdf",
            "Attribute3": "asdf",
            "Attribute4": "adfs",
            "Attribute5": "asdf",
            "Attribute6": "asdf",
            "Attribute7": "asdf",
            "Attribute8": "asdf",
            "Attribute9": "asdf",
            "auditFailedCmds": "ON",
            "authorization": "ON",
            "authTimeout": 4,
            "defaultAuthenticationGroup": "asdf",
            "groupAttrName": "adsf",
            "serverPort": "48"
            }
        config1 = ns.NewConfig()
        config1.add_auth_tacacsaction(nameact, server, tacacssecret, attrs)
        config1.add_auth_tacacspolicy(namepol, { 'rule': 'true', 'action': nameact})
        expectedout = \
            'add authentication tacacsAction {} '.format(nameact) + \
            '-serverIP {} '.format(server) + \
            '-tacacssecret "{}" '.format(tacacssecret) + \
            '-authTimeout {} '.format(attrs['authTimeout']) + \
            '-groupAttrName "{}" '.format(attrs['groupAttrName']) + \
            '-Attribute8 "{}" '.format(attrs['Attribute8']) + \
            '-Attribute9 "{}" '.format(attrs['Attribute9']) + \
            '-serverPort {} '.format(attrs['serverPort']) + \
            '-accounting {} '.format(attrs['accounting']) + \
            '-Attribute2 "{}" '.format(attrs['Attribute2']) + \
            '-Attribute3 "{}" '.format(attrs['Attribute3']) + \
            '-Attribute1 "{}" '.format(attrs['Attribute1']) + \
            '-Attribute6 "{}" '.format(attrs['Attribute6']) + \
            '-Attribute7 "{}" '.format(attrs['Attribute7']) + \
            '-Attribute4 "{}" '.format(attrs['Attribute4']) + \
            '-Attribute5 "{}" '.format(attrs['Attribute5']) + \
            '-authorization {} '.format(attrs['authorization']) + \
            '-Attribute10 "{}" '.format(attrs['Attribute10']) + \
            '-Attribute11 "{}" '.format(attrs['Attribute11']) + \
            '-Attribute12 "{}" '.format(attrs['Attribute12']) + \
            '-Attribute13 "{}" '.format(attrs['Attribute13']) + \
            '-Attribute14 "{}" '.format(attrs['Attribute14']) + \
            '-Attribute15 "{}" '.format(attrs['Attribute15']) + \
            '-Attribute16 "{}" '.format(attrs['Attribute16']) + \
            '-defaultAuthenticationGroup "{}" '.format(attrs['defaultAuthenticationGroup']) + \
            '-auditFailedCmds {} '.format(attrs['auditFailedCmds']) + \
            '\n' + \
            'add authentication tacacspolicy {} '.format(namepol) + \
            '-action {} '.format(nameact) +\
            '-rule "true" ' + \
            '\n'

        self.assertEqual(str(config1), expectedout)

    def test_03_certbasic(self):
        nameact = 'certact'
        namepol = 'certpol'
        attrs = None
        config1 = ns.NewConfig()
        config1.add_auth_certaction(nameact, attrs)
        config1.add_auth_certpolicy(namepol, { 'rule': 'true', 'action': nameact})
        expectedout = \
            'add authentication certAction {} '.format(nameact) + \
            '\n' + \
            'add authentication certpolicy {} '.format(namepol) + \
            '-action {} '.format(nameact) + \
            '-rule "true" ' + \
            '\n'

        self.assertEqual(str(config1), expectedout)

    def test_04_certadvanced(self):
        nameact = 'certact'
        namepol = 'certpol'
        attrs = {
                "defaultAuthenticationGroup": "asdf",
                "groupNameField": "asdf",
                "twoFactor": "ON",
                "userNameField": "asdf"
            }
        config1 = ns.NewConfig()
        config1.add_auth_certaction(nameact, attrs)
        config1.add_auth_certpolicy(namepol, { 'rule': 'true', 'action': nameact})
        expectedout = \
            'add authentication certAction {} '.format(nameact) + \
            '-userNameField "{}" '.format(attrs['userNameField']) + \
            '-defaultAuthenticationGroup "{}" '.format(attrs['defaultAuthenticationGroup']) + \
            '-groupNameField "{}" '.format(attrs['groupNameField']) + \
            '-twoFactor {} '.format(attrs['twoFactor']) + \
            '\n'+ \
            'add authentication certpolicy {} '.format(namepol) + \
            '-action {} '.format(nameact) + \
            '-rule "true" ' + \
            '\n'

        self.assertEqual(str(config1), expectedout)

    def test_05_radiusbasic(self):
        nameact = 'radiusact'
        namepol = 'radiuspol'
        server = '10.0.1.98'
        radkey = 'asdf'
        config1 = ns.NewConfig()
        config1.add_auth_radiusaction(nameact, server, radkey)
        config1.add_auth_radiuspolicy(namepol, { 'rule': 'true', 'action': nameact })
        expectedout = \
            'add authentication radiusAction {} '.format(nameact) + \
            '-serverIP {} '.format(server) + \
            '-radKey "{}" '.format(radkey) + \
            '\n' + \
            'add authentication radiuspolicy {} '.format(namepol) + \
            '-action {} '.format(nameact) + \
            '-rule "true" ' + \
            '\n'

        self.assertEqual(str(config1), expectedout)

    def test_06_radiusadvanced(self):
        nameact = 'radiusact'
        namepol = 'radiuspol'
        server = '10.0.1.98'
        radkey = 'asdf'
        attrs = {
            "accounting": "ON",
            "authentication": "OFF",
            "authservRetry": 4,
            "authTimeout": 4,
            "callingstationid": "ENABLED",
            "defaultAuthenticationGroup": "adf",
            "ipAttributeType": "adf",
            "ipVendorID": "asdf",
            "passEncoding": "chap",
            "pwdAttributeType": "adsf",
            "pwdVendorID": "asdf",
            "radAttributeType": "asdf",
            "radGroupSeparator": "adf",
            "radGroupsPrefix": "asdf",
            "radNASid": "asdf",
            "radNASip": "ENABLED",
            "radVendorID": "1",
            "serverPort": "1813",
            }
        config1 = ns.NewConfig()
        config1.add_auth_radiusaction(nameact, server, radkey, attrs)
        config1.add_auth_radiuspolicy(namepol, { 'rule': 'true', 'action': nameact })
        expectedout = \
            'add authentication radiusAction {} '.format(nameact) + \
            '-serverIP {} '.format(server) + \
            '-radKey "{}" '.format(radkey) + \
            '-passEncoding {} '.format(attrs['passEncoding']) + \
            '-callingstationid {} '.format(attrs['callingstationid']) + \
            '-radNASip {} '.format(attrs['radNASip']) + \
            '-radVendorID {} '.format(attrs['radVendorID']) + \
            '-authTimeout {} '.format(attrs['authTimeout']) + \
            '-defaultAuthenticationGroup "{}" '.format(attrs['defaultAuthenticationGroup']) + \
            '-radAttributeType {} '.format(attrs['radAttributeType']) + \
            '-authentication {} '.format(attrs['authentication']) + \
            '-radGroupSeparator "{}" '.format(attrs['radGroupSeparator']) + \
            '-authservRetry {} '.format(attrs['authservRetry']) + \
            '-radNASid "{}" '.format(attrs['radNASid']) + \
            '-ipVendorID {} '.format(attrs['ipVendorID']) + \
            '-serverPort {} '.format(attrs['serverPort']) + \
            '-pwdVendorID {} '.format(attrs['pwdVendorID']) + \
            '-accounting {} '.format(attrs['accounting']) + \
            '-radGroupsPrefix "{}" '.format(attrs['radGroupsPrefix']) + \
            '-pwdAttributeType {} '.format(attrs['pwdAttributeType']) + \
            '-ipAttributeType {} '.format(attrs['ipAttributeType']) + \
            '\n' + \
            'add authentication radiuspolicy {} '.format(namepol) + \
            '-action {} '.format(nameact) + \
            '-rule "true" ' + \
            '\n'

        self.assertEqual(str(config1), expectedout)


    def test_07_ldapbasic(self):
        nameact = 'ldapact'
        namepol = 'ldappol'
        server = '10.0.1.98'
        config1 = ns.NewConfig()
        config1.add_auth_ldapaction(nameact, server)
        config1.add_auth_ldappolicy(namepol, { 'rule': 'true', 'action': nameact })
        expectedout = \
            'add authentication ldapAction {} '.format(nameact) + \
            '-serverIP {} '.format(server) + \
            '\n' + \
            'add authentication ldappolicy {} '.format(namepol) + \
            '-action {} '.format(nameact) + \
            '-rule "true" ' + \
            '\n'

        self.assertEqual(str(config1), expectedout)

    def test_08_ldapadvanced(self):
        nameact = 'ldapact'
        namepol = 'ldappol'
        server = '10.0.1.98'
        attrs = {
            "groupAttrName": "cn",
            "ldapBase": "dc=test,dc=local",
            "ldapBindDn": "user@domain.com",
            "groupSearchFilter": "memberof",
            "ssoNameAttribute": "samaccountname",
            }
        config1 = ns.NewConfig()
        config1.add_auth_ldapaction(nameact, server, attrs)
        config1.add_auth_ldappolicy(namepol, { 'rule': 'true', 'action': nameact })
        expectedout = \
            'add authentication ldapAction {} '.format(nameact) + \
            '-serverIP {} '.format(server) + \
            '-ldapBindDn "{}" '.format(attrs['ldapBindDn']) + \
            '-groupAttrName "{}" '.format(attrs['groupAttrName']) + \
            '-ssoNameAttribute "{}" '.format(attrs['ssoNameAttribute']) + \
            '-ldapBase "{}" '.format(attrs['ldapBase']) + \
            '-groupSearchFilter "{}" '.format(attrs['groupSearchFilter']) + \
            '\n' + \
            'add authentication ldappolicy {} '.format(namepol) + \
            '-action {} '.format(nameact) + \
            '-rule "true" ' + \
            '\n'

        self.assertEqual(str(config1), expectedout)


if __name__ == '__main__':
    unittest.main()
