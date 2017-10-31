#!/usr/bin/python

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import NetScaler.CSAction as CSAction
import unittest

class TestAttribute(unittest.TestCase):

    def test_01_Basic(self):
        csaname = 'csactname'
        expectedout = 'add cs action {} '.format(csaname)

        orig = CSAction(csaname)
        self.assertEqual(str(orig), expectedout)

    def test_02_Advanced(self):
        csaname = 'csactname'
        orig = CSAction(csaname, {
                "comment": "This is a comment",
                "targetLBVserver": "asdf",
                "targetVserver": "asdf",
                "targetVserverExpr": "asdf"
            })

        expectedout = 'add cs action {} '.format(csaname) + \
            '-comment "This is a comment" -targetVserver asdf -targetVserverExpr asdf -targetLBVserver asdf '
        self.assertEqual(str(orig), expectedout)

    def test_03_Repr(self):
        csaname = 'csactname'
        orig = CSAction(csaname, {
                "comment": "This is a comment",
                "targetLBVserver": "asdf",
                "targetVserver": "asdf",
                "targetVserverExpr": "asdf"
            })

        expectedout = '{  "objecttype": "csaction",  "name": "csactname",  ' + \
            '"Attributes": { ' + \
            '"comment": {\'default_value\': \'\', \'changed\': True, \'quoted\': True, \'key\': \'comment\', \'val\': \'This is a comment\'}, ' + \
            '"targetVserver": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'targetVserver\', \'val\': \'asdf\'}, ' + \
            '"targetVserverExpr": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'targetVserverExpr\', \'val\': \'asdf\'}, ' + \
            '"targetLBVserver": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'targetLBVserver\', \'val\': \'asdf\'} } }'

        self.assertEqual(orig.__repr__(), expectedout)

if __name__ == '__main__':
    unittest.main()
