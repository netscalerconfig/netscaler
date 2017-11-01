#!/usr/bin/python

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import NetScaler as ns
import unittest


class TestAttribute(unittest.TestCase):

    def test_01_basic(self):
        name = 'tacacstest'
        server = '10.0.1.98'
        tacacssecret = 'asdf'
        attrs = None
        config1 = ns.NewConfig()
        config1.add_auth_tacacsaction(name, server, tacacssecret, attrs)
        expectedout = \
            'add authentication tacacsAction {} '.format(name) + \
            '-serverIP {} '.format(server) + \
            '-tacacssecret "{}" \n'.format(tacacssecret)

        self.assertEqual(str(config1), expectedout)

    def test_02_advanced(self):
        name = 'tacacstest'
        server = '10.0.1.98'
        tacacssecret = 'asdf'
        attrs = {
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
            }
        config1 = ns.NewConfig()
        config1.add_auth_tacacsaction(name, server, radkey, attrs)
        expectedout = \
            'add authentication tacacsAction {} '.format(name) + \
            '-serverIP {} '.format(server) + \
            '-radKey "{}" '.format(radkey) + \
            '-accounting {} '.format(accounting) + \
            '-Attribute1 "{}" '.format(Attribute1) + \
            '-Attribute10 "{}" '.format(Attribute10) + \
            '-Attribute11 "{}" '.format(Attribute11) + \
            '-Attribute12 "{}" '.format(Attribute12) + \
            '-Attribute13 "{}" '.format(Attribute13) + \
            '-Attribute14 "{}" '.format(Attribute14) + \
            '-Attribute15 "{}" '.format(Attribute15) + \
            '-Attribute16 "{}" '.format(Attribute16) + \
            '-Attribute2 "{}" '.format(Attribute2) + \
            '-Attribute3 "{}" '.format(Attribute3) + \
            '-Attribute4 "{}" '.format(Attribute4) + \
            '-Attribute5 "{}" '.format(Attribute5) + \
            '-Attribute6 "{}" '.format(Attribute6) + \
            '-Attribute7 "{}" '.format(Attribute7) + \
            '-Attribute8 "{}" '.format(Attribute8) + \
            '-Attribute9 "{}" '.format(Attribute9) + \
            '-auditFailedCmds {} '.format(auditFailedCmds) + \
            '-authorization {} '.format(authorization) + \
            '-authTimeout {} '.format(authTimeout) + \
            '-defaultAuthenticationGroup "{}" '.format(defaultAuthenticationGroup) + \
            '-groupAttrName "{}" '.format(groupAttrName) + \
            '-serverPort {} '.format(serverPort)

        self.assertEqual(str(config1), expectedout)

if __name__ == '__main__':
    unittest.main()
