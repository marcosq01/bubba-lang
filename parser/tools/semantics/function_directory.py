from tools.semantics.vars_table import VariableContext, VarsTable

def print_funcs_from_directory(directory):
    for x in directory.directory:
        print(directory.directory[x].__dict__)


class FunctionContext:
    # TODO anadir el address de la funcion
    def __init__(self, name, type, vars_table) -> None:
        self.name = name
        self.type = type
        self.vars_table = vars_table
        self.signature = []
    
    def get_vars_table(self):
        return self.vars_table
    
    def get_parameters(self):
        return self.signature
    
    def add_parameter(self, p):
        self.signature.append(p)



class FunctionDirectory:

    def __init__(self) -> None:
        self.directory = {}
    
    def insert_function(self, func : FunctionContext):
        # no hace falta validar si existe la funcion
        # porque ya se verificó antes (supuestamente)
        self.directory[func.name] = func

    # regresa booleano si existe o no la funcion
    def has_function(self, func_name):
        return func_name in self.directory

    # regresa toda la info de la funcion
    def search_function(self, func_name):
        if func_name in self.directory:
            return self.directory[func_name]
        else:
            return None
    
    def print(self):
        for f in self.directory:
            print("Funcion:", f, " type:", self.directory[f].type)
            print("Parametros:", self.directory[f].signature)
            # print tabla variables
            self.directory[f].vars_table.print()
            print(" ")


            
if __name__ == "__main__":
    func_dir = FunctionDirectory()

    func_dir.insert_function(FunctionContext("main", "void", None))

    print(func_dir.__dict__)
    print_funcs_from_directory(func_dir)
