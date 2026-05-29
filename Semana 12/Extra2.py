from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def get_role (self):
        pass
    
    @abstractmethod
    def has_permission(self, permission):
        pass

class AdminUser(User):
    def __init__(self, name):
        super().__init__(name)
        self._access = ("read", "write", "delete", "execute") 

    def get_role (self):
        return f'Admin'
    
    def has_permission(self, permission):
        if permission in self._access:
            return True
        else:
            return False
    
class RegularUser(User):
    def __init__(self, name):
        super().__init__(name)
        self._access = ("read",) 

    def get_role (self):
        return f'Regular'
    
    def has_permission(self, permission):
        if permission in self._access:
            return True
        else:
            return False

user1 = AdminUser("Nicole")
user2 = RegularUser("Andrea")
print(user1.get_role())
print(user2.get_role())

print(user1.has_permission("execute"))
print(user2.has_permission("write"))
