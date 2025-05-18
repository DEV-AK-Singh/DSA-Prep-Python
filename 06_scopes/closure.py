def outer_func(x):
    def inner_func(y):
        print(x ** y)
    return inner_func

f = outer_func(2)
f(3)    

g = outer_func(3)
g(3)

h = outer_func(4)
h(3)