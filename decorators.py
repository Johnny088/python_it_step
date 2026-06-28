import time

def time_decorator(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        print(f'duration this function: {end- start}')
        return result
    return wrapper

@time_decorator
def timer(secs: int):
    while secs >0:
        print(f'left: {secs} seconds')
        secs -= 1
        time.sleep(1)

# timer = time_decorator(timer)

timer(5)