from .Server import Server
from .Service import Service
from .ServiceGroup import ServiceGroup
from .LBvServer import LBvServer
from .CSvServer import CSvServer
from .VPNvServer import VPNvServer
from .CSAction import CSAction
from .LDAPAction import LDAPAction
from .RadiusAction import RadiusAction
from .TacacsAction import TacacsAction
from .CertAction import CertAction
from .Policy import Policy
from .Bind import Bind
import socket
import logging

class Config:
    def __init__(self):
        self._version = '12.0'
        self.servers = {}
        self.services = {}
        self.servicegroups = {}
        self.lbvservers = {}
        self.csvservers = {}
        self.vpnvservers = {}
        self.csactions = {}
        self.cspolicies = {}
        self.vservernames = {}
        self.vsipport_tuples = {}
        self.svcipport_tuples = {}
        self.serverips = {}
        self.ldapactions = {}
        self.radiusactions = {}
        self.tacacsactions = {}
        self.certactions = {}
        self.certpolicies = {}
        self.tacacspolicies = {}
        self.radiuspolicies = {}
        self.ldappolicies = {}
        self.comment_list = []

    def add_lb_vserver(self, name, servicetype, IPAddress, port, Attributes=None):
        ipport_tuple = str(IPAddress) + str(port)

        if name in self.vservernames: 
            raise KeyError("Duplicate name of virtual server")
        if ipport_tuple in self.vsipport_tuples: 
            raise KeyError("IP and Port already in use")

        self.lbvservers[name] = LBvServer(name, servicetype, IPAddress, port, Attributes)
        if IPAddress != '0.0.0.0' and str(port) != '0':
            self.vsipport_tuples[ipport_tuple] = 1
        self.vservernames[name] = 1

    def add_cs_vserver(self, name, servicetype, IPAddress, port, Attributes=None):
        ipport_tuple = str(IPAddress) + str(port)

        if name in self.vservernames: 
            raise KeyError("Duplicate name of virtual server")
        if ipport_tuple in self.vsipport_tuples: 
            return self.vsipport_tuples[ipport_tuple]

        self.csvservers[name] = CSvServer(name, servicetype, IPAddress, port, Attributes)
        self.vsipport_tuples[ipport_tuple] = name
        self.vservernames[name] = ipport_tuple
        return name

    def add_vpn_vserver(self, name, servicetype, IPAddress, port, Attributes=None):
        ipport_tuple = str(IPAddress) + str(port)

        if name in self.vservernames: 
            raise KeyError("Duplicate name of virtual server")
        if ipport_tuple in self.vsipport_tuples: 
            raise KeyError("IP and Port already in use")

        self.vpnvservers[name] = VPNvServer(name, servicetype, IPAddress, port, Attributes)
        if IPAddress != '0.0.0.0' and str(port) != '0':
            self.vsipport_tuples[ipport_tuple] = 1
        self.vservernames[name] = 1

    def add_server(self, name, IPAddress, Attributes=None):
        if name in self.servers:
            # si existe y la ip no es igual, levantamos este error
            # raise KeyError("Duplicated name of server")
            logging.warning('Duplicated name of server: %s', name)
            return
        if IPAddress in self.serverips:
            # raise KeyError("Duplicate IP for server")
            logging.warning('Duplicated IP address: %s', IPAddress)
            return

        self.servers[name] = Server(name, IPAddress, Attributes)
        self.serverips[IPAddress] = 1

    def add_service(self, name, server, servicetype, port, Attributes=None):
        ipport_tuple = str(server) + str(port)
        serverisip = self.is_ip(server)

        if serverisip and server not in self.serverips:
            self.servers[server] = Server(server, server)

        if serverisip and server not in self.servers and server in self.serverips:
            raise KeyError("IP already defined in a server")
        if not serverisip and server not in self.servers:
            raise KeyError("Server not defined")
        if name in self.services or name in self.servicegroups:
            raise KeyError("Duplicate name of service")
        if ipport_tuple in self.svcipport_tuples:
            raise KeyError("IP and Port already in use")

        self.services[name] = Service(name, server, servicetype, port, Attributes)
        self.svcipport_tuples[ipport_tuple] = 1

    def add_servicegroup(self, name, servicetype, Attributes=None):
        if name in self.servicegroups or name in self.services:
            raise KeyError("Duplicate name of service")
        self.servicegroups[name] = ServiceGroup(name, servicetype, Attributes)

    def add_cs_action(self, name, Attributes=None):
        if name in self.csactions:
            raise KeyError("Duplicate name of cs action")
        if Attributes is not None and 'targetLBVserver' in Attributes:
            if Attributes['targetLBVserver'] not in self.lbvservers:
                raise KeyError("Target LB vServer {} doesn't exist".format(Attributes['targetLBVserver']))

        self.csactions[name] = CSAction(name, Attributes)

    def add_cs_policy(self, name, Attributes=None):
        if name in self.cspolicies:
            raise KeyError("Duplicate name of cs policy")
        if 'domain' not in Attributes and 'url' not in Attributes and 'rule' not in Attributes:
            raise KeyError("Too few arguments")
        if 'action' in Attributes and Attributes['action'] not in self.csactions:
            raise KeyError("Action doesn't exist")
        self.cspolicies[name] = Policy(name, 'cspolicy', Attributes)

    def bind_lbvserver_service(self, lb_name, svc_name, Attributes=None):
        if lb_name not in self.lbvservers:
            raise KeyError("Load Balancing vServer doesn't exist")
        if svc_name not in self.services:
            raise KeyError("Service doesn't exist")
        if svc_name in self.lbvservers[lb_name].svc_bind:
            raise KeyError("Service already bound")

        self.lbvservers[lb_name].svc_bind[svc_name] = \
            Bind(self.lbvservers[lb_name], self.services[svc_name], 'lsv', Attributes)

    def bind_lbvserver_servicegroup(self, lb_name, sg_name, Attributes=None):
        if lb_name not in self.lbvservers:
            raise KeyError("Load Balancing vServer doesn't exist")
        if sg_name not in self.servicegroups:
            raise KeyError("ServiceGroup doesn't exist")
        if sg_name in self.lbvservers[lb_name].svc_bind:
            raise KeyError("ServiceGroup already bound")

        self.lbvservers[lb_name].svc_bind[sg_name] = \
            Bind(self.lbvservers[lb_name], self.servicegroups[sg_name], 'lsv', Attributes)

    def bind_servicegroup_server(self, sg_name, srv_name, port, Attributes=None):
        serverisip = self.is_ip(srv_name)
        if sg_name not in self.servicegroups:
            raise KeyError("ServiceGroup doesn't exist")
        if serverisip:
            if srv_name not in self.serverips:
                self.add_server(srv_name, srv_name)
            elif srv_name not in self.servers:
                raise KeyError("Server already exists with a name")
        else:
            if srv_name not in self.servers:
                raise KeyError("Server doesn't exist")
        srv_key = srv_name + '_' + port
        self.servicegroups[sg_name].server_bind[srv_key] = \
            Bind(self.servicegroups[sg_name], self.servers[srv_name], 'sgs', Attributes, port)

    def bind_cs_lbvserver(self, cs_name, lb_name, Attributes=None):
        if cs_name not in self.csvservers:
            raise KeyError("Content Swith vServer doesn't exist")
        if lb_name not in self.lbvservers:
            raise KeyError("LB vServer doesn't exist")

        self.csvservers[cs_name].setCSDefault( \
            Bind(self.csvservers[cs_name], self.lbvservers[lb_name], 'clb', Attributes))

    def bind_cs_cspolicy(self, cs_name, cspol_name, Attributes=None):
        if cs_name not in self.csvservers:
            raise KeyError("Content Swith vServer doesn't exist")
        if cspol_name not in self.cspolicies:
            raise KeyError("CS Policy doesn't exist")
        if 'priority' not in Attributes:
            raise KeyError("Priority is mandatory for advanced expressions")

        self.csvservers[cs_name].csp_bind[Attributes['priority']] = \
            Bind(self.csvservers[cs_name], self.cspolicies[cspol_name], 'csp', Attributes)

    def add_auth_ldapaction(self, name, server, Attributes=None):
        if name in self.ldapactions:
            raise KeyError("Dumplicate name of ldapAction")

        self.ldapactions[name] = LDAPAction(name, server, Attributes)

    def add_auth_radiusaction(self, name, server, radkey, Attributes=None):
        if name in self.radiusactions:
            raise KeyError("Dumplicate name of radiusAction")

        self.radiusactions[name] = RadiusAction(name, server, radkey, Attributes)

    def add_auth_tacacsaction(self, name, server, tacacssecret, Attributes=None):
        if name in self.tacacsactions:
            raise KeyError("Dumplicate name of tacacsAction")

        self.tacacsactions[name] = TacacsAction(name, server, tacacssecret, Attributes)

    def add_auth_certaction(self, name, Attributes=None):
        if name in self.certactions:
            raise KeyError("Dumplicate name of certAction")

        self.certactions[name] = CertAction(name, Attributes, self._version)

    def add_auth_certpolicy(self, name, Attributes=None):
        if 'rule' not in Attributes:
            raise KeyError("Rule is required")
        if 'action' not in Attributes:
            raise KeyError("Action is required")
        if Attributes['action'] not in self.certactions:
            raise KeyError("Action doesn't exist")

        self.certpolicies[name] = Policy(name, 'certpolicy', Attributes, self._version)

    def add_auth_tacacspolicy(self, name, Attributes=None):
        if 'rule' not in Attributes:
            raise KeyError("Rule is required")
        if 'action' not in Attributes:
            raise KeyError("Action is required")
        if Attributes['action'] not in self.tacacsactions:
            raise KeyError("Action doesn't exist")

        self.tacacspolicies[name] = Policy(name, 'tacacspolicy', Attributes, self._version)

    def add_auth_radiuspolicy(self, name, Attributes=None):
        if 'rule' not in Attributes:
            raise KeyError("Rule is required")
        if 'action' not in Attributes:
            raise KeyError("Action is required")
        if Attributes['action'] not in self.radiusactions:
            raise KeyError("Action doesn't exist")

        self.radiuspolicies[name] = Policy(name, 'radiuspolicy', Attributes, self._version)

    def add_auth_ldappolicy(self, name, Attributes=None):
        if 'rule' not in Attributes:
            raise KeyError("Rule is required")
        if 'action' not in Attributes:
            raise KeyError("Action is required")
        if Attributes['action'] not in self.ldapactions:
            raise KeyError("Action doesn't exist")

        self.ldappolicies[name] = Policy(name, 'ldappolicy', Attributes, self._version)

    def __str__(self):
        out = ""
        if len(self.comment_list) > 0:
            out += "# Global settings need to be configured manually"
            for x in self.comment_list:
                out += '\n# {}'.format(x)
            out += '\n\n'

        for x in self.ldapactions: out += str(self.ldapactions[x]) + '\n'
        for x in self.radiusactions: out += str(self.radiusactions[x]) + '\n'
        for x in self.tacacsactions: out += str(self.tacacsactions[x]) + '\n'
        for x in self.certactions: out += str(self.certactions[x]) + '\n'
        for x in self.certpolicies: out += str(self.certpolicies[x]) + '\n'
        for x in self.tacacspolicies: out += str(self.tacacspolicies[x]) + '\n'
        for x in self.radiuspolicies: out += str(self.radiuspolicies[x]) + '\n'
        for x in self.ldappolicies: out += str(self.ldappolicies[x]) + '\n'
        for x in self.servers: out += str(self.servers[x]) + '\n'
        for x in self.services: out += str(self.services[x]) + '\n'
        for x in self.servicegroups: out += str(self.servicegroups[x]) + '\n'
        for x in self.lbvservers: out += str(self.lbvservers[x]) + '\n'
        for x in self.csactions: out += str(self.csactions[x]) + '\n'
        for x in self.cspolicies: out += str(self.cspolicies[x]) + '\n'
        for x in self.csvservers: out += str(self.csvservers[x]) + '\n'
        for x in self.vpnvservers: out += str(self.vpnvservers[x]) + '\n'
        return out

    def is_ip(self, str):
        try:
            socket.inet_aton(str)
            return True
        except socket.error:
            return False
