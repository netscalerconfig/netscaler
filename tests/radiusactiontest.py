#!/usr/bin/python

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import NetScaler as ns
import unittest


class TestAttribute(unittest.TestCase):

    def test_01_basic(self):
        config1 = ns.NewConfig()
        config1.add_auth_radiusaction('radtest', '10.0.1.98', 'asdf')
        expectedout = \
            'add authentication radiusAction radtest -serverIP 10.0.1.98 -radKey "asdf" \n'

        self.assertEqual(str(config1), expectedout)

    def test_02_advanced(self):
        name = 'radtest'
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
        config1.add_auth_radiusaction(name, server, radkey, attrs)
        expectedout = \
            'add authentication radiusAction {} '.format(name) + \
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
            '-ipAttributeType {} \n'.format(attrs['ipAttributeType'])

        self.assertEqual(str(config1), expectedout)

if __name__ == '__main__':
    unittest.main()
