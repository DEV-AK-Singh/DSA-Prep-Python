# def add(x, y):
#     print("Using add(x, y)")
#     return x + y
# print(add(1, 2))

# def add(x, y, z):
#     print("Using add(x, y, z)")
#     return x + y + z
# print(add(1, 2, 3))

# cube = lambda x: x**3
# print(cube(3))

# add = lambda x, y: x + y
# print(add(1, 2))

# def add(*args):
#     print("Using add(*args)")
#     return sum(args)
# print(add(1, 2))    
# print(add(1, 2, 3, 4, 5))

# def keyword_args(**kwargs):
#     print(kwargs)
# keyword_args(a=1, b=2, c=3)
# keyword_args(a=1, b=2, c=3, d=4, e=5)

# def yield_func(n):
#     for i in range(n):
#         yield i
# for i in yield_func(5):
#     print(i)

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)
print(fact(5))