def decorator(func):
    def wrapper(*args):
        print "{}{}".format(func.__name__, '(%s)' % ', '.join(map(repr, args)))
        return func(*args)

    return wrapper
