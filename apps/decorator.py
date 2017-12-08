def decorator(func):
    def wrapper(*args):
        for arg in args:
            print 'argument: "{}"'.format(arg)
        return func(*args)

    return wrapper
