#!/usr/bin/env python

def func1():
    print "hello world"

def func2(x, y):
    print "hello world func2, argx: {}, argy: {}".format(x, y)

def func3(x, y, z=10):
    print "hello world func3"
    print "argx: {}, argy: {} argz: {}".format(x, y, z)

def func4(x, y, z):
    return x + y + z

def func5(my_func):
    """Call my_func three times."""
    my_func()
    my_func()
    my_func()

def print_wrapper(header=""):
    if header:
        print "\n"
        print header
        print '-' * 80
    else:
        print '-' * 80

def main():

    ##### Exercise 7A #####
    print_wrapper(header="Exercise 7A")
    func1()
    print_wrapper()

    ##### Exercise 7B #####
    print_wrapper(header="Exercise 7B")
    func2(22, 17)
    print_wrapper()

    ##### Exercise 7C #####
    print_wrapper(header="Exercise 7C")
    func3(22, 17)
    print
    func3(22, 17, 1)
    print
    func3(x=7, y=7, z=3)
    print
    func3(7, z=22, y=9)
    print
    try:
        func3(7, 9, y=8)        # generates exception
    except TypeError:
        print "Handled exception"
    print_wrapper()

    ##### Exercise 7D #####
    print_wrapper(header="Exercise 7D")
    my_args = [3, 4, 5]
    func3(*my_args)
    print_wrapper()

    ##### Exercise 7E #####
    print_wrapper(header="Exercise 7E")
    my_kwargs = {'x': 1, 'y': 2, 'z': 3}
    func3(**my_kwargs)
    print_wrapper()

    ##### Exercise 7F #####
    print_wrapper(header="Exercise 7F")
    return_val = func4(17, 8, 3)
    print return_val
    print
    my_val = func4('hello ', 'world ', 'whatever')
    print my_val
    print_wrapper()

    ##### Exercise 7G #####
    print_wrapper(header="Exercise 7G")
    func5(func1)
    print_wrapper()


if __name__ == "__main__":
    main()
