import json

class Attribute:
    def __init__(self, key, default_value, quoted=False):
        self.key = key
        self.default_value = default_value
        self.changed = False
        self.val = default_value
        self.quoted = quoted
        self._locked = True

    def setquoted(self, q):
        self.__dict__['quoted'] = q

    def __setattr__(self, name, value):
        if self.__dict__.get('_locked'):
            if name == 'val':
                self.__dict__[name] = value
                self.__dict__['changed'] = (value != self.__dict__['default_value'])
            elif name == 'quoted': self.quoted = value
            else:
                raise AttributeError, "Attribute does not allow assignment to .{} member".format(name)
        self.__dict__[name] = value

    def __str__(self):
        if self.changed:
            if self.quoted: val = json.dumps(self.val)
            else: val = self.val
            return "-{} {} ".format(self.key, val)
        return ""

    def __repr__(self):
        return str({ \
            "key": self.key, \
            "default_value": self.default_value, \
            "changed": self.changed, \
            "quoted": self.quoted, \
            "val": self.val \
        })

    def __eq__(self, other):
        if 'key' not in other or self.key != other['key']: return False
        if 'default_value' not in other or self.default_value != other['default_value']: return False
        if 'changed' not in other or self.changed != other['changed']: return False
        if 'val' not in other or self.val != other['val']: return False
        if 'quoted' not in other or self.quoted != other['quoted']: return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)