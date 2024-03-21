class store_results:
    _logfile = 'results.txt'

    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        result = self.func(*args)

        log_string = "Function '" + self.func.__name__ + "' was called. Result: " + str(result)

        with open(self._logfile, 'a') as opened_file:
            opened_file.write(log_string + '\n')
        return self.func(*args)

@store_results
def add(a, b):
    return a + b

@store_results
def mult(a, b):
    return a * b

add(2, 2)
mult(6, 4)
