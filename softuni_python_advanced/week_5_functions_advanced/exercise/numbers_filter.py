def even_odd_filter(**kwargs):

    if 'even' in kwargs.keys():
        kwargs['even'] = [n for n in kwargs['even'] if n % 2 == 0]

    if 'odd' in kwargs.keys():
        kwargs['odd'] = [n for n in kwargs['odd'] if n % 2 != 0]

    return dict(sorted(kwargs.items(), key=lambda x: -len(x[1])))

print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))

