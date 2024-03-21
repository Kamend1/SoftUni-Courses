def make_bold(function):

    def wrapper(*args):
        result = function(*args)
        wrap_result = "<b>" + result + "</b>"
        return wrap_result

    return wrapper


def make_italic(function):
    def wrapper(*args):
        result = function(*args)
        wrap_result = "<i>" + result + "</i>"
        return wrap_result

    return wrapper


def make_underline(function):
    def wrapper(*args):
        result = function(*args)
        wrap_result = "<u>" + result + "</u>"
        return wrap_result

    return wrapper

@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"

print(greet("Peter"))
