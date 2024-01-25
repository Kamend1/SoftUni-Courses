from collections import deque

def math_operations(*args, **kwargs):
    floats = deque(args)
    operations = deque(kwargs.keys())

    while floats:
        operator = operations.popleft()
        float_num = floats.popleft()
        if operator == 'a':
            kwargs['a'] += float_num
        elif operator == 's':
            kwargs['s'] -= float_num
        elif operator == 'd':
            if float_num != 0:
                kwargs['d'] /= float_num
        elif operator == 'm':
            kwargs['m'] *= float_num
        operations.append(operator)

    sorted_kwargs = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))

    result = '\n'.join(f"{k}: {v:.1f}" for k, v in sorted_kwargs)

    return result

print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))