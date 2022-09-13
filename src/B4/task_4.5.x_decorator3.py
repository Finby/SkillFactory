# wrap function with time execution decorator
import time


def timing_decorator(function_name):
    def wrap_function(*args):
        t1 = time.time()
        result = function_name(*args)
        dt = time.time() - t1
        print(f'Result is {result}, time spent to run {function_name} is {dt}')
        return result

    return wrap_function


def hashing_decorator(function_name):
    hash_dict = {}
    hits = 0
    new = 0

    def wrap_function(*args):
        nonlocal hash_dict
        nonlocal hits
        nonlocal new
        if args in hash_dict:
            result = hash_dict[args]
            hits += 1
        else:
            result = function_name(*args)
            hash_dict[args] = result
            new += 1
        # print(f'new {new}, hits {hits}')
        return result

    return wrap_function


@timing_decorator
def fib_n(n):
    return fibinachi(n)


@timing_decorator
def fin_n_caching(n):
    return fibinachi(n)

@hashing_decorator
def fibinachi(n):
    if n == 0:
        return 0
    elif n in (1, 2):
        return 1
    else:
        return fibinachi(n-1) + fibinachi(n-2)


fn = int(input('enter Fibonachi number: '))
# fib_n(fn)
fin_n_caching(fn)
