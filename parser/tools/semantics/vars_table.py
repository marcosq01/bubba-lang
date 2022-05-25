

def print_vars_from_table(table):
    for x in table.table:
        print(table.table[x].__dict__)


# Hasta ahorita solo tienen estos atributos
# para los arreglos y clases tendremos que anadir mas cosas
# pero por mientras con esto
class VariableContext:
    def __init__(self, name, type, address):
        self.name = name
        self.type = type
        self.address = address
        self.is_array = 0
        self.first_len = 0
        self.second_len = None



class VarsTable:

    def __init__(self):
        self.table = {}

    # inserta variable en la table
    def insert_var(self, var : VariableContext):
        # no hace falta validar si existe la variable
        # porque ya se verificó antes (supuestamente)
        self.table[var.name] = var

    # regresa toda la info de la variable, None si no
    def search_var(self, name):
        if name in self.table:
            return self.table[name]
        return None

    # regresa booleano si existe la variable
    def has_var(self, name):
        return name in self.table

    def print(self):
        for var in self.table:
            v = self.table[var]
            print("nombre_variable:", v.name, "type_variable:", v.type, "address_var:", v.address, "is_array:", v.is_array, "first_len:", v.first_len, "second_len:", v.second_len)
            





# tests
if __name__ == "__main__":
    table = VarsTable()

    var = VariableContext("x", "int", "global", 100)


    table.insert_var(var)
    var = VariableContext("y", "string", "local", 150)
    table.insert_var(var)


    print(table.__dict__)
    print_vars_from_table(table)

