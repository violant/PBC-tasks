def decorator(func):
    def wrapper(*args):
        print(func.__name__ + '('),
        for arg in args:
            print str(arg),
        print (')')
        return func(*args)

    return wrapper
