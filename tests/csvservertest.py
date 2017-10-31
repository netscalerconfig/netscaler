#!/usr/bin/python

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import NetScaler.CSvServer as CSvServer
import unittest

class TestAttribute(unittest.TestCase):

    def test_01_Basic(self):
        lbname = 'csname'
        servicetype = 'HTTP'
        ipaddress = '10.10.10.10'
        port = 80
        expectedout = 'add cs vserver {} {} {} {} '.format(lbname, servicetype, ipaddress, port)
        orig = CSvServer(lbname, servicetype, ipaddress, port)
        self.assertEqual(str(orig), expectedout)

    def test_02_Advanced(self):
        lbname = 'csname'
        servicetype = 'HTTP'
        ipaddress = '10.10.10.10'
        port = 80
        expectedout = 'add cs vserver {} {} {} {} '.format(lbname, servicetype, ipaddress, port)
        orig = CSvServer(lbname, servicetype, ipaddress, port, {
                "range": "asdf",
                "IPPattern": "asdf",
                "IPMask": "asdf",
                "targetType": "asdf",
                "appflowLog": "ENABLED",
                "Authentication": "ON",
                "AuthenticationHost": "asdf",
                "authn401": "ON",
                "authnProfile": "asdf",
                "authnVs": "asdf",
                "backupVServer": "asdf",
                "cacheable": "YES",
                "caseSensitive": "YES",
                "cltTimeout": 181,
                "comment": "This is a comment",
                "dbProfileName": "asdf",
                "dbsLb": "ENABLED",
                "disablePrimaryOnDown": "ENABLED",
                "dnsProfileName": "asdf",
                "dnsRecordType": "asdf",
                "downStateFlush": "DISABLED",
                "httpProfileName": "asdf",
                "icmpVsrResponse": "ACTIVE",
                "insertVserverIPPort": "ON",
                "l2Conn": "ON",
                "Listenpolicy": "asdf",
                "Listenpriority": "asdf",
                "mssqlServerVersion": "asdf",
                "mysqlCharacterSet": "asdf",
                "mysqlProtocolVersion": "asdf",
                "mysqlServerCapabilities": "asdf",
                "mysqlServerVersion": "asdf",
                "netProfile": "asdf",
                "oracleServerVersion": "asdf",
                "persistenceId": "asdf",
                "presedence": "URL",
                "push": "ENABLED",
                "pushLabel": "asdf",
                "pushMultiClients": "YES",
                "pushVserver": "asdf",
                "redirectPortRewrite": "ENABLED",
                "redirectURL": "asdf",
                "RHIstate": "ACTIVE",
                "rtspNat": "ON",
                "soBackupAction": "asdf",
                "soMethod": "OTHER",
                "soPersistence": "ENABLED",
                "soPersistenceTimeOut": 1,
                "soThreshold": 1,
                "state" : "DISABLED",
                "tcpProfileName": "asdf",
                "td": 1
            })

        expectedout = 'add cs vserver {} {} {} {} '.format(lbname, servicetype, ipaddress, port) + \
            '-comment "This is a comment" -persistenceId asdf -oracleServerVersion asdf -backupVServer asdf ' + \
            '-soBackupAction asdf -soMethod OTHER -dnsRecordType asdf -soPersistenceTimeOut 1 -caseSensitive YES ' + \
            '-Authentication ON -presedence URL -range asdf -insertVserverIPPort ON -cacheable YES ' + \
            '-mysqlServerCapabilities asdf -rtspNat ON -authn401 ON -state DISABLED -mssqlServerVersion asdf ' + \
            '-RHIstate ACTIVE -redirectURL asdf -pushMultiClients YES -td 1 -httpProfileName asdf -cltTimeout 181 ' + \
            '-dnsProfileName asdf -netProfile asdf -IPPattern asdf -Listenpriority asdf -pushVserver asdf ' + \
            '-dbProfileName asdf -mysqlServerVersion asdf -icmpVsrResponse ACTIVE -pushLabel asdf ' + \
            '-redirectPortRewrite ENABLED -AuthenticationHost asdf -targetType asdf -soThreshold 1 -authnVs asdf ' + \
            '-soPersistence ENABLED -appflowLog ENABLED -tcpProfileName asdf -mysqlCharacterSet asdf ' + \
            '-mysqlProtocolVersion asdf -disablePrimaryOnDown ENABLED -dbsLb ENABLED -Listenpolicy asdf ' + \
            '-l2Conn ON -push ENABLED -IPMask asdf -authnProfile asdf -downStateFlush DISABLED '
        self.assertEqual(str(orig), expectedout)

    def test_03_Repr(self):
        lbname = 'csname'
        servicetype = 'HTTP'
        ipaddress = '10.10.10.10'
        port = 80
        expectedout = 'add cs vserver {} {} {} {} '.format(lbname, servicetype, ipaddress, port)
        orig = CSvServer(lbname, servicetype, ipaddress, port, {
                "range": "asdf",
                "IPPattern": "asdf",
                "IPMask": "asdf",
                "targetType": "asdf",
                "appflowLog": "ENABLED",
                "Authentication": "ON",
                "AuthenticationHost": "asdf",
                "authn401": "ON",
                "authnProfile": "asdf",
                "authnVs": "asdf",
                "backupVServer": "asdf",
                "cacheable": "YES",
                "caseSensitive": "YES",
                "cltTimeout": 181,
                "comment": "This is a comment",
                "dbProfileName": "asdf",
                "dbsLb": "ENABLED",
                "disablePrimaryOnDown": "ENABLED",
                "dnsProfileName": "asdf",
                "dnsRecordType": "asdf",
                "downStateFlush": "DISABLED",
                "httpProfileName": "asdf",
                "icmpVsrResponse": "ACTIVE",
                "insertVserverIPPort": "ON",
                "l2Conn": "ON",
                "Listenpolicy": "asdf",
                "Listenpriority": "asdf",
                "mssqlServerVersion": "asdf",
                "mysqlCharacterSet": "asdf",
                "mysqlProtocolVersion": "asdf",
                "mysqlServerCapabilities": "asdf",
                "mysqlServerVersion": "asdf",
                "netProfile": "asdf",
                "oracleServerVersion": "asdf",
                "persistenceId": "asdf",
                "presedence": "URL",
                "push": "ENABLED",
                "pushLabel": "asdf",
                "pushMultiClients": "YES",
                "pushVserver": "asdf",
                "redirectPortRewrite": "ENABLED",
                "redirectURL": "asdf",
                "RHIstate": "ACTIVE",
                "rtspNat": "ON",
                "soBackupAction": "asdf",
                "soMethod": "OTHER",
                "soPersistence": "ENABLED",
                "soPersistenceTimeOut": 1,
                "soThreshold": 1,
                "state" : "DISABLED",
                "tcpProfileName": "asdf",
                "td": 1
            })

        expected = '{  "objecttype": "csvserver",  ' + \
            '"name": "csname",  ' + \
            '"servicetype": "HTTP",  ' + \
            '"ipaddress": "10.10.10.10",  ' + \
            '"port": 80,  ' + \
            '"Attributes": { ' + \
            '"comment": {\'default_value\': \'\', \'changed\': True, \'quoted\': True, \'key\': \'comment\', \'val\': \'This is a comment\'}, ' + \
            '"persistenceId": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'persistenceId\', \'val\': \'asdf\'}, ' + \
            '"oracleServerVersion": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'oracleServerVersion\', \'val\': \'asdf\'}, ' + \
            '"backupVServer": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'backupVServer\', \'val\': \'asdf\'}, ' + \
            '"soBackupAction": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'soBackupAction\', \'val\': \'asdf\'}, ' + \
            '"soMethod": {\'default_value\': \'NONE\', \'changed\': True, \'quoted\': False, \'key\': \'soMethod\', \'val\': \'OTHER\'}, ' + \
            '"dnsRecordType": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'dnsRecordType\', \'val\': \'asdf\'}, ' + \
            '"soPersistenceTimeOut": {\'default_value\': 0, \'changed\': True, \'quoted\': False, \'key\': \'soPersistenceTimeOut\', \'val\': 1}, ' + \
            '"caseSensitive": {\'default_value\': \'ON\', \'changed\': True, \'quoted\': False, \'key\': \'caseSensitive\', \'val\': \'YES\'}, ' + \
            '"Authentication": {\'default_value\': \'OFF\', \'changed\': True, \'quoted\': False, \'key\': \'Authentication\', \'val\': \'ON\'}, ' + \
            '"presedence": {\'default_value\': \'RULE\', \'changed\': True, \'quoted\': False, \'key\': \'presedence\', \'val\': \'URL\'}, ' + \
            '"range": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'range\', \'val\': \'asdf\'}, ' + \
            '"insertVserverIPPort": {\'default_value\': \'OFF\', \'changed\': True, \'quoted\': False, \'key\': \'insertVserverIPPort\', \'val\': \'ON\'}, ' + \
            '"cacheable": {\'default_value\': \'NO\', \'changed\': True, \'quoted\': False, \'key\': \'cacheable\', \'val\': \'YES\'}, ' + \
            '"mysqlServerCapabilities": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'mysqlServerCapabilities\', \'val\': \'asdf\'}, ' + \
            '"rtspNat": {\'default_value\': \'OFF\', \'changed\': True, \'quoted\': False, \'key\': \'rtspNat\', \'val\': \'ON\'}, ' + \
            '"authn401": {\'default_value\': \'OFF\', \'changed\': True, \'quoted\': False, \'key\': \'authn401\', \'val\': \'ON\'}, ' + \
            '"state": {\'default_value\': \'ENABLED\', \'changed\': True, \'quoted\': False, \'key\': \'state\', \'val\': \'DISABLED\'}, ' + \
            '"mssqlServerVersion": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'mssqlServerVersion\', \'val\': \'asdf\'}, ' + \
            '"RHIstate": {\'default_value\': \'PASSIVE\', \'changed\': True, \'quoted\': False, \'key\': \'RHIstate\', \'val\': \'ACTIVE\'}, ' + \
            '"redirectURL": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'redirectURL\', \'val\': \'asdf\'}, ' + \
            '"pushMultiClients": {\'default_value\': \'NO\', \'changed\': True, \'quoted\': False, \'key\': \'pushMultiClients\', \'val\': \'YES\'}, ' + \
            '"td": {\'default_value\': 0, \'changed\': True, \'quoted\': False, \'key\': \'td\', \'val\': 1}, ' + \
            '"httpProfileName": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'httpProfileName\', \'val\': \'asdf\'}, ' + \
            '"cltTimeout": {\'default_value\': 180, \'changed\': True, \'quoted\': False, \'key\': \'cltTimeout\', \'val\': 181}, ' + \
            '"dnsProfileName": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'dnsProfileName\', \'val\': \'asdf\'}, ' + \
            '"netProfile": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'netProfile\', \'val\': \'asdf\'}, ' + \
            '"IPPattern": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'IPPattern\', \'val\': \'asdf\'}, ' + \
            '"Listenpriority": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'Listenpriority\', \'val\': \'asdf\'}, ' + \
            '"pushVserver": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'pushVserver\', \'val\': \'asdf\'}, ' + \
            '"dbProfileName": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'dbProfileName\', \'val\': \'asdf\'}, ' + \
            '"mysqlServerVersion": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'mysqlServerVersion\', \'val\': \'asdf\'}, ' + \
            '"icmpVsrResponse": {\'default_value\': \'PASSIVE\', \'changed\': True, \'quoted\': False, \'key\': \'icmpVsrResponse\', \'val\': \'ACTIVE\'}, ' + \
            '"pushLabel": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'pushLabel\', \'val\': \'asdf\'}, ' + \
            '"redirectPortRewrite": {\'default_value\': \'DISABLED\', \'changed\': True, \'quoted\': False, \'key\': \'redirectPortRewrite\', \'val\': \'ENABLED\'}, ' + \
            '"AuthenticationHost": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'AuthenticationHost\', \'val\': \'asdf\'}, ' + \
            '"targetType": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'targetType\', \'val\': \'asdf\'}, ' + \
            '"soThreshold": {\'default_value\': 0, \'changed\': True, \'quoted\': False, \'key\': \'soThreshold\', \'val\': 1}, ' + \
            '"authnVs": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'authnVs\', \'val\': \'asdf\'}, ' + \
            '"soPersistence": {\'default_value\': \'DISABLED\', \'changed\': True, \'quoted\': False, \'key\': \'soPersistence\', \'val\': \'ENABLED\'}, ' + \
            '"appflowLog": {\'default_value\': \'DISABLED\', \'changed\': True, \'quoted\': False, \'key\': \'appflowLog\', \'val\': \'ENABLED\'}, ' + \
            '"tcpProfileName": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'tcpProfileName\', \'val\': \'asdf\'}, ' + \
            '"mysqlCharacterSet": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'mysqlCharacterSet\', \'val\': \'asdf\'}, ' + \
            '"mysqlProtocolVersion": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'mysqlProtocolVersion\', \'val\': \'asdf\'}, ' + \
            '"disablePrimaryOnDown": {\'default_value\': \'DISABLED\', \'changed\': True, \'quoted\': False, \'key\': \'disablePrimaryOnDown\', \'val\': \'ENABLED\'}, ' + \
            '"dbsLb": {\'default_value\': \'DISABLED\', \'changed\': True, \'quoted\': False, \'key\': \'dbsLb\', \'val\': \'ENABLED\'}, ' + \
            '"Listenpolicy": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'Listenpolicy\', \'val\': \'asdf\'}, ' + \
            '"l2Conn": {\'default_value\': \'OFF\', \'changed\': True, \'quoted\': False, \'key\': \'l2Conn\', \'val\': \'ON\'}, ' + \
            '"push": {\'default_value\': \'DISABLED\', \'changed\': True, \'quoted\': False, \'key\': \'push\', \'val\': \'ENABLED\'}, ' + \
            '"IPMask": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'IPMask\', \'val\': \'asdf\'}, ' + \
            '"authnProfile": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'authnProfile\', \'val\': \'asdf\'}, ' + \
            '"downStateFlush": {\'default_value\': \'ENABLED\', \'changed\': True, \'quoted\': False, \'key\': \'downStateFlush\', \'val\': \'DISABLED\'} } }'

        self.assertEqual(orig.__repr__(), expected)

if __name__ == '__main__':
    unittest.main()
