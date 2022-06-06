import mimetypes

class Attribute:
    def __init__(self, name, type, address=0) -> None:
        self.name = name
        self.type = type
        self.address = address

    def __str__(self) -> str:
        return self.name + self.type 
    
    # def __repr__(self) -> str:
    #     return self.__str__


class ClassEntry:

    def __init__(self, name) -> None:
        self.name = name
        self.attributes = {}
        self.int_count = 0
        self.float_count = 0
        self.string_count = 0

    def has_attribute(self, name):
        return name in self.attributes

    def get_attribute(self, name):
        return self.attributes[name]

    def add_attribute(self, attr: Attribute):
        self.attributes[attr.name] = attr

    def increment_type_count(self, t, n):
        if t == 'int':
            self.int_count += n
        elif t == 'float':
            self.float_count += n
        elif t == 'string':
            self.string_count += n


class ClassDirectory:

    def __init__(self) -> None:
        self.table = {}

    
    # inserta una clase en el directorio
    def add_class(self, c : ClassEntry):
        self.table[c.name] = c 
        pass


    # revisa sin existe una clase 
    def has_class(self, name):
        return name in self.table


    def get_class(self, name):
        return self.table[name]


    def print(self):
        print("jaja")
        for c in self.table:
            print("c", c)
            print(self.table[c].__dict__)