#!/usr/bin/python

import sys
sys.path.append('../')
import NetScaler.Service as Service
import unittest

class TestAttribute(unittest.TestCase):

    def test_01_BasicServer(self):
        servicename = 'svcname'
        servername = 'servername'
        servicetype = 'HTTP'
        port = 80

        expectedout = 'add service {} {} {} {} '.format( \
            servicename, servername, servicetype, port)

        orig = Service(servicename, servername, servicetype, port)
        self.assertEqual(str(orig), expectedout)

    def test_02_AdvancedServer(self):
        servicename = 'svcname'
        servername = 'servername'
        servicetype = 'HTTP'
        port = 80

        orig = Service(servicename, servername, servicetype, port, {
            "accessDown": "YES",
            "appflowLog": "DISABLED",
            "cacheable": "YES",
            "cacheType": "asdf",
            "cip": "asdf",
            "CKA": "YES",
            "clearTextPort": "80",
            "cltTimeout": 190,
            "CMP": "YES",
            "comment": "this is a comment",
            "CustomServerID": "adsf",
            "dnsProfileName": "asdf",
            "downStateFlush": "DISABLED",
            "hashId": "1",
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
            "processLocal": "ENABLED",
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

        expectedout = 'add service svcname servername HTTP 80 -comment "this is a comment" ' + \
            '-pathMonitorIndv YES -monThreshold 1 -accessDown YES -maxClient 1 -TCPB YES ' + \
            '-CustomServerID adsf -CKA YES -CMP YES -cacheable YES -pathMonitor YES -state DISABLED ' + \
            '-usip YES -cacheType asdf -hashId 1 -td 1 -httpProfileName asdf -cltTimeout 190 ' + \
            '-dnsProfileName asdf -clearTextPort 80 -healthMonitor NO -netProfile asdf -svrTimeout 361 ' + \
            '-sp OFF -monConnectionClose adsf -tcpProfileName asdf -appflowLog DISABLED ' + \
            '-downStateFlush DISABLED -cip asdf -maxReq 1 -useproxyport NO -rtspSessionidRemap ON ' + \
            '-maxBandwidth 1 -processLocal ENABLED '
        self.assertEqual(str(orig), expectedout)

    def test_03_Repr(self):
        servicename = 'svcname'
        servername = 'servername'
        servicetype = 'HTTP'
        port = 80

        orig = Service(servicename, servername, servicetype, port, {
            "accessDown": "YES",
            "appflowLog": "DISABLED",
            "cacheable": "YES",
            "cacheType": "asdf",
            "cip": "asdf",
            "CKA": "YES",
            "clearTextPort": "80",
            "cltTimeout": 190,
            "CMP": "YES",
            "comment": "this is a comment",
            "CustomServerID": "adsf",
            "dnsProfileName": "asdf",
            "downStateFlush": "DISABLED",
            "hashId": "1",
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
            "processLocal": "ENABLED",
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
        expected = '{  "objecttype": "service",  ' + \
            '"name": "svcname",  ' + \
            '"server": "servername",  ' + \
            '"servicetype": "HTTP",  ' + \
            '"port": 80,  ' + \
            '"Attributes": { ' + \
            '"comment": {\'default_value\': \'\', \'changed\': True, \'quoted\': True, \'key\': \'comment\', \'val\': \'this is a comment\'}, ' + \
            '"pathMonitorIndv": {\'default_value\': \'NO\', \'changed\': True, \'quoted\': False, \'key\': \'pathMonitorIndv\', \'val\': \'YES\'}, ' + \
            '"monThreshold": {\'default_value\': 0, \'changed\': True, \'quoted\': False, \'key\': \'monThreshold\', \'val\': 1}, ' + \
            '"accessDown": {\'default_value\': \'NO\', \'changed\': True, \'quoted\': False, \'key\': \'accessDown\', \'val\': \'YES\'}, ' + \
            '"maxClient": {\'default_value\': 0, \'changed\': True, \'quoted\': False, \'key\': \'maxClient\', \'val\': 1}, ' + \
            '"TCPB": {\'default_value\': \'NO\', \'changed\': True, \'quoted\': False, \'key\': \'TCPB\', \'val\': \'YES\'}, ' + \
            '"CustomServerID": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'CustomServerID\', \'val\': \'adsf\'}, ' + \
            '"CKA": {\'default_value\': \'NO\', \'changed\': True, \'quoted\': False, \'key\': \'CKA\', \'val\': \'YES\'}, ' + \
            '"CMP": {\'default_value\': \'NO\', \'changed\': True, \'quoted\': False, \'key\': \'CMP\', \'val\': \'YES\'}, ' + \
            '"cacheable": {\'default_value\': \'NO\', \'changed\': True, \'quoted\': False, \'key\': \'cacheable\', \'val\': \'YES\'}, ' + \
            '"pathMonitor": {\'default_value\': \'NO\', \'changed\': True, \'quoted\': False, \'key\': \'pathMonitor\', \'val\': \'YES\'}, ' + \
            '"state": {\'default_value\': \'ENABLED\', \'changed\': True, \'quoted\': False, \'key\': \'state\', \'val\': \'DISABLED\'}, ' + \
            '"usip": {\'default_value\': \'NO\', \'changed\': True, \'quoted\': False, \'key\': \'usip\', \'val\': \'YES\'}, ' + \
            '"cacheType": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'cacheType\', \'val\': \'asdf\'}, ' + \
            '"hashId": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'hashId\', \'val\': \'1\'}, ' + \
            '"td": {\'default_value\': 0, \'changed\': True, \'quoted\': False, \'key\': \'td\', \'val\': 1}, ' + \
            '"httpProfileName": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'httpProfileName\', \'val\': \'asdf\'}, ' + \
            '"cltTimeout": {\'default_value\': 180, \'changed\': True, \'quoted\': False, \'key\': \'cltTimeout\', \'val\': 190}, ' + \
            '"dnsProfileName": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'dnsProfileName\', \'val\': \'asdf\'}, ' + \
            '"clearTextPort": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'clearTextPort\', \'val\': \'80\'}, ' + \
            '"healthMonitor": {\'default_value\': \'YES\', \'changed\': True, \'quoted\': False, \'key\': \'healthMonitor\', \'val\': \'NO\'}, ' + \
            '"netProfile": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'netProfile\', \'val\': \'asdf\'}, ' + \
            '"svrTimeout": {\'default_value\': 360, \'changed\': True, \'quoted\': False, \'key\': \'svrTimeout\', \'val\': 361}, ' + \
            '"sp": {\'default_value\': \'ON\', \'changed\': True, \'quoted\': False, \'key\': \'sp\', \'val\': \'OFF\'}, ' + \
            '"monConnectionClose": {\'default_value\': \'NONE\', \'changed\': True, \'quoted\': False, \'key\': \'monConnectionClose\', \'val\': \'adsf\'}, ' + \
            '"tcpProfileName": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'tcpProfileName\', \'val\': \'asdf\'}, ' + \
            '"appflowLog": {\'default_value\': \'ENABLED\', \'changed\': True, \'quoted\': False, \'key\': \'appflowLog\', \'val\': \'DISABLED\'}, ' + \
            '"downStateFlush": {\'default_value\': \'ENABLED\', \'changed\': True, \'quoted\': False, \'key\': \'downStateFlush\', \'val\': \'DISABLED\'}, ' + \
            '"cip": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'cip\', \'val\': \'asdf\'}, ' + \
            '"maxReq": {\'default_value\': 0, \'changed\': True, \'quoted\': False, \'key\': \'maxReq\', \'val\': 1}, ' + \
            '"useproxyport": {\'default_value\': \'YES\', \'changed\': True, \'quoted\': False, \'key\': \'useproxyport\', \'val\': \'NO\'}, ' + \
            '"rtspSessionidRemap": {\'default_value\': \'OFF\', \'changed\': True, \'quoted\': False, \'key\': \'rtspSessionidRemap\', \'val\': \'ON\'}, ' + \
            '"maxBandwidth": {\'default_value\': 0, \'changed\': True, \'quoted\': False, \'key\': \'maxBandwidth\', \'val\': 1}, ' + \
            '"processLocal": {\'default_value\': \'DISABLED\', \'changed\': True, \'quoted\': False, \'key\': \'processLocal\', \'val\': \'ENABLED\'} } }'

        self.assertEqual(orig.__repr__(), expected)

if __name__ == '__main__':
    unittest.main()
