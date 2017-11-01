#!/usr/bin/python

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import NetScaler as ns
import unittest


class TestAttribute(unittest.TestCase):

    def test_01_vpnvserver(self):
        config1 = ns.NewConfig()
        config1.add_vpn_vserver('vpntest', 'SSL', '10.0.1.98', 443)
        expectedout = \
            'add vpn vserver vpntest SSL 10.0.1.98 443 \n' 

        self.assertEqual(str(config1), expectedout)


if __name__ == '__main__':
    unittest.main()
