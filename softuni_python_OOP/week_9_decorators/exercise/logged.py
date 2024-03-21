def logged(function):

    def wrapper(*args):
        result = function(*args)
        function_name_str = str(function.__name__)
        function_args = ", ".join(map(str, args))
        log_result = "you called " + function_name_str + "(" + function_args + ")" + '\n' + "it returned " + str(result)
        return log_result

    return wrapper

@logged
def func(*args):
    return 3 + len(args)
print(func(4, 4, 4))

# def logged(function):
#
#     def wrapper(*args):
#         result = function(*args)
#         log_result = f"you called {function.__name__}({", ".join(map(str, args))})\nit returned {result}"
#         return log_result
#
#     return wrapper
#
# @logged
# def func(*args):
#     return 3 + len(args)
# print(func(4, 4, 4))

    
