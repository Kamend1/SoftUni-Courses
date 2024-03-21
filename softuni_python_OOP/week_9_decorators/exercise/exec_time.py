import time

def exec_time(func):

    def wrapper(start, end):
        start_time = time.time()
        result = func(start, end)
        end_time = time.time()
        return end_time - start_time
    return wrapper


@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total
print(loop(1, 10000000))
