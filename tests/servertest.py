#!/usr/bin/python

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import NetScaler.Server as Server
import unittest

class TestAttribute(unittest.TestCase):

    def test_01_BasicServer(self):
        orig = Server('test', '1.1.1.1')
        self.assertEqual(str(orig), 'add server test 1.1.1.1 ')

    def test_02_AdvancedServer(self):
        orig = Server('test', '1.1.1.1', { 
                "domainResolveRetry": 10,
                "IPv6Address"       : "YES",
                "translationIp"     : "10.10.10.10",
                "translationMask"   : "255.255.255.255",
                "state"             : "DISABLED",
                "comment"           : "This is a comment"
            })
        self.assertEqual(str(orig), 'add server test 1.1.1.1 -comment \"This is a comment\" ' + \
                '-translationMask 255.255.255.255 -IPv6Address YES ' + \
                '-domainResolveRetry 10 -state DISABLED -translationIp 10.10.10.10 ')

    def test_03_Repr(self):
        orig = Server('test', '1.1.1.1', { 
                "domainResolveRetry": 10,
                "IPv6Address"       : "YES",
                "translationIp"     : "10.10.10.10",
                "translationMask"   : "255.255.255.255",
                "state"             : "DISABLED",
                "comment"           : "This is a comment"
            })
        expected = '{  "objecttype": "server",  "name": "test",  "IPAddress": "1.1.1.1",  ' + \
            '"Attributes": { ' + \
            '"comment": {\'default_value\': \'\', \'changed\': True, \'quoted\': True, \'key\': \'comment\', \'val\': \'This is a comment\'}, ' + \
            '"translationMask": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'translationMask\', \'val\': \'255.255.255.255\'}, ' + \
            '"IPv6Address": {\'default_value\': \'NO\', \'changed\': True, \'quoted\': False, \'key\': \'IPv6Address\', \'val\': \'YES\'}, ' + \
            '"domainResolveRetry": {\'default_value\': 0, \'changed\': True, \'quoted\': False, \'key\': \'domainResolveRetry\', \'val\': 10}, ' + \
            '"state": {\'default_value\': \'ENABLED\', \'changed\': True, \'quoted\': False, \'key\': \'state\', \'val\': \'DISABLED\'}, ' + \
            '"translationIp": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'translationIp\', \'val\': \'10.10.10.10\'} } }'
        self.assertEqual(orig.__repr__(), expected)

if __name__ == '__main__':
    unittest.main()
