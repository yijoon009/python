def star(func):
    def inner(*args, **kwrds):
        print(args[1] * 30)
        func(*args, **kwrds)
        print(args[1] * 30)
    return inner

@star
def printer(msg, mark):
    print(msg)

printer('hello', '^')