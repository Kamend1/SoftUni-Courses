def even_odd_filter(**kwargs):
    even = []
    odd = []
    if len(kwargs.keys()) == 1:
        if 'even' in kwargs.keys():
            current_list = kwargs['even']
            for num in current_list:
                if num % 2 == 0:
                    even.append(num)
            kwargs['even'] = even
            return kwargs
        else:
            current_list = kwargs['odd']
            for num in current_list:
                if num % 2 != 0:
                    odd.append(num)
            kwargs['odd'] = odd
            return kwargs
    else:
        for key, values in kwargs.items():
            if key == 'even':
                even = [num for num in values if num % 2 == 0]
            else:
                odd = [num for num in values if num % 2 != 0]

        if even:
            kwargs['even'] = even

        if odd:
            kwargs['odd'] = odd

    return dict(sorted(kwargs.items(), key=lambda x: -len(x[1])))

print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))

