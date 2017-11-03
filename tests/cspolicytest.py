#!/usr/bin/python

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import NetScaler.Policy as Policy
import unittest

class TestAttribute(unittest.TestCase):

    def test_01_Basic(self):
        cspname = 'cspctname'
        expectedout = 'add cs policy {} '.format(cspname)

        orig = Policy(cspname, 'cspolicy')
        self.assertEqual(str(orig), expectedout)

    def test_02_Advanced(self):
        cspname = 'cspctname'
        expectedout = 'add cs policy {} '.format(cspname)

        orig = Policy(cspname, 'cspolicy', {
                "domain": "asdf",
                "logAction": "asdf",
                "url": "asdf",
                "rule": "asdf",
                "action": "sadf"

            })

        expectedout = 'add cs policy {} '.format(cspname) + \
            '-url asdf -logAction asdf -domain asdf -action "sadf" -rule "asdf" '
        self.assertEqual(str(orig), expectedout)

    def test_03_Repr(self):
        cspname = 'cspctname'
        expectedout = 'add cs policy {} '.format(cspname)

        orig = Policy(cspname, 'cspolicy', {
                "domain": "asdf",
                "logAction": "asdf",
                "url": "asdf",
                "rule": "asdf",
                "action": "sadf"

            })

        expected = '{  "objecttype": "cspolicy",  "name": "cspctname",  "Attributes": { ' + \
        '"url": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'url\', \'val\': \'asdf\'}, ' + \
        '"logAction": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'logAction\', \'val\': \'asdf\'}, ' + \
        '"domain": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'domain\', \'val\': \'asdf\'}, ' + \
        '"action": {\'default_value\': \'\', \'changed\': True, \'quoted\': True, \'key\': \'action\', \'val\': \'sadf\'}, ' + \
        '"rule": {\'default_value\': \'\', \'changed\': True, \'quoted\': True, \'key\': \'rule\', \'val\': \'asdf\'} } }'

        self.assertEqual(orig.__repr__(), expected)

if __name__ == '__main__':
    unittest.main()
