from tools.semantics.vars_table import VariableContext, VarsTable

def print_funcs_from_directory(directory):
    for x in directory.directory:
        print(directory.directory[x].__dict__)


class FunctionContext:
    def __init__(self, name, type, vars_table) -> None:
        self.name = name
        self.type = type
        self.vars_table = vars_table


class FunctionDirectory:

    def __init__(self) -> None:
        self.directory = {}
    
    def insert_function(self, func : FunctionContext):
        # no hace falta validar si existe la funcion
        # porque ya se verificó antes (supuestamente)
        self.directory[func.name] = func

    # regresa booleano si existe o no la funcion
    def has_function(self, func_name):
        return func_name in self

    # regresa toda la info de la funcion
    def search_function(self, func_name):
        if func_name in self.directory:
            return self.directory[func_name]
        else:
            return None
            
if __name__ == "__main__":
    func_dir = FunctionDirectory()

    func_dir.insert_function(FunctionContext("main", "void", None))

    print(func_dir.__dict__)
    print_funcs_from_directory(func_dir)
