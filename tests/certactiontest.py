#!/usr/bin/python

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import NetScaler as ns
import unittest


class TestAttribute(unittest.TestCase):

    def test_01_basic(self):
        name = 'certtest'
        attrs = None
        config1 = ns.NewConfig()
        config1.add_auth_certaction(name, attrs)
        expectedout = \
            'add authentication certAction {} \n'.format(name)

        self.assertEqual(str(config1), expectedout)

    def test_02_advanced(self):
        name = 'certtest'
        attrs = {
                "defaultAuthenticationGroup": "asdf",
                "groupNameField": "asdf",
                "twoFactor": "ON",
                "userNameField": "asdf"
            }
        config1 = ns.NewConfig()
        config1.add_auth_certaction(name, attrs)
        expectedout = \
            'add authentication certAction {} '.format(name) + \
            '-userNameField "{}" '.format(attrs['userNameField']) + \
            '-defaultAuthenticationGroup "{}" '.format(attrs['defaultAuthenticationGroup']) + \
            '-groupNameField "{}" '.format(attrs['groupNameField']) + \
            '-twoFactor {} '.format(attrs['twoFactor']) + \
            '\n'

        self.assertEqual(str(config1), expectedout)

if __name__ == '__main__':
    unittest.main()
