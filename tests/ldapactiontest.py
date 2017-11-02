#!/usr/bin/python

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import NetScaler as ns
import unittest


class TestAttribute(unittest.TestCase):

    def test_01_basic(self):
        nameact = 'ldapact'
        server = '10.0.1.98'
        config1 = ns.NewConfig()
        config1.add_auth_ldapaction(nameact, server)
        expectedout = \
            'add authentication ldapAction {} '.format(nameact) + \
            '-serverIP {} '.format(server) + \
            '\n'

        self.assertEqual(str(config1), expectedout)

    def test_02_advanced(self):
        nameact = 'ldapact'
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
        expectedout = \
            'add authentication ldapAction {} '.format(nameact) + \
            '-serverIP {} '.format(server) + \
            '-ldapBindDn "{}" '.format(attrs['ldapBindDn']) + \
            '-groupAttrName "{}" '.format(attrs['groupAttrName']) + \
            '-ssoNameAttribute "{}" '.format(attrs['ssoNameAttribute']) + \
            '-ldapBase "{}" '.format(attrs['ldapBase']) + \
            '-groupSearchFilter "{}" '.format(attrs['groupSearchFilter']) + \
            '\n'

        self.assertEqual(str(config1), expectedout)

if __name__ == '__main__':
    unittest.main()
