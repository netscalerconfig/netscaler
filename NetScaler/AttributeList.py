import json
from . import Attribute

class AttributeList:
    def __init__(self, attributes):
        if isinstance(attributes, dict):
            self._list = {}
            for key in attributes:
                self._list[key] = Attribute(key, attributes[key])
        else:
            raise AttributeError("Cannot initialize an attribute list without attributes")

    def setquote(self, key, q):
        self[key].quoted(q)

    def __setattr__(self, name, value):
        if name == '_list':
            self.__dict__['_list'] = value
        else:
            self.__setitem__(name, value)

    def __getattr__(self, name):
        if name == "_list": return self._list
        return self.__getitem__(name)

    def __setitem__(self, name, value):
        if name not in self._list:
            raise AttributeError("Attribute {} doesn't exist".format(name))
        self._list[name].val = value

    def __getitem__(self, name):
        if name not in self._list:
            raise AttributeError("Attribute {} doesn't exist".format(name))
        return self._list[name]

    def __repr__(self):
        out = "{ "
        first = True
        for x in self._list:
            if first: first = False
            else: out += ", "
            out += "{}: {}".format(json.dumps(x), self._list[x].__repr__())
        out += " }"
        return out

    def __str__(self):
        out = ""
        for x in self._list:
            out += str(self._list[x])
        return out

    def __len__(self):
        return len(self._list)

    def __iter__(self):
        for x in self._list:
            yield x

    def __eq__(self, other):
        for x in other:
            if self._list[x] != other[x]: return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)
