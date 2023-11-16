from collections import UserDict


class LookUpKeyDict(UserDict):
    def lookup_key(self, value):
        self.value = value
        keys = []
        for key in self:
            if self[key] == self.value:
                keys.append(key)
        return keys
            