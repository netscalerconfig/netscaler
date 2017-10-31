from Server import Server
from Service import Service
from ServiceGroup import ServiceGroup
from LBvServer import LBvServer
from CSvServer import CSvServer
from CSAction import CSAction
from CSPolicy import CSPolicy
from Bind import Bind
import socket

class Config:
    def __init__(self):
        self.servers = {}
        self.services = {}
        self.servicegroups = {}
        self.lbvservers = {}
        self.csvservers = {}
        self.csactions = {}
        self.cspolicies = {}
        self.vservernames = {}
        self.vsipport_tuples = {}
        self.svcipport_tuples = {}
        self.serverips = {}

    def add_lb_vserver(self, name, servicetype, IPAddress, port, Attributes=None):
        ipport_tuple = str(IPAddress) + str(port)

        if name in self.lbvservers or name in self.vservernames: 
            raise KeyError, "Duplicate name of virtual server"
        if ipport_tuple in self.vsipport_tuples: 
            raise KeyError, "IP and Port already in use"

        self.lbvservers[name] = LBvServer(name, servicetype, IPAddress, port, Attributes)
        self.vsipport_tuples[ipport_tuple] = 1
        self.vservernames[name] = 1

    def add_cs_vserver(self, name, servicetype, IPAddress, port, Attributes=None):
        ipport_tuple = str(IPAddress) + str(port)

        if name in self.csvservers or name in self.vservernames: 
            raise KeyError, "Duplicate name of virtual server"
        if ipport_tuple in self.vsipport_tuples: 
            raise KeyError, "IP and Port already in use"

        self.csvservers[name] = CSvServer(name, servicetype, IPAddress, port, Attributes)
        self.vsipport_tuples[ipport_tuple] = 1
        self.vsipport_tuples[ipport_tuple] = 1
        self.vservernames[name] = 1

    def add_server(self, name, IPAddress, Attributes=None):
        if name in self.servers:
            raise KeyError, "Duplicate name of server"
        if IPAddress in self.serverips:
            raise KeyError, "Duplicate IP for server"

        self.servers[name] = Server(name, IPAddress, Attributes)
        self.serverips[IPAddress] = 1

    def add_service(self, name, server, servicetype, port, Attributes=None):
        ipport_tuple = str(server) + str(port)
        serverisip = self.is_ip(server)

        if serverisip and server not in self.serverips:
            self.servers[server] = Server(server, server)

        if serverisip and server not in self.servers and server in self.serverips:
            raise KeyError, "IP already defined in a server"
        if not serverisip and server not in self.servers:
            raise KeyError, "Server not defined"
        if name in self.services or name in self.servicegroups:
            raise KeyError, "Duplicate name of service"
        if ipport_tuple in self.svcipport_tuples:
            raise KeyError, "IP and Port already in use"

        self.services[name] = Service(name, server, servicetype, port, Attributes)
        self.svcipport_tuples[ipport_tuple] = 1

    def add_servicegroup(self, name, servicetype, Attributes=None):
        if name in self.servicegroups or name in self.services:
            raise KeyError, "Duplicate name of service"
        self.servicegroups[name] = ServiceGroup(name, servicetype, Attributes)

    def add_cs_action(self, name, Attributes=None):
        if name in self.csactions:
            raise KeyError, "Duplicate name of cs action"
        self.csactions[name] = CSAction(name, Attributes)

    def add_cs_policy(self, name, Attributes=None):
        if name in self.cspolicies:
            raise KeyError, "Duplicate name of cs policy"
        if 'action' in Attributes and Attributes['action'] not in self.csactions:
            raise KeyError, "Action doesn't exist"
        self.cspolicies[name] = CSPolicy(name, Attributes)

    def bind_lbvserver_service(self, lb_name, svc_name, Attributes=None):
        if lb_name not in self.lbvservers:
            raise KeyError, "Load Balancing vServer doesn't exist"
        if svc_name not in self.services:
            raise KeyError, "Service doesn't exist"
        if svc_name in self.lbvservers[lb_name].svc_bind:
            raise KeyError, "Service already bound"

        self.lbvservers[lb_name].svc_bind[svc_name] = \
            Bind(self.lbvservers[lb_name], self.services[svc_name], 'lsv', Attributes)

    def bind_lbvserver_servicegroup(self, lb_name, sg_name, Attributes=None):
        if lb_name not in self.lbvservers:
            raise KeyError, "Load Balancing vServer doesn't exist"
        if sg_name not in self.servicegroups:
            raise KeyError, "ServiceGroup doesn't exist"
        if sg_name in self.lbvservers[lb_name].svc_bind:
            raise KeyError, "ServiceGroup already bound"

        self.lbvservers[lb_name].svc_bind[sg_name] = \
            Bind(self.lbvservers[lb_name], self.servicegroups[sg_name], 'lsv', Attributes)

    def bind_servicegroup_server(self, sg_name, srv_name, port, Attributes=None):
        serverisip = self.is_ip(srv_name)
        if sg_name not in self.servicegroups:
            raise KeyError, "ServiceGroup doesn't exist"
        if serverisip:
            if srv_name not in self.serverips:
                self.add_server(srv_name, srv_name)
            elif srv_name not in self.servers:
                raise KeyError, "Server already exists with a name"
        else:
            if srv_name not in self.servers:
                raise KeyError, "Server doesn't exist"
        self.servicegroups[sg_name].server_bind[srv_name] = \
            Bind(self.servicegroups[sg_name], self.servers[srv_name], 'sgs', Attributes, port)


    def __str__(self):
        out = ""
        for x in self.servers: out += str(self.servers[x]) + '\n'
        for x in self.services: out += str(self.services[x]) + '\n'
        for x in self.servicegroups: out += str(self.servicegroups[x]) + '\n'
        for x in self.lbvservers: out += str(self.lbvservers[x]) + '\n'
        for x in self.csactions: out += str(self.csactions[x]) + '\n'
        for x in self.cspolicies: out += str(self.cspolicies[x]) + '\n'
        for x in self.csvservers: out += str(self.csvservers[x]) + '\n'

        return out

    def is_ip(self, str):
        try:
            socket.inet_aton(str)
            return True
        except socket.error:
            return False
