# Get an initial value for x
x = 10
print(f"The initial value of x is {x}")

# Ask the user for a new value
user_input = input("Please enter a new value: ")

# Print the user's input and its type
print(f"You entered: {user_input} ({type(user_input).__name__})")



# pickle

import pickle

# Define some variables
x = 10
y = 4.5
z = 'help'
a = [1, 2, 3]
b = (4, 5, 6)
c = {'a': 1, 'b': 2, 'c': 3}

# Open a file in binary write mode
with open('my_file.data', 'wb') as f1:
    pickle.dump(x, f1)
    pickle.dump(y, f1)
    pickle.dump(z, f1)
    pickle.dump(a, f1)
    pickle.dump(b, f1)
    pickle.dump(c, f1)

# Delete the variables
del x
del y
del z
del a
del b
del c

# Open the file in binary read mode
with open('my_file.data', 'rb') as f2:
    new_x = pickle.load(f2)
    print("The Variable x", new_x, type(new_x))
    new_y = pickle.load(f2)
    print("The Variable y", new_y, type(new_y))
    new_z = pickle.load(f2)
    print("The Variable z", new_z, type(new_z))
    new_a = pickle.load(f2)
    print("The Variable a", new_a, type(new_a))
    new_b = pickle.load(f2)
    print("The Variable b", new_b, type(new_b))
    new_c = pickle.load(f2)
    print("The Variable c", new_c, type(new_c))

# Define a class
class DumpClass(object):
    def __init__(self):
        self.a = 10

    def print_my_data(self):
        print("DUMPED CLASS DATA", self.a)

# Create an instance of the class
dump_obj = DumpClass()

# Open the file in binary write mode to dump the object
with open('my_class_data.data', 'wb') as f3:
    pickle.dump(dump_obj, f3)

# Delete the object
del dump_obj

# Reopen the file in binary read mode to load the dumped object
with open('my_class_data.data', 'rb') as f4:
    # Load the dumped object into a new variable
    new_dump_obj = pickle.load(f4)

# Use the class's method using the newly loaded object
new_dump_obj.print_my_data()

# Use the class's variable using the object
print(new_dump_obj.a)



