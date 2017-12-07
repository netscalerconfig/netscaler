import socket

class NSObject:
    _locked = False
    _objecttype = 'None'
    def __getitem__(self, name):
        try:
            if name == 'Attributes': return self.__dict__['Attributes']
            if name in self.__dict__: return self.__dict__[name]
            if name in self.__dict__['Attributes']:
                return self.__dict__['Attributes'][name]
            else:
                raise KeyError("Attribute {} doesn't exist".format(name))
        except:
            raise KeyError("Attribute {} doesn't exist".format(name))

    def __getattr__(self, name):
        return self.__getitem__(name)

    def __setitem__(self, name, value):
        if name == '_locked' or not self._locked:
            self.__dict__[name] = value
        else:
            if name in self.__dict__['Attributes']:
                self.__dict__['Attributes'][name] = value
        return value

    def __setattr__(self, name, value):
        return self.__setitem__(name, value)

    def __repr__(self):
        outstring = "{ "
        outstring += " \"objecttype\": \"{}\", ".format(self._objecttype)
        outstring += self.LocalAttributes()
        outstring += " \"Attributes\": {}".format(self.Attributes.__repr__())
        outstring += " }"
        return outstring

    def LocalAttributes():
        return ""

    def is_ip(self, str):
        try:
            socket.inet_aton(str)
            return True
        except socket.error:
            return False
