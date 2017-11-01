#!/usr/bin/python

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import NetScaler as ns
import unittest


class TestAttribute(unittest.TestCase):

    def test_01_basic(self):
        config1 = ns.NewConfig()
        config1.add_auth_ldapaction('ldaptest', '10.0.1.98')
        expectedout = \
            'add authentication ldapAction ldaptest -serverIP 10.0.1.98 \n'

        self.assertEqual(str(config1), expectedout)

    def test_02_advanced(self):
        config1 = ns.NewConfig()
        config1.add_auth_ldapaction('ldaptest', '10.0.1.98', {
            "groupAttrName": "cn",
            "ldapBase": "dc=test,dc=local",
            "ldapBindDn": "user@domain.com",
            "groupSearchFilter": "memberof",
            "ssoNameAttribute": "samaccountname",
            })
        expectedout = \
            'add authentication ldapAction ldaptest -serverIP 10.0.1.98 ' + \
            '-ldapBindDn "user@domain.com" ' + \
            '-groupAttrName "cn" ' + \
            '-ssoNameAttribute "samaccountname" ' + \
            '-ldapBase "dc=test,dc=local" ' + \
            '-groupSearchFilter "memberof" \n'

        self.assertEqual(str(config1), expectedout)

if __name__ == '__main__':
    unittest.main()
