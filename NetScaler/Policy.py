from .AttributeList import AttributeList
from .NSObject import NSObject
import json

class Policy(NSObject):
    def __init__(self, name, poltype, Attributes=None, version=None):
        self.attr = {
            '12.0': {
                'cspolicy': {
                    'attrs': {
                        "domain": "",
                        "logAction": "",
                        "url": "",
                        "rule": "",
                        "action": ""
                    },
                    'quoted': [ "rule" ],
                    'policytype': 'cs policy'
                },
                'certpolicy': {
                    'attrs': { 
                        'rule': "",
                        'action': ""
                    },
                    'quoted': [ 'rule' ],
                    'policytype': 'authentication certpolicy'
                },
                'ldappolicy': {
                    'attrs': { 
                        'rule': "",
                        'action': ""
                    },
                    'quoted': [ 'rule' ],
                    'policytype': 'authentication ldappolicy'
                },
                'radiuspolicy': {
                    'attrs': { 
                        'rule': "",
                        'action': ""
                    },
                    'quoted': [ 'rule' ],
                    'policytype': 'authentication radiuspolicy'
                },
                'tacacspolicy': {
                    'attrs': { 
                        'rule': "",
                        'action': ""
                    },
                    'quoted': [ 'rule' ],
                    'policytype': 'authentication tacacspolicy'
                }
            }
        }
        if version is None:
            self._version = '12.0'
        else:
            self._version = version
        if poltype not in self.attr[self._version]:
            raise KeyError("Policy type {} not implemented".format(poltype))
        self._objecttype = poltype
        self.InitVersion()
        self.name = name
        if Attributes is not None:
            for x in Attributes:
                self.Attributes[x] = Attributes[x]
        self._locked = True

    def InitVersion(self):
        self.__dict__['Attributes'] = \
            AttributeList(self.attr[self._version][self._objecttype]['attrs'])
        for x in self.attr[self._version][self._objecttype]['quoted']:
            self.Attributes[x].setquoted(True)

    def LocalAttributes(self):
        outstring  = " \"name\": {}, ".format(json.dumps(self.name))
        return outstring

    def __str__(self):
        outstring = "add {} {} {}".format(self.attr[self._version][self._objecttype]['policytype'] , \
            self.name, str(self.Attributes))
            
        return outstring
