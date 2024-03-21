def cache(func):

    def wrapper(param):

        if not wrapper.log.get(param):  # Check if the result for the current parameter is already cached
            wrapper.log[param] = func(param)  # Compute and cache the result

        return wrapper.log[param]  # Return the cached result

    wrapper.log = {}

    return wrapper


@cache
def fibonacci(n):

    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(3)
print(fibonacci.log)
