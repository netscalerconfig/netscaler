#!/usr/bin/python

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import NetScaler as ns
import unittest


class TestAttribute(unittest.TestCase):

    def test_01_Basic(self):

        ns.conf.add_server('server1', '10.0.1.98')
        ns.conf.add_service('testsvc1', '10.0.1.99', 'HTTP', '80')
        ns.conf.add_service('testsvc2', 'server1', 'HTTP', '80')
        ns.conf.add_lb_vserver('test', 'HTTP', '10.0.0.1', '80')
        ns.conf.add_lb_vserver('test2', 'HTTP', '10.0.0.2', '80')
        expectedout = \
            'add server 10.0.1.99 10.0.1.99 \n' + \
            'add server server1 10.0.1.98 \n' + \
            'add service testsvc2 server1 HTTP 80 \n' + \
            'add service testsvc1 10.0.1.99 HTTP 80 \n' + \
            'add lb vserver test HTTP 10.0.0.1 80 \n' + \
            'add lb vserver test2 HTTP 10.0.0.2 80 \n'

        self.assertEqual(str(ns.conf), expectedout)

if __name__ == '__main__':
    unittest.main()
