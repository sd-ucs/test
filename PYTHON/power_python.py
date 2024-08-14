
# lambda function
def f(x):
    return x ** 2

print(f(8))

g = lambda x: x ** 2
print(g(8))

# inline function
x = [1, 2, 3, 4, 5]
y = [ele * ele for ele in x]
print(y)

# in line for loops with if
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [ele for ele in x if ele % 2 == 0]
print(y)

# using conditional expressions
x = [1]
res = x[0] if x else 0
print(res)

# built in function
z = abs(-10)
print("Absolute Value", z)

# rounding numbers
z = round(10.57689033, 2)
print("Rounding", z)

z = round(19.78363)
print(z)

# using filter 

my_list = [1, 2.0, 3, 4.6, 'd', 6, 7]
z = filter(lambda x: isinstance(x, int), my_list)
print(list(z))

# using map
my_list = [1, 2, 3, 4]
w = map(lambda x: x * x, my_list)
print(list(w))
 
#  using reduce
from functools import reduce

u = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
print(u)

# Assertions and Dynamic Execution
x = 0
assert (x > 0, 'X cannot be zero!')


# Eval
x = eval("{'a':1}")
print(x, type(x))

x = eval("[1,2,3,4,5]")
print(x, type(x))

x = eval("'Anup'")
print(x)

a = 10
x = eval('a')
print(x, type(x))


# Execute a statement
exec('print("Hello")')

# Read and execute code from a file
with open('power_python.py', 'r') as f1:
    x1 = f1.read()
    exec(x1)

