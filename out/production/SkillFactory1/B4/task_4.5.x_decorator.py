# decoratotr to show execution time
import time


def decorate_function(function_name):
    def wrapped():
        t0 = time.time()
        for _ in range(100000):
            result = function_name()
        t1 = time.time()
        dt = t1 - t0
        print(f'function {function_name} executed {dt:.20f}')
        return dt
    return wrapped


def pow_2(n=9):
    return n ** 2


def default_pow_2(n=9):
    return pow(n, 2)


wrapped_pow_2 = decorate_function(pow_2)
wrapped_default_pow_2 = decorate_function(default_pow_2)

print(wrapped_pow_2() - wrapped_default_pow_2())