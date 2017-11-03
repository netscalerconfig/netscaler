# NetScaler batch generation Python Library

When loaded, this librar will offer access to a class that allows creation of NetScaler config files. This library will validate most configurations before generating the config file.

Library must be loaded by using:

_import NetScaler_

The object can be generated using the following command:

_nsconfig = NetScaler.NewConfig()_

## Functions

* _NetScaler.add_lb_vserver(name, servicetype, IPAddress, port, Attributes)_

    Will create a LB vServer of type "servicetype" using IPAddress and Port. 
    ServiceType must match one of NetScaler's types. Please refer to NetScaler documentation
    This library will check that the IPAddress and port tuple is not used in the same config before. If so, it will generate an exception.
    The accepted attributes are based on NetScaler firmware version 12.0. Attributes accepted must be of the form of a Dictionary and the keys are case sensitive. For documentation of each attribute please use NetScaler documentation. The list of accepted keys is:

        * range
        * IPPattern
        * IPMask
        * appflowLog
        * Authentication
        * AuthenticationHost
        * authn401
        * authnProfile
        * authnVs
        * backupLB
        * backupPersistence
        * backupVServer
        * bypassAAAA
        * cacheable
        * cltTimeout
        * comment
        * connfailover
        * cookieName
        * dbProfileName
        * dbsLb
        * disablePrimaryOnDown
        * dns64
        * dnsProfileName
        * downStateFlush
        * healthThreshold
        * httpProfileName
        * httpsRedirectUrl
        * icmpVsrResponse
        * insertVserverIPPort
        * l2Conn
        * lbMethod
        * lbprofilename
        * Listenpolicy
        * Listenpriority
        * m
        * macmodeRetainvlan
        * maxAutoscaleMembers
        * minAutoscaleMembers
        * mssqlServerVersion
        * mysqlCharacterSet
        * mysqlProtocolVersion
        * mysqlServerCapabilities
        * mysqlServerVersion
        * netProfile
        * newServiceRequest
        * newServiceRequestIncrementInterval
        * oracleServerVersion
        * persistAVPno
        * persistenceBackup
        * persistenceType
        * persistMask
        * processLocal
        * push
        * pushLabel
        * pushMultiClients
        * pushVserver
        * RecursionAvailable
        * redirectFromPort
        * redirectPortRewrite
        * redirectURL
        * resRule
        * retainConnectionsOnCluster
        * RHIstate
        * rtspNat
        * rule
        * sessionless
        * skippersistency
        * soBackupAction
        * soMethod
        * soPersistence
        * soPersistenceTimeOut
        * soThreshold
        * state"
        * tcpProfileName
        * timeout
        * tosId
        * trofsPersistence
        * v6persistmasklen

* _NetScaler.add_cs_vserver(name, servicetype, IPAddress, port, Attributes)_

    Will create a CS vServer of type "servicetype" using IPAddress and Port. ServiceType must match one of NetScaler's types. Please refer to NetScaler documentation. This library will check that the IPAddress and port tuple is not used in the same config before. If so, it will generate an exception.
    The accepted attributes are based on NetScaler firmware version 12.0. Attributes accepted must be of the form of a Dictionary and the keys are case sensitive. For documentation of each attribute please use NetScaler documentation. The list of accepted keys is:

        * range
        * IPPattern
        * IPMask
        * targetType
        * appflowLog
        * Authentication
        * AuthenticationHost
        * authn401
        * authnProfile
        * authnVs
        * backupVServer
        * cacheable
        * caseSensitive
        * cltTimeout
        * comment
        * dbProfileName
        * dbsLb
        * disablePrimaryOnDown
        * dnsProfileName
        * dnsRecordType
        * downStateFlush
        * httpProfileName
        * icmpVsrResponse
        * insertVserverIPPort
        * l2Conn
        * Listenpolicy
        * Listenpriority
        * mssqlServerVersion
        * mysqlCharacterSet
        * mysqlProtocolVersion
        * mysqlServerCapabilities
        * mysqlServerVersion
        * netProfile
        * oracleServerVersion
        * persistenceId
        * presedence
        * push
        * pushLabel
        * pushMultiClients
        * pushVserver
        * redirectPortRewrite
        * redirectURL
        * RHIstate
        * rtspNat
        * soBackupAction
        * soMethod
        * soPersistence
        * soPersistenceTimeOut
        * soThreshold
        * state
        * tcpProfileName
        * td

* _NetScaler.add_vpn_vserver(self, name, servicetype, IPAddress, port, Attributes)_

    Will create a VPN vServer of type "servicetype" using IPAddress and Port. ServiceType must be 'SSL'. Please refer to NetScaler documentation. This library will check that the IPAddress and port tuple is not used in the same config before. If so, it will generate an exception.
    The accepted attributes are based on NetScaler firmware version 12.0. Attributes accepted must be of the form of a Dictionary and the keys are case sensitive. For documentation of each attribute please use NetScaler documentation. The list of accepted keys is:

        * appflowLog
        * authentication
        * authnProfile
        * cginfraHomePageRedirect
        * comment
        * deploymentType
        * deviceCert
        * doubleHop
        * downStateFlush
        * dtls
        * httpProfileName
        * icaOnly
        * icaProxySessionMigration
        * icmpVsrResponse
        * l2Conn
        * LinuxEPAPluginUpgrade
        * Listenpolicy
        * loginOnce
        * logoutOnSmartcardRemoval
        * MacEPAPluginUpgrade
        * maxAAAUsers
        * maxLoginAttempts
        * netProfile
        * pcoipVserverProfileName
        * rdpServerProfileName
        * RHIstate
        * state
        * tcpProfileName
        * vserverFqdn
        * WindowsEPAPluginUpgrade

* _NetScaler.add_server(name, IPAddress, Attributes)_

    Will create a server. Checks of duplicate IP addresses will be done before registering the object in the config.
    The accepted attributes are based on NetScaler firmware version 12.0. Attributes accepted must be of the form of a Dictionary and the keys are case sensitive. For documentation of each attribute please use NetScaler documentation. The list of accepted keys is:

        * domainResolveRetry
        * IPv6Address
        * translationIp
        * translationMask
        * state
        * comment

* _NetScaler.add_service(name, server, servicetype, port, Attributes)_

    Will create a service. Will check for duplicate names. Also, if the service is created with an IP address of a server previously defined, will generate an exception. Library will also check if service being created is referencing a server name that was not previously created and generate an exception. If the service references an IP address and the server doesn't exist, it will create it automatically.
    The accepted attributes are based on NetScaler firmware version 12.0. Attributes accepted must be of the form of a Dictionary and the keys are case sensitive. For documentation of each attribute please use NetScaler documentation. The list of accepted keys is:

        * accessDown
        * appflowLog
        * cacheable
        * cacheType
        * cip
        * CKA
        * clearTextPort
        * cltTimeout
        * CMP
        * comment
        * CustomServerID
        * dnsProfileName
        * downStateFlush
        * hashId
        * healthMonitor
        * httpProfileName
        * maxBandwidth
        * maxClient
        * maxReq
        * monConnectionClose
        * monThreshold
        * netProfile
        * pathMonitor
        * pathMonitorIndv
        * processLocal
        * rtspSessionidRemap
        * sp
        * state
        * svrTimeout
        * TCPB
        * tcpProfileName
        * td
        * useproxyport
        * usip

* _NetScaler.add_servicegroup(name, servicetype, Attributes)_

    Will create a servicegroup. Name duplicates will generate an exception.
    The accepted attributes are based on NetScaler firmware version 12.0. Attributes accepted must be of the form of a Dictionary and the keys are case sensitive. For documentation of each attribute please use NetScaler documentation. The list of accepted keys is:

        * appflowLog
        * autoScale
        * memberPort
        * cacheable
        * cacheType
        * cip
        * CKA
        * cltTimeout
        * CMP
        * comment
        * downStateFlush
        * healthMonitor
        * httpProfileName
        * maxBandwidth
        * maxClient
        * maxReq
        * monConnectionClose
        * monThreshold
        * netProfile
        * pathMonitor
        * pathMonitorIndv
        * rtspSessionidRemap
        * sp
        * state
        * svrTimeout
        * TCPB
        * tcpProfileName
        * td
        * useproxyport
        * usip

* _NetScaler.add_cs_action(name, Attributes)_

    Will create a content switch action. Name duplicates will generate an exception. If the action is created with 'targetLBVserver' attribute, the existence of the lb vserver referenced is checked, if it doesn't exist the library will generate an exception.
    The accepted attributes are based on NetScaler firmware version 12.0. Attributes accepted must be of the form of a Dictionary and the keys are case sensitive. For documentation of each attribute please use NetScaler documentation. The list of accepted keys is:

        * comment
        * targetLBVserver
        * targetVserver
        * targetVserverExpr

* _NetScaler.add_cs_policy(name, Attributes)_

    Will create a content switch policy. Name duplicates will generate an exception. The 'action' attribute is optional, but recommended. This library has been created with "Advanced Expressions" in mind. At lease one of the 'domain', 'url' or 'rule' attributes must exist.
    The accepted attributes are based on NetScaler firmware version 12.0. Attributes accepted must be of the form of a Dictionary and the keys are case sensitive. For documentation of each attribute please use NetScaler documentation. The list of accepted keys is:

        * domain
        * logAction (ignored for now)
        * url
        * rule
        * action

* _NetScaler.bind_lbvserver_service(lb_name, svc_name, Attributes)_

    Will bind a service with a lb vServer. This function will check for the existence of both objects. The only attribute accepted is 'weight'

* _NetScaler.bind_lbvserver_servicegroup(lb_name, sg_name, Attributes)_

    Will bind a servicegroup with an lb vServer. This function will check for the existence of both objects. The only attribute accepted is 'weight'

* _NetScaler.bind_servicegroup_server(sg_name, srv_name, port, Attributes)_

    Will bind a server with the servicegroup. If the server is called by name, the existence of the server is validates before the bind; if the server doesn't exist an exception is generated. If the server is called by IP and the server exists with a name different than the IP address, an exception is generated and if it doesn't exist, a server is created using the ip as name.
    The accepted attributes are based on NetScaler firmware version 12.0. Attributes accepted must be of the form of a Dictionary and the keys are case sensitive. For documentation of each attribute please use NetScaler documentation. The list of accepted keys is:

        * CustomServerID
        * hashId
        * state
        * weight

* _NetScaler.bind_cs_lbvserver(cs_name, lb_name, Attributes)_

    Will bind the lb vserver as the default content switch behavior. The library will check for the existence of both objects, if one or both don't exist an exception will be generated. Attributes will be ignored.

* _NetScaler.bind_cs_cspolicy(cs_name, cspol_name, Attributes)_

    Will bind a content switch policy with a cs vserver. 'priority' attributes is mandatory and the same priority cannot be used on the same virtual server.
    The accepted attributes are based on NetScaler firmware version 12.0. Attributes accepted must be of the form of a Dictionary and the keys are case sensitive. For documentation of each attribute please use NetScaler documentation. The list of accepted keys is:

        * targetLBVserver
        * priority
        * gotoPriorityExpression
        * invoke

* _NetScaler.add_auth_ldapaction(self, name, server, Attributes)_

    Will create an LDAP authentication server. Library will check for duplicate names and if so, it will generate an exception.
    The accepted attributes are based on NetScaler firmware version 12.0. Attributes accepted must be of the form of a Dictionary and the keys are case sensitive. For documentation of each attribute please use NetScaler documentation. The list of accepted keys is:

        * Attribute1
        * Attribute10
        * Attribute11
        * Attribute12
        * Attribute13
        * Attribute14
        * Attribute15
        * Attribute16
        * Attribute2
        * Attribute3
        * Attribute4
        * Attribute5
        * Attribute6
        * Attribute7
        * Attribute8
        * Attribute9
        * authentication
        * authTimeout
        * defaultAuthenticationGroup
        * followReferrals
        * maxLDAPReferrals
        * groupAttrName
        * groupNameIdentifier
        * groupSearchAttribute
        * ldapBase
        * ldapBindDn
        * ldapHostname
        * ldapLoginName
        * nestedGroupExtraction
        * maxNestingLevel
        * groupSearchSubAttribute
        * groupSearchFilter
        * OTPSecret
        * passwdChange
        * referralDNSLookup
        * msSRVRecordlocation
        * requireUser
        * searchFilter
        * secType
        * serverPort
        * ssoNameAttribute
        * subAttributeName
        * svrType
        * validateServerCert

* _NetScaler.add_auth_radiusaction(self, name, server, radkey, Attributes=None)_

    Will create an RADIUS authentication server. Library will check for duplicate names and if so, it will generate an exception.
    The accepted attributes are based on NetScaler firmware version 12.0. Attributes accepted must be of the form of a Dictionary and the keys are case sensitive. For documentation of each attribute please use NetScaler documentation. The list of accepted keys is:

        * accounting
        * authentication
        * authservRetry
        * authTimeout
        * callingstationid
        * defaultAuthenticationGroup
        * ipAttributeType
        * ipVendorID
        * passEncoding
        * pwdAttributeType
        * pwdVendorID
        * radAttributeType
        * radGroupSeparator
        * radGroupsPrefix
        * radNASid
        * radNASip
        * radVendorID
        * serverPort

* _NetScaler.add_auth_tacacsaction(self, name, server, tacacssecret, Attributes=None)_

    Will create an TACACS authentication server. Library will check for duplicate names and if so, it will generate an exception.
    The accepted attributes are based on NetScaler firmware version 12.0. Attributes accepted must be of the form of a Dictionary and the keys are case sensitive. For documentation of each attribute please use NetScaler documentation. The list of accepted keys is:

        * accounting
        * Attribute1
        * Attribute10
        * Attribute11
        * Attribute12
        * Attribute13
        * Attribute14
        * Attribute15
        * Attribute16
        * Attribute2
        * Attribute3
        * Attribute4
        * Attribute5
        * Attribute6
        * Attribute7
        * Attribute8
        * Attribute9
        * auditFailedCmds
        * authorization
        * authTimeout
        * defaultAuthenticationGroup
        * groupAttrName
        * serverPort

* _NetScaler.add_auth_certaction(self, name, Attributes=None)_

    Will create an Certificate authentication server. Library will check for duplicate names and if so, it will generate an exception.
    The accepted attributes are based on NetScaler firmware version 12.0. Attributes accepted must be of the form of a Dictionary and the keys are case sensitive. For documentation of each attribute please use NetScaler documentation. The list of accepted keys is:

        * defaultAuthenticationGroup
        * groupNameField
        * twoFactor
        * userNameField

* _NetScaler.add_auth_certpolicy(self, name, Attributes=None)_

    Will create a cert authentication policy. Name duplicates will generate an exception. The 'action' and 'rule' attribute are mandatory. This library has been created with "Advanced Expressions" in mind.
    The accepted attributes are based on NetScaler firmware version 12.0. Attributes accepted must be of the form of a Dictionary and the keys are case sensitive. For documentation of each attribute please use NetScaler documentation. The list of accepted keys is:

        * rule
        * action

* _NetScaler.add_auth_tacacspolicy(self, name, Attributes=None)_

    Will create a TACACS authentication policy. Name duplicates will generate an exception. The 'action' and 'rule' attribute are mandatory. This library has been created with "Advanced Expressions" in mind.
    The accepted attributes are based on NetScaler firmware version 12.0. Attributes accepted must be of the form of a Dictionary and the keys are case sensitive. For documentation of each attribute please use NetScaler documentation. The list of accepted keys is:

        * rule
        * action

* _NetScaler.add_auth_radiuspolicy(self, name, Attributes=None)_

    Will create a RADIUS authentication policy. Name duplicates will generate an exception. The 'action' and 'rule' attribute are mandatory. This library has been created with "Advanced Expressions" in mind.
    The accepted attributes are based on NetScaler firmware version 12.0. Attributes accepted must be of the form of a Dictionary and the keys are case sensitive. For documentation of each attribute please use NetScaler documentation. The list of accepted keys is:

        * rule
        * action

* _NetScaler.add_auth_ldappolicy(self, name, Attributes=None)_

    Will create a LDAP authentication policy. Name duplicates will generate an exception. The 'action' and 'rule' attribute are mandatory. This library has been created with "Advanced Expressions" in mind.
    The accepted attributes are based on NetScaler firmware version 12.0. Attributes accepted must be of the form of a Dictionary and the keys are case sensitive. For documentation of each attribute please use NetScaler documentation. The list of accepted keys is:

        * rule
        * action


