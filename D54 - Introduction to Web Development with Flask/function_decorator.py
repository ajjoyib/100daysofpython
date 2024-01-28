import time

current_time = time.time()
print(current_time)


def timer(print_result=True):
    def speed_calc_decorator(function):
        def wrapper_function(*args, **kwargs):
            start_time = time.time()
            result = function(*args, **kwargs)
            end_time = time.time()
            duration = end_time - start_time

            if print_result:
                print(f"{function.__name__} run speed: {duration}s")
            return result

        return wrapper_function

    return speed_calc_decorator


# noinspection PyStatementEffect
@timer()
def fast_function():
    for i in range(1000000):
        i * i


# noinspection PyStatementEffect
@timer()
def slow_function():
    for i in range(10000000):
        i * i


@timer(print_result=False)
def another_function():
    time.sleep(2)
    print("Function executed")


fast_function()
slow_function()
another_function()
