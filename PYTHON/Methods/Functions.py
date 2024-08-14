
# Variable declarations
a = 10
b = 15
c = 13
d = 14
e = 8

# Function definitions

## Simple function to print "Hello"
def print_hello():
    """Prints a simple 'Hello' message"""
    print("Hello")

## Function to print a personalized "Hello" message
def print_hello_name(name: str):
    """Prints a personalized 'Hello' message with a name"""
    print(f"Hello, {name}")

## Function to calculate the sum of two numbers
def sum_numbers(a: int, b: int) -> int:
    """Returns the sum of two numbers"""
    return a + b

## Function to demonstrate local variables
def print_local_x():
    """Prints a local variable x"""
    x = 20
    print("Local X:", x)

## Function to demonstrate global variables
def print_global_x():
    """Prints a global variable x"""
    global x
    x = 20
    print("Global X:", x)

## Function to calculate the power of a number
def power(num: int, pow: int = 1) -> int:
    """Returns the power of a number"""
    return num ** pow

## Function to demonstrate nested functions
def mul_add(a: int, b: int, c: int) -> int:
    """Returns the result of a nested function"""
    def mul(x: int, y: int) -> int:
        """Returns the product of two numbers"""
        return x * y
    e = a + b
    return mul(e, c)

# Function calls
print("THE METHOD CALLING::")
print_hello()

print("THE METHOD WITH ARGUMENT")
print_hello_name('Anup')

print("METHOD WITH RETURN")
result = sum_numbers(10, 15)
print("Result:", result)

print("LOCAL X", 10)
print_local_x()
print("X", 10)

print("GLOBAL X", 10)
print_global_x()
print("X", 20)

print(":CALLING WITH POWER")
pow1 = power(2, 3)
print("pow1:", pow1)

print(":CALLING WITHOUT POWER")
pow2 = power(5)
print("pow2:", pow2)

print("MAIN FUNCTION CALLED")
result = mul_add(2, 5, 6)
print("RESULT OF NESTED FUNCTION", result)

