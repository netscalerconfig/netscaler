#!/usr/bin/python

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import NetScaler as ns
import unittest


class TestAttribute(unittest.TestCase):

    def test_01_lbsvcbind(self):
        config1 = ns.NewConfig()
        config1.add_server('servertest', '10.0.1.98')
        config1.add_service('svctest', 'servertest', 'HTTP', '80')
        config1.add_lb_vserver('lbtest', 'HTTP', '10.0.0.2', '80')
        config1.bind_lbvserver_service('lbtest', 'svctest')
        expectedout = \
            'add server servertest 10.0.1.98 \n' + \
            'add service svctest servertest HTTP 80 \n' + \
            'add lb vserver lbtest HTTP 10.0.0.2 80 \n' + \
            'bind lbvserver lbtest svctest \n'

        self.assertEqual(str(config1), expectedout)

    def test_02_lbsgbind(self):
        config1 = ns.NewConfig()
        config1.add_servicegroup('sgtest', 'HTTP')
        config1.add_lb_vserver('lbtest', 'HTTP', '10.0.0.2', '80')
        config1.bind_lbvserver_servicegroup('lbtest', 'sgtest')
        expectedout = \
            'add servicegroup sgtest HTTP \n' + \
            'add lb vserver lbtest HTTP 10.0.0.2 80 \n' + \
            'bind lbvserver lbtest sgtest \n'
        self.assertEqual(str(config1), expectedout)

    def test_03_sgsrvbind(self):
        config1 = ns.NewConfig()
        config1.add_servicegroup('sgtest', 'HTTP')
        config1.bind_servicegroup_server('sgtest', '10.0.1.1', 80)
        config1.bind_servicegroup_server('sgtest', '10.0.1.2', 80)
        config1.bind_servicegroup_server('sgtest', '10.0.1.3', 80)

        expectedout = \
            'add server 10.0.1.1 10.0.1.1 \n' + \
            'add server 10.0.1.2 10.0.1.2 \n' + \
            'add server 10.0.1.3 10.0.1.3 \n' + \
            'add servicegroup sgtest HTTP \n' + \
            'bind servicegroup sgtest 10.0.1.1 80 \n' + \
            'bind servicegroup sgtest 10.0.1.2 80 \n' + \
            'bind servicegroup sgtest 10.0.1.3 80 \n'
        self.assertEqual(str(config1), expectedout)

    def test_04_cslbbind(self):
        config1 = ns.NewConfig()
        config1.add_lb_vserver('lbtest', 'HTTP', '0.0.0.0', 0)
        config1.add_cs_vserver('cstest', 'HTTP', '10.0.1.10', 80)
        config1.bind_cs_lbvserver('cstest', 'lbtest')
        expectedout = \
            'add lb vserver lbtest HTTP 0.0.0.0 0 \n' + \
            'add cs vserver cstest HTTP 10.0.1.10 80 \n' + \
            'bind csvserver cstest -lbvserver lbtest \n'
        self.assertEqual(str(config1), expectedout)

    def test_05_cscspolbind(self):
        config1 = ns.NewConfig()
        config1.add_lb_vserver('lbtest', 'HTTP', '0.0.0.0', 0)
        config1.add_cs_action('act1', {'targetLBVserver': 'lbtest'})
        config1.add_cs_policy('pol1', {'action': 'act1', 'rule': 'HTTP.REQ.URL.STARTSWITH("/")'})
        config1.add_cs_vserver('cstest', 'HTTP', '10.0.1.10', 80)
        config1.bind_cs_cspolicy('cstest', 'pol1', {'priority': 100})
        expectedout = \
            'add lb vserver lbtest HTTP 0.0.0.0 0 \n' + \
            'add cs action act1 -targetLBVserver lbtest \n' + \
            'add cs policy pol1 -action "act1" -rule "HTTP.REQ.URL.STARTSWITH(\\"/\\")" \n' + \
            'add cs vserver cstest HTTP 10.0.1.10 80 \n' + \
            'bind csvserver cstest -policyName pol1 -priority 100 \n'
        self.assertEqual(str(config1), expectedout)


if __name__ == '__main__':
    unittest.main()
