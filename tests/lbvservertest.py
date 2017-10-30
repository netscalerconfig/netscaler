#!/usr/bin/python

import sys
sys.path.append('../')
import NetScaler.LBvServer as LBvServer
import unittest

class TestAttribute(unittest.TestCase):

    def test_01_Basic(self):
        lbname = 'svcname'
        servicetype = 'HTTP'
        ipaddress = '10.10.10.10'
        port = 80
        expectedout = 'add lb vserver {} {} {} {} '.format(lbname, servicetype, ipaddress, port)
        orig = LBvServer(lbname, servicetype, ipaddress, port)
        self.assertEqual(str(orig), expectedout)

    def test_02_Advanced(self):
        lbname = 'svcname'
        servicetype = 'HTTP'
        ipaddress = '10.10.10.10'
        port = 80
        expectedout = 'add lb vserver {} {} {} {} '.format(lbname, servicetype, ipaddress, port)
        orig = LBvServer(lbname, servicetype, ipaddress, port, {
                "range": "adsf",
                "IPPattern": "asdf",
                "IPMask": "adsf",
                "appflowLog": "ENABLED",
                "Authentication": "ON",
                "AuthenticationHost": "asdf",
                "authn401": "ON",
                "authnProfile": "asdf",
                "authnVs": "asdf",
                "backupLB": "LEASTCONNECTION",
                "backupPersistence": 10,
                "backupVServer": "ASDF",
                "bypassAAAA": "YES",
                "cacheable": "YES",
                "cltTimeout": 181,
                "comment": "This is a comment",
                "connfailover": "ENABLED",
                "cookieName": "adsf",
                "dbProfileName": "asdf",
                "dbsLb": "ENABLED",
                "disablePrimaryOnDown": "ENABLED",
                "dns64": "ENABLED",
                "dnsProfileName": "asdf",
                "downStateFlush": "DISABLED",
                "healthThreshold": 1,
                "httpProfileName": "asdf",
                "httpsRedirectUrl": "asdf",
                "icmpVsrResponse": "ACTIVE",
                "insertVserverIPPort": "ON",
                "l2Conn": "ON",
                "lbMethod": "ROUNDROBIN",
                "lbprofilename": "asdf",
                "Listenpolicy": "asdf",
                "Listenpriority": "asdf",
                "m": "OTHER",
                "macmodeRetainvlan": "ENABLED",
                "maxAutoscaleMembers": 1,
                "minAutoscaleMembers": 1,
                "mssqlServerVersion": "asdf",
                "mysqlCharacterSet": "asdf",
                "mysqlProtocolVersion": "asdf",
                "mysqlServerCapabilities": "asdf",
                "mysqlServerVersion": "asdf",
                "netProfile": "asdf",
                "newServiceRequest": 1,
                "newServiceRequestIncrementInterval": 1,
                "oracleServerVersion": "asdf",
                "persistAVPno": 2,
                "persistenceBackup": "SOURCEIP",
                "persistenceType": "COOKIEINSERT",
                "persistMask": "asdf",
                "processLocal": "ENABLED",
                "push": "ENABLED",
                "pushLabel": "asdf",
                "pushMultiClients": "YES",
                "pushVserver": "asdf",
                "RecursionAvailable": "asdf",
                "redirectFromPort": "asdf",
                "redirectPortRewrite": "ENABLED",
                "redirectURL": "asdf",
                "resRule": "asdf",
                "retainConnectionsOnCluster": "YES",
                "RHIstate": "ACTIVE",
                "rtspNat": "ON",
                "rule": "asdf",
                "sessionless": "ENABLED",
                "skippersistency": "Other",
                "soBackupAction": "asdf",
                "soMethod": "OTHER",
                "soPersistence": "ENABLED",
                "soPersistenceTimeOut": 1,
                "soThreshold": 1,
                "tcpProfileName": "asdf",
                "timeout": 1,
                "tosId": "asdf",
                "trofsPersistence": "DISABLED",
                "v6persistmasklen": "127"
            })

        expectedout = 'add lb vserver {} {} {} {} '.format(lbname, servicetype, ipaddress, port) + \
        '-comment "This is a comment" -mysqlServerVersion asdf ' + \
        '-newServiceRequestIncrementInterval 1 -icmpVsrResponse ACTIVE -persistenceBackup SOURCEIP ' + \
        '-mysqlCharacterSet asdf -processLocal ENABLED -soBackupAction asdf -cookieName adsf -authn401 ON ' + \
        '-soPersistenceTimeOut 1 -Authentication ON -healthThreshold 1 -soMethod OTHER -oracleServerVersion asdf ' + \
        '-tosId asdf -persistAVPno 2 -insertVserverIPPort ON -connfailover ENABLED -minAutoscaleMembers 1 ' + \
        '-cacheable YES -authnVs asdf -disablePrimaryOnDown ENABLED -redirectPortRewrite ENABLED -rtspNat ON ' + \
        '-backupLB LEASTCONNECTION -mssqlServerVersion asdf -lbMethod ROUNDROBIN -macmodeRetainvlan ENABLED ' + \
        '-RHIstate ACTIVE -redirectURL asdf -lbprofilename asdf -RecursionAvailable asdf -httpProfileName asdf ' + \
        '-cltTimeout 181 -dnsProfileName asdf -IPMask adsf -persistenceType COOKIEINSERT -maxAutoscaleMembers 1 ' + \
        '-l2Conn ON -IPPattern asdf -dns64 ENABLED -skippersistency Other -bypassAAAA YES -Listenpriority asdf ' + \
        '-pushVserver asdf -dbProfileName asdf -persistMask asdf -netProfile asdf -pushMultiClients YES ' + \
        '-pushLabel asdf -sessionless ENABLED -trofsPersistence DISABLED -resRule asdf -AuthenticationHost asdf ' + \
        '-redirectFromPort asdf -soThreshold 1 -mysqlServerCapabilities asdf -soPersistence ENABLED ' + \
        '-appflowLog ENABLED -retainConnectionsOnCluster YES -rule asdf -httpsRedirectUrl asdf ' + \
        '-tcpProfileName asdf -m OTHER -mysqlProtocolVersion asdf -backupPersistence 10 -range adsf ' + \
        '-backupVServer ASDF -dbsLb ENABLED -Listenpolicy asdf -timeout 1 -newServiceRequest 1 -push ENABLED ' + \
        '-v6persistmasklen 127 -authnProfile asdf -downStateFlush DISABLED '
        self.assertEqual(str(orig), expectedout)

    def test_03_Repr(self):
        lbname = 'svcname'
        servicetype = 'HTTP'
        ipaddress = '10.10.10.10'
        port = 80
        expectedout = 'add lb vserver {} {} {} {} '.format(lbname, servicetype, ipaddress, port)
        orig = LBvServer(lbname, servicetype, ipaddress, port, {
                "range": "adsf",
                "IPPattern": "asdf",
                "IPMask": "adsf",
                "appflowLog": "ENABLED",
                "Authentication": "ON",
                "AuthenticationHost": "asdf",
                "authn401": "ON",
                "authnProfile": "asdf",
                "authnVs": "asdf",
                "backupLB": "LEASTCONNECTION",
                "backupPersistence": 10,
                "backupVServer": "ASDF",
                "bypassAAAA": "YES",
                "cacheable": "YES",
                "cltTimeout": 181,
                "comment": "This is a comment",
                "connfailover": "ENABLED",
                "cookieName": "adsf",
                "dbProfileName": "asdf",
                "dbsLb": "ENABLED",
                "disablePrimaryOnDown": "ENABLED",
                "dns64": "ENABLED",
                "dnsProfileName": "asdf",
                "downStateFlush": "DISABLED",
                "healthThreshold": 1,
                "httpProfileName": "asdf",
                "httpsRedirectUrl": "asdf",
                "icmpVsrResponse": "ACTIVE",
                "insertVserverIPPort": "ON",
                "l2Conn": "ON",
                "lbMethod": "ROUNDROBIN",
                "lbprofilename": "asdf",
                "Listenpolicy": "asdf",
                "Listenpriority": "asdf",
                "m": "OTHER",
                "macmodeRetainvlan": "ENABLED",
                "maxAutoscaleMembers": 1,
                "minAutoscaleMembers": 1,
                "mssqlServerVersion": "asdf",
                "mysqlCharacterSet": "asdf",
                "mysqlProtocolVersion": "asdf",
                "mysqlServerCapabilities": "asdf",
                "mysqlServerVersion": "asdf",
                "netProfile": "asdf",
                "newServiceRequest": 1,
                "newServiceRequestIncrementInterval": 1,
                "oracleServerVersion": "asdf",
                "persistAVPno": 2,
                "persistenceBackup": "SOURCEIP",
                "persistenceType": "COOKIEINSERT",
                "persistMask": "asdf",
                "processLocal": "ENABLED",
                "push": "ENABLED",
                "pushLabel": "asdf",
                "pushMultiClients": "YES",
                "pushVserver": "asdf",
                "RecursionAvailable": "asdf",
                "redirectFromPort": "asdf",
                "redirectPortRewrite": "ENABLED",
                "redirectURL": "asdf",
                "resRule": "asdf",
                "retainConnectionsOnCluster": "YES",
                "RHIstate": "ACTIVE",
                "rtspNat": "ON",
                "rule": "asdf",
                "sessionless": "ENABLED",
                "skippersistency": "Other",
                "soBackupAction": "asdf",
                "soMethod": "OTHER",
                "soPersistence": "ENABLED",
                "soPersistenceTimeOut": 1,
                "soThreshold": 1,
                "tcpProfileName": "asdf",
                "timeout": 1,
                "tosId": "asdf",
                "trofsPersistence": "DISABLED",
                "v6persistmasklen": "127"
            })

        expected = '{  "objecttype": "lbvserver",  ' + \
            '"name": "svcname",  ' + \
            '"servicetype": "HTTP",  ' + \
            '"ipaddress": "10.10.10.10",  ' + \
            '"port": 80,  ' + \
            '"Attributes": { ' + \
            '"comment": {\'default_value\': \'\', \'changed\': True, \'quoted\': True, \'key\': \'comment\', \'val\': \'This is a comment\'}, ' + \
            '"mysqlServerVersion": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'mysqlServerVersion\', \'val\': \'asdf\'}, ' + \
            '"newServiceRequestIncrementInterval": {\'default_value\': 0, \'changed\': True, \'quoted\': False, \'key\': \'newServiceRequestIncrementInterval\', \'val\': 1}, ' + \
            '"icmpVsrResponse": {\'default_value\': \'PASSIVE\', \'changed\': True, \'quoted\': False, \'key\': \'icmpVsrResponse\', \'val\': \'ACTIVE\'}, ' + \
            '"persistenceBackup": {\'default_value\': \'NONE\', \'changed\': True, \'quoted\': False, \'key\': \'persistenceBackup\', \'val\': \'SOURCEIP\'}, ' + \
            '"mysqlCharacterSet": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'mysqlCharacterSet\', \'val\': \'asdf\'}, ' + \
            '"processLocal": {\'default_value\': \'DISABLED\', \'changed\': True, \'quoted\': False, \'key\': \'processLocal\', \'val\': \'ENABLED\'}, ' + \
            '"soBackupAction": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'soBackupAction\', \'val\': \'asdf\'}, ' + \
            '"cookieName": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'cookieName\', \'val\': \'adsf\'}, ' + \
            '"authn401": {\'default_value\': \'OFF\', \'changed\': True, \'quoted\': False, \'key\': \'authn401\', \'val\': \'ON\'}, ' + \
            '"soPersistenceTimeOut": {\'default_value\': 0, \'changed\': True, \'quoted\': False, \'key\': \'soPersistenceTimeOut\', \'val\': 1}, ' + \
            '"Authentication": {\'default_value\': \'OFF\', \'changed\': True, \'quoted\': False, \'key\': \'Authentication\', \'val\': \'ON\'}, ' + \
            '"healthThreshold": {\'default_value\': 0, \'changed\': True, \'quoted\': False, \'key\': \'healthThreshold\', \'val\': 1}, ' + \
            '"soMethod": {\'default_value\': \'NONE\', \'changed\': True, \'quoted\': False, \'key\': \'soMethod\', \'val\': \'OTHER\'}, ' + \
            '"oracleServerVersion": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'oracleServerVersion\', \'val\': \'asdf\'}, ' + \
            '"tosId": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'tosId\', \'val\': \'asdf\'}, ' + \
            '"persistAVPno": {\'default_value\': 1, \'changed\': True, \'quoted\': False, \'key\': \'persistAVPno\', \'val\': 2}, ' + \
            '"insertVserverIPPort": {\'default_value\': \'OFF\', \'changed\': True, \'quoted\': False, \'key\': \'insertVserverIPPort\', \'val\': \'ON\'}, ' + \
            '"connfailover": {\'default_value\': \'DISABLED\', \'changed\': True, \'quoted\': False, \'key\': \'connfailover\', \'val\': \'ENABLED\'}, ' + \
            '"minAutoscaleMembers": {\'default_value\': 0, \'changed\': True, \'quoted\': False, \'key\': \'minAutoscaleMembers\', \'val\': 1}, ' + \
            '"cacheable": {\'default_value\': \'NO\', \'changed\': True, \'quoted\': False, \'key\': \'cacheable\', \'val\': \'YES\'}, ' + \
            '"authnVs": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'authnVs\', \'val\': \'asdf\'}, ' + \
            '"disablePrimaryOnDown": {\'default_value\': \'DISABLED\', \'changed\': True, \'quoted\': False, \'key\': \'disablePrimaryOnDown\', \'val\': \'ENABLED\'}, ' + \
            '"redirectPortRewrite": {\'default_value\': \'DISABLED\', \'changed\': True, \'quoted\': False, \'key\': \'redirectPortRewrite\', \'val\': \'ENABLED\'}, ' + \
            '"rtspNat": {\'default_value\': \'OFF\', \'changed\': True, \'quoted\': False, \'key\': \'rtspNat\', \'val\': \'ON\'}, ' + \
            '"backupLB": {\'default_value\': \'ROUNDROBIN\', \'changed\': True, \'quoted\': False, \'key\': \'backupLB\', \'val\': \'LEASTCONNECTION\'}, ' + \
            '"mssqlServerVersion": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'mssqlServerVersion\', \'val\': \'asdf\'}, ' + \
            '"lbMethod": {\'default_value\': \'LEASTCONNECTION\', \'changed\': True, \'quoted\': False, \'key\': \'lbMethod\', \'val\': \'ROUNDROBIN\'}, ' + \
            '"macmodeRetainvlan": {\'default_value\': \'DISABLED\', \'changed\': True, \'quoted\': False, \'key\': \'macmodeRetainvlan\', \'val\': \'ENABLED\'}, ' + \
            '"RHIstate": {\'default_value\': \'PASSIVE\', \'changed\': True, \'quoted\': False, \'key\': \'RHIstate\', \'val\': \'ACTIVE\'}, ' + \
            '"redirectURL": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'redirectURL\', \'val\': \'asdf\'}, ' + \
            '"lbprofilename": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'lbprofilename\', \'val\': \'asdf\'}, ' + \
            '"RecursionAvailable": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'RecursionAvailable\', \'val\': \'asdf\'}, ' + \
            '"httpProfileName": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'httpProfileName\', \'val\': \'asdf\'}, ' + \
            '"cltTimeout": {\'default_value\': 180, \'changed\': True, \'quoted\': False, \'key\': \'cltTimeout\', \'val\': 181}, ' + \
            '"dnsProfileName": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'dnsProfileName\', \'val\': \'asdf\'}, ' + \
            '"IPMask": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'IPMask\', \'val\': \'adsf\'}, ' + \
            '"persistenceType": {\'default_value\': \'NONE\', \'changed\': True, \'quoted\': False, \'key\': \'persistenceType\', \'val\': \'COOKIEINSERT\'}, ' + \
            '"maxAutoscaleMembers": {\'default_value\': 0, \'changed\': True, \'quoted\': False, \'key\': \'maxAutoscaleMembers\', \'val\': 1}, ' + \
            '"l2Conn": {\'default_value\': \'OFF\', \'changed\': True, \'quoted\': False, \'key\': \'l2Conn\', \'val\': \'ON\'}, ' + \
            '"IPPattern": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'IPPattern\', \'val\': \'asdf\'}, ' + \
            '"dns64": {\'default_value\': \'DISABLED\', \'changed\': True, \'quoted\': False, \'key\': \'dns64\', \'val\': \'ENABLED\'}, ' + \
            '"skippersistency": {\'default_value\': \'None\', \'changed\': True, \'quoted\': False, \'key\': \'skippersistency\', \'val\': \'Other\'}, ' + \
            '"bypassAAAA": {\'default_value\': \'NO\', \'changed\': True, \'quoted\': False, \'key\': \'bypassAAAA\', \'val\': \'YES\'}, ' + \
            '"Listenpriority": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'Listenpriority\', \'val\': \'asdf\'}, ' + \
            '"pushVserver": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'pushVserver\', \'val\': \'asdf\'}, ' + \
            '"dbProfileName": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'dbProfileName\', \'val\': \'asdf\'}, ' + \
            '"persistMask": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'persistMask\', \'val\': \'asdf\'}, ' + \
            '"netProfile": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'netProfile\', \'val\': \'asdf\'}, ' + \
            '"pushMultiClients": {\'default_value\': \'NO\', \'changed\': True, \'quoted\': False, \'key\': \'pushMultiClients\', \'val\': \'YES\'}, ' + \
            '"pushLabel": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'pushLabel\', \'val\': \'asdf\'}, ' + \
            '"sessionless": {\'default_value\': \'DISABLED\', \'changed\': True, \'quoted\': False, \'key\': \'sessionless\', \'val\': \'ENABLED\'}, ' + \
            '"trofsPersistence": {\'default_value\': \'ENABLED\', \'changed\': True, \'quoted\': False, \'key\': \'trofsPersistence\', \'val\': \'DISABLED\'}, ' + \
            '"resRule": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'resRule\', \'val\': \'asdf\'}, ' + \
            '"AuthenticationHost": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'AuthenticationHost\', \'val\': \'asdf\'}, ' + \
            '"redirectFromPort": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'redirectFromPort\', \'val\': \'asdf\'}, ' + \
            '"soThreshold": {\'default_value\': 0, \'changed\': True, \'quoted\': False, \'key\': \'soThreshold\', \'val\': 1}, ' + \
            '"mysqlServerCapabilities": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'mysqlServerCapabilities\', \'val\': \'asdf\'}, ' + \
            '"soPersistence": {\'default_value\': \'DISABLED\', \'changed\': True, \'quoted\': False, \'key\': \'soPersistence\', \'val\': \'ENABLED\'}, ' + \
            '"appflowLog": {\'default_value\': \'DISABLED\', \'changed\': True, \'quoted\': False, \'key\': \'appflowLog\', \'val\': \'ENABLED\'}, ' + \
            '"retainConnectionsOnCluster": {\'default_value\': \'NO\', \'changed\': True, \'quoted\': False, \'key\': \'retainConnectionsOnCluster\', \'val\': \'YES\'}, ' + \
            '"rule": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'rule\', \'val\': \'asdf\'}, ' + \
            '"httpsRedirectUrl": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'httpsRedirectUrl\', \'val\': \'asdf\'}, ' + \
            '"tcpProfileName": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'tcpProfileName\', \'val\': \'asdf\'}, ' + \
            '"m": {\'default_value\': \'IP\', \'changed\': True, \'quoted\': False, \'key\': \'m\', \'val\': \'OTHER\'}, ' + \
            '"mysqlProtocolVersion": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'mysqlProtocolVersion\', \'val\': \'asdf\'}, ' + \
            '"backupPersistence": {\'default_value\': 0, \'changed\': True, \'quoted\': False, \'key\': \'backupPersistence\', \'val\': 10}, ' + \
            '"range": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'range\', \'val\': \'adsf\'}, ' + \
            '"backupVServer": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'backupVServer\', \'val\': \'ASDF\'}, ' + \
            '"dbsLb": {\'default_value\': \'DISABLED\', \'changed\': True, \'quoted\': False, \'key\': \'dbsLb\', \'val\': \'ENABLED\'}, ' + \
            '"Listenpolicy": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'Listenpolicy\', \'val\': \'asdf\'}, ' + \
            '"timeout": {\'default_value\': 0, \'changed\': True, \'quoted\': False, \'key\': \'timeout\', \'val\': 1}, ' + \
            '"newServiceRequest": {\'default_value\': 0, \'changed\': True, \'quoted\': False, \'key\': \'newServiceRequest\', \'val\': 1}, ' + \
            '"push": {\'default_value\': \'DISABLED\', \'changed\': True, \'quoted\': False, \'key\': \'push\', \'val\': \'ENABLED\'}, ' + \
            '"v6persistmasklen": {\'default_value\': \'128\', \'changed\': True, \'quoted\': False, \'key\': \'v6persistmasklen\', \'val\': \'127\'}, ' + \
            '"authnProfile": {\'default_value\': \'\', \'changed\': True, \'quoted\': False, \'key\': \'authnProfile\', \'val\': \'asdf\'}, ' + \
            '"downStateFlush": {\'default_value\': \'ENABLED\', \'changed\': True, \'quoted\': False, \'key\': \'downStateFlush\', \'val\': \'DISABLED\'} } }'

        self.assertEqual(orig.__repr__(), expected)

if __name__ == '__main__':
    unittest.main()
