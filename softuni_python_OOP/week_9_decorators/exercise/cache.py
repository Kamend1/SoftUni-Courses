def cache(func):
    log = {}

    def wrapper(param):
        nonlocal log
        wrapper.log = log
        if param not in log:  # Check if the result for the current parameter is already cached
            log[param] = func(param)  # Compute and cache the result
        return log[param]  # Return the cached result

    return wrapper


@cache
def fibonacci(n):

    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(3)
print(fibonacci.log)
