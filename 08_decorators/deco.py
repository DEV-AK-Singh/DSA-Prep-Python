import time

# def timer(func):
#     def inner():
#         start = time.time()
#         func()
#         end = time.time()
#         print(end - start)
#     return inner

# @timer
# def my_func():
#     for i in range(1000000):
#         pass

# my_func()    

# def debugger(func):
#     def inner(*args, **kwargs): 
#         print(f"{func.__name__} was called with {args} and {kwargs}")
#         return func(*args, **kwargs)
#     return inner

# @debugger
# def greet(name, age=20):
#     print(f"Hello {name}")

# greet("Rajesh")

def cache(func):
    cache = {}
    def inner(*args, **kwargs):
        if args in cache:
            return cache[args]
        else:
            result = func(*args, **kwargs)
            cache[args] = result
            return result
    return inner

def long_process(func):
    def inner(*args, **kwargs):
        time.sleep(5) 
        return func(*args, **kwargs) 
    return inner

@cache
@long_process
def add(x, y):
    return x + y

print(add(1, 2))
print(add(1, 2))
print(add(4, 6))