# Define a list with elements
my_list = [5, 10, 15]

# Define variables
a = 5
b = 10

# Check if 'a' is in the list
if a in my_list:
    print("Element is in List")

# Check if 'b' is not in the list
if b not in my_list:
    print("Element is not in List")

# SLICING USING : and ::

#### LIST
x = range(1, 10)
print ("FIRST THREE ELEMENTS", x[:3])
print ("THREE ELEMENTS STARTING FROM INDEX 3 to 6", x[3:6])
print ("LAST 3 ELEMENTS", x[-3:])
print ("ALL ELEMENTS EXCEPT THE LAST ELEMENT", x[:-1])


#### TUPLE
x = tuple(x)
print ("FIRST THREE ELEMENTS", x[:3])
print ("THREE ELEMENTS STARTING FROM INDEX 3 to 6", x[3:6])
print ("LAST 3 ELEMENTS", x[-3:])
print ("ALL ELEMENTS EXCEPT THE LAST ELEMENT", x[:-1])


#### STRING
x = 'My name is Anup'
print ("FIRST THREE CHARACTERS", x[:3])
print ("THREE CHARACTERS STARTING FROM INDEX 3 to 6", x[3:6])
print ("LAST 4 CHARACTERS", x[-4:])
print ("ALL CHARACTERS EXCEPT THE LAST ELEMENT", x[:-1])

