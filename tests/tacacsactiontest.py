#!/usr/bin/python

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import NetScaler as ns
import unittest


class TestAttribute(unittest.TestCase):

    def test_01_basic(self):
        nameact = 'tacacsact'
        server = '10.0.1.98'
        tacacssecret = 'asdf'
        attrs = None
        config1 = ns.NewConfig()
        config1.add_auth_tacacsaction(nameact, server, tacacssecret, attrs)
        expectedout = \
            'add authentication tacacsAction {} '.format(nameact) + \
            '-serverIP {} '.format(server) + \
            '-tacacssecret "{}" '.format(tacacssecret) + \
            '\n'

        self.assertEqual(str(config1), expectedout)

    def test_02_advanced(self):
        nameact = 'tacacsact'
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
            '\n' 

        self.assertEqual(str(config1), expectedout)

if __name__ == '__main__':
    unittest.main()
