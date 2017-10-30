

class NSObject:
    _locked = False
    _objecttype = 'None'
    def __getitem__(self, name):
        if name in self.__dict__: return self.__dict__[name]
        return self.Attributes[name]

    def __getattr__(self, name):
        return self.__getitem__(name)

    def __setitem__(self, name, value):
        if name == '_locked' or not self._locked:
            self.__dict__[name] = value
        else: self.__dict__['Attributes'][name] = value
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