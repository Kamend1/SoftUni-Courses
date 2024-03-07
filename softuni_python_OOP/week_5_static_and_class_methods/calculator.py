class Calculator:

    @staticmethod
    def add(*args):
        args = [x for x in args]
        result = args[0]
        for arg in args[1:]:
            result += arg
        return result

    @staticmethod
    def multiply(*args):
        args = [x for x in args]
        result = args[0]
        for arg in args[1:]:
            result *= arg
        return result

    @staticmethod
    def divide(*args):
        args = [x for x in args]
        result = args[0]
        for arg in args[1:]:
            if arg != 0:
                result /= arg
        return result

    @staticmethod
    def subtract(*args):
        args = [x for x in args]
        result = args[0]
        for arg in args[1:]:
            result -= arg
        return result
