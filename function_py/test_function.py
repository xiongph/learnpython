def func1(arg, x = 0, y = 0):
    return arg * (x**2 + y**2)

def func2(arg, *args):
    for i in args:
        arg += i
    return arg, args

def func3(arg, **args):
    for key, val in args.items():
        arg += val
        print('adding {} sum={}'.format(key, val))
    return arg, args

print(func1(10))
print(func1(10,1))
print(func1(10,1,2))
print(func1(10,y=5))

print(func2(10, 1,2,3,4,5))
x = tuple(range(10))
y = list(range(10))
print(func2(10, *x))
print(func2(10, *y))

print(func3(10, x=1, y=2))
z = {'x':1, 'y':2}
print(func3(10, **z))
print('')



