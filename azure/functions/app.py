class AzureFunctionApp():
    functions = {}

    @classmethod
    def http_decorator(cls, function_id=None, name=None, bindings=None):
        print("Making the decorator, passing the args")

        def decorator(function):
            print("Here are the args inside of the decorator:", function_id, name, bindings)
            new_func = [name, bindings]
            cls.functions[function_id] = new_func
            return function
        return decorator