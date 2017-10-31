from AttributeList import AttributeList
from NSObject import NSObject
import json

# Types of target:
#  svm: svc or sg ->monitor
#  sgs: sg->server
#  lsv: lb->service or sg
#  clb: cs->lbvserver
#  cvp: cs->vpnvserver
#  csp: cs vserver->cs policy
#  rsp: any vserver->responder policy
#  rwp: any vserver->rewrite policy

class Bind(NSObject):
    # source is the source object, not just the name
    # target is the target object, not nust the name
    def __init__(self, source, target, targetType, Attributes=None, port=None):
        self.targetType = targetType 
        self.InitVersion("12.0")
        self._objecttype = "bind_" + targetType
        self.source = source
        self.target = target
        self.port = port
        if Attributes is not None:
            for x in Attributes:
                self.Attributes[x] = Attributes[x]
        self._locked = True

    def InitVersion(self, version):
        attrs = {
            '12.0': {
                'svm': {
                    'monState': 'ENABLED',
                    'weight': 1,
                    'passive': 0
                },
                'sgs': {
                    'CustomServerID': '',
                    'hashId': '',
                    'state': 'ENABLED',
                    'weight': 1
                },
                'lsv': {
                    'weight': 1
                },
                'clb': {},
                'cvp': {},
                'csp': {
                    'targetLBVserver': '',
                    'priority': '',
                    'gotoPriorityExpression': '',
                    'invoke': '',
                    'type': ''
                },
                'rsp': {
                    'priority': '',
                    'gotoPriorityExpression': '',
                    'invoke': '',
                },
                'rwp': {
                    'priority': '',
                    'gotoPriorityExpression': '',
                    'invoke': '',
                    'type': ''
                }
            }
        }
        if version not in attrs:
            raise KeyError, "Invalid version."
        if self.targetType not in attrs[version]:
            raise KeyError, "Bind type not identified."

        self.__dict__['Attributes'] = AttributeList(attrs[version][self.targetType])


    def LocalAttributes(self):
        outstring  = " \"source\": {}, ".format(json.dumps(self.source))
        outstring += " \"target\": {}, ".format(json.dumps(self.target))
        return outstring

    def __str__(self):
        cmds = {
            'svm': '-monitorName ',
            'sgs': '',
            'lsv': '',
            'clb': '-lbvserver ',
            'cvp': '-vServer ',
            'csp': '-policyName ',
            'rsp': '-policyName ',
            'rwp': '-policyName '
        }
        if self.port is not None:
            tn = self.target.name + " " + str(self.port)
        else:
            tn = self.target.name
        outstring = "bind " + self.source._objecttype + " " + self.source.name + " " + \
            cmds[self.targetType] + tn + " " + str(self.Attributes)
        return outstring
