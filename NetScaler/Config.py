from Server import Server
from Service import Service
from ServiceGroup import ServiceGroup
from LBvServer import LBvServer
from CSvServer import CSvServer
from CSAction import CSAction
from CSPolicy import CSPolicy
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
        serverisip = False
        try:
            socket.inet_aton(server)
            serverisip = True
        except socket.error:
            serverisip = False

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
        self.cspolicies[name] = CSPolicy(name, Attributes)

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
