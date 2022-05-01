

def print_vars_from_table(table):
    for x in table.table:
        print(table.table[x].__dict__)


# Hasta ahorita solo tienen estos atributos
# para los arreglos y clases tendremos que anadir mas cosas
# pero por mientras con esto
class VariableContext:
    def __init__(self, name, type, scope, address):
        self.name = name
        self.type = type
        self.scope = scope
        self.address = address



class VarsTable:

    def __init__(self):
        self.table = {}

    # inserta variable en la table
    def insert_var(self, var : VariableContext):
        # no hace falta validar si existe la variable
        # porque ya se verificó antes (supuestamente)
        if var.name in self.table:
            return  False
        self.table[var.name] = var
        return True

    # regresa toda la info de la variable, None si no
    def search_var(self, name):
        if name in self.table:
            return self.table[name]
        return None

    # regresa booleano si existe la variable
    def has_var(self, name):
        return name in self.table






# tests
if __name__ == "__main__":
    table = VarsTable()

    var = VariableContext("x", "int", "global", 100)


    table.insert_var(var)
    var = VariableContext("y", "string", "local", 150)
    table.insert_var(var)


    print(table.__dict__)
    print_vars_from_table(table)

