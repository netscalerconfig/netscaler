#!/usr/bin/python

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import NetScaler.ServiceGroup as ServiceGroup
import unittest

class TestAttribute(unittest.TestCase):

    def test_01_Basic(self):
        servicename = 'svcname'
        servicetype = 'HTTP'
        expectedout = 'add servicegroup {} {} '.format(servicename, servicetype)
        orig = ServiceGroup(servicename, servicetype)
        self.assertEqual(str(orig), expectedout)

    def test_02_Advanced(self):
        servicename = 'svcname'
        servicetype = 'HTTP'
        orig = ServiceGroup(servicename, servicetype, {
            "appflowLog": "DISABLED",
            "autoScale": "asdf",
            "memberPort": "1",
            "cacheable": "YES",
            "cacheType": "asdf",
            "cip": "asdf",
            "CKA": "YES",
            "cltTimeout": 190,
            "CMP": "YES",
            "comment": "this is a comment",
            "downStateFlush": "DISABLED",
            "healthMonitor": "NO",
            "httpProfileName": "asdf",
            "maxBandwidth": 1,
            "maxClient": 1,
            "maxReq": 1,
            "monConnectionClose": "adsf",
            "monThreshold": 1,
            "netProfile": "asdf",
            "pathMonitor": "YES",
            "pathMonitorIndv": "YES",
            "rtspSessionidRemap": "ON",
            "sp": "OFF",
            "state": "DISABLED",
            "svrTimeout": 361,
            "TCPB": "YES",
            "tcpProfileName": "asdf",
            "td": 1,
            "useproxyport": "NO",
            "usip": "YES"
            })

        expectedout = 'add servicegroup svcname HTTP -comment "this is a comment" ' + \
            '-pathMonitorIndv YES -monThreshold 1 -CKA YES -maxClient 1 -TCPB YES -CMP YES ' + \
            '-cacheable YES -pathMonitor YES -state DISABLED -usip YES -cacheType asdf ' + \
            '-svrTimeout 361 -httpProfileName asdf -cltTimeout 190 -autoScale asdf ' + \
            '-healthMonitor NO -netProfile asdf -td 1 -sp OFF -monConnectionClose adsf ' + \
            '-tcpProfileName asdf -appflowLog DISABLED -downStateFlush DISABLED -cip asdf ' + \
            '-maxReq 1 -memberPort 1 -useproxyport NO -rtspSessionidRemap ON -maxBandwidth 1 '
        self.assertEqual(str(orig), expectedout)

    def test_03_Repr(self):
        servicename = 'svcname'
        servicetype = 'HTTP'

        orig = ServiceGroup(servicename, servicetype, {
            "appflowLog": "DISABLED",
            "autoScale": "asdf",
            "memberPort": "1",
            "cacheable": "YES",
            "cacheType": "asdf",
            "cip": "asdf",
            "CKA": "YES",
            "cltTimeout": 190,
            "CMP": "YES",
            "comment": "this is a comment",
            "downStateFlush": "DISABLED",
            "healthMonitor": "NO",
            "httpProfileName": "asdf",
            "maxBandwidth": 1,
            "maxClient": 1,
            "maxReq": 1,
            "monConnectionClose": "adsf",
            "monThreshold": 1,
            "netProfile": "asdf",
            "pathMonitor": "YES",
            "pathMonitorIndv": "YES",
            "rtspSessionidRemap": "ON",
            "sp": "OFF",
            "state": "DISABLED",
            "svrTimeout": 361,
            "TCPB": "YES",
            "tcpProfileName": "asdf",
            "td": 1,
            "useproxyport": "NO",
            "usip": "YES"
            })

        expected = '{  "objecttype": "servicegroup",  "name": "svcname",  "servicetype": "HTTP",  ' + \
            '"Attributes": { ' + \
            '"comment": {\'default_value\': \'\', \'changed\': True, \'quoted\': True, \'key\': \'comment\', \'val\': \'this is a comment\'}, ' + \
            '"pathMonitorIndv": {\'default_value\': \'NO\', \'changed\': True, \'quoted\': False, \'key\': \'pathMonitorIndv\', \'val\': \'YES\'}, ' + \
            '"monThreshold": {\'default_value\': 0, \'changed\': True, \'quoted\': False, \'key\': \'monThreshold\', \'val\': 1}, ' + \
            '"CKA": {\'default_value\': \'NO\', \'changed\': True, \'quoted\': False, \'key\': \'CKA\', \'val\': \'YES\'}, ' + \
            '"maxClient": {\'default_value\': 0, \'changed\': True, \'quoted\': False, \'key\': \'maxClient\', \'val\': 1}, ' + \
            '"TCPB": {\'default_value\': \'NO\', \'changed\': True, \'quoted\': False, \'key\': \'TCPB\', \'val\': \'YES\'}, ' + \
            '"CMP": {\'default_value\': \'NO\', \'changed\': True, \'quoted\': False, \'key\': \'CMP\', \'val\': \'YES\'}, ' + \
            '"cacheable": {\'default_value\': \'NO\', \'changed\': True, \'quoted\': False, \'key\': \'cacheable\', \'val\': \'YES\'}, ' + \
            '"pathMonitor": {\'default_value\': \'NO\', \'changed\': True, \'quoted\': False, \'key\': \'pathMonitor\', \'val\': \'YES\'}, ' + \
            '"state": {\'default_value\': \'ENABLED\', \'changed\': True, \'quoted\': False, \'key\': \'state\', \'val\': \'DISABLED\'}, ' + \
            '"usip": {\'default_value\': \'NO\', \'changed\': True, \'quoted\': False, \'key\': \'usip\', \'val\': \'YES\'}, ' + \
            '"cacheType": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'cacheType\', \'val\': \'asdf\'}, ' + \
            '"svrTimeout": {\'default_value\': 360, \'changed\': True, \'quoted\': False, \'key\': \'svrTimeout\', \'val\': 361}, ' + \
            '"httpProfileName": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'httpProfileName\', \'val\': \'asdf\'}, ' + \
            '"cltTimeout": {\'default_value\': 180, \'changed\': True, \'quoted\': False, \'key\': \'cltTimeout\', \'val\': 190}, ' + \
            '"autoScale": {\'default_value\': \'DISABLED\', \'changed\': True, \'quoted\': False, \'key\': \'autoScale\', \'val\': \'asdf\'}, ' + \
            '"healthMonitor": {\'default_value\': \'YES\', \'changed\': True, \'quoted\': False, \'key\': \'healthMonitor\', \'val\': \'NO\'}, ' + \
            '"netProfile": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'netProfile\', \'val\': \'asdf\'}, ' + \
            '"td": {\'default_value\': 0, \'changed\': True, \'quoted\': False, \'key\': \'td\', \'val\': 1}, ' + \
            '"sp": {\'default_value\': \'ON\', \'changed\': True, \'quoted\': False, \'key\': \'sp\', \'val\': \'OFF\'}, ' + \
            '"monConnectionClose": {\'default_value\': \'NONE\', \'changed\': True, \'quoted\': False, \'key\': \'monConnectionClose\', \'val\': \'adsf\'}, ' + \
            '"tcpProfileName": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'tcpProfileName\', \'val\': \'asdf\'}, ' + \
            '"appflowLog": {\'default_value\': \'ENABLED\', \'changed\': True, \'quoted\': False, \'key\': \'appflowLog\', \'val\': \'DISABLED\'}, ' + \
            '"downStateFlush": {\'default_value\': \'ENABLED\', \'changed\': True, \'quoted\': False, \'key\': \'downStateFlush\', \'val\': \'DISABLED\'}, ' + \
            '"cip": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'cip\', \'val\': \'asdf\'}, ' + \
            '"maxReq": {\'default_value\': 0, \'changed\': True, \'quoted\': False, \'key\': \'maxReq\', \'val\': 1}, ' + \
            '"memberPort": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'memberPort\', \'val\': \'1\'}, ' + \
            '"useproxyport": {\'default_value\': \'YES\', \'changed\': True, \'quoted\': False, \'key\': \'useproxyport\', \'val\': \'NO\'}, ' + \
            '"rtspSessionidRemap": {\'default_value\': \'OFF\', \'changed\': True, \'quoted\': False, \'key\': \'rtspSessionidRemap\', \'val\': \'ON\'}, ' + \
            '"maxBandwidth": {\'default_value\': 0, \'changed\': True, \'quoted\': False, \'key\': \'maxBandwidth\', \'val\': 1} ' + \
            '} }'

        self.assertEqual(orig.__repr__(), expected)

if __name__ == '__main__':
    unittest.main()
