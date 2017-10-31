#!/usr/bin/python

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import NetScaler as ns
import unittest


class TestAttribute(unittest.TestCase):

    def test_99_Full(self):

        ns.conf.add_server('server1', '10.0.1.98')
        ns.conf.add_service('testsvc1', '10.0.1.99', 'HTTP', '80')
        ns.conf.add_service('testsvc2', 'server1', 'HTTP', '80')
        ns.conf.add_servicegroup('testsg1', 'HTTP')
        ns.conf.add_lb_vserver('test', 'HTTP', '10.0.0.1', '80')
        ns.conf.add_lb_vserver('test2', 'HTTP', '10.0.0.2', '80')
        ns.conf.add_cs_action('csaction1', {'targetLBVserver': 'test'})
        ns.conf.add_cs_policy('cspolicy1', {'domain': 'www.customer.com', 'rule': 'HTTP.REQ.URL.STARTS_WITH(\"/\")', 'action': 'csaction1'})
        ns.conf.add_cs_vserver('testcs', 'HTTP', '10.0.0.3', '80')
        expectedout = \
            'add server 10.0.1.99 10.0.1.99 \n' + \
            'add server server1 10.0.1.98 \n' + \
            'add service testsvc2 server1 HTTP 80 \n' + \
            'add service testsvc1 10.0.1.99 HTTP 80 \n' + \
            'add servicegroup testsg1 HTTP \n' + \
            'add lb vserver test HTTP 10.0.0.1 80 \n' + \
            'add lb vserver test2 HTTP 10.0.0.2 80 \n' + \
            'add cs action csaction1 -targetLBVserver test \n' + \
            'add cs policy cspolicy1 -domain www.customer.com -action "csaction1" -rule "HTTP.REQ.URL.STARTS_WITH(\\"/\\")" \n' + \
            'add cs vserver testcs HTTP 10.0.0.3 80 \n'

        self.assertEqual(str(ns.conf), expectedout)

if __name__ == '__main__':
    unittest.main()
