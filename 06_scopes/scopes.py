x = "abhi"
print(x)

def hello():
    x = 10
    print(x)
    print(globals()['x'])

def hello2():
    global x
    x = 20    

hello()
hello2()
print(x)