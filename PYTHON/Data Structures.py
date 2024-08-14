# LIST DEFINITIONS
## HOMOGENEOUS LISTS

# Define lists with descriptive variable names
numbers = [1, 2, 3, 4, 5, 6]
float_numbers = [1.2, 3.5, 4.6, 2.6]
letters = ['a', 'b', 'c', 'd']
words = ['help', 'run']

# Print list information
print("Numbers:", numbers, type(numbers))
print("Float Numbers:", float_numbers, type(float_numbers))
print("Letters:", letters, type(letters))
print("Words:", words, type(words))

## HETEROGENOUS LIST
mixed_list = [1, 2.5, 's', 5, 'f', 4.5, 'run']
print("Mixed List:", mixed_list, type(mixed_list))

# → LIST FUNCTIONS
# Append an element to the list
numbers.append(7)
print("Appended Element:", numbers)

# Remove the last element from the list
numbers.pop()
print("Popped Element:", numbers)

# Remove the element at index 2
numbers.pop(2)
print("Popped Second Element:", numbers)

# Remove the first occurrence of 5 from the list
numbers.remove(5)
print("Removed 5 from List:", numbers)

# Define a new list
new_numbers = [11, 12, 13]

# Note: lists do not have an `add` method, use `extend` instead
numbers.extend(new_numbers)
print("Extended List:", numbers)

# Alternatively, use the `+` operator to concatenate lists
combined_list = numbers + new_numbers
print("Combined List:", combined_list)



# TUPLE DEFINITIONS
#### HOMOGENEOUS TUPLE
my_tuple = (1, 3, 5, 2, 4, 8, 9)

#### HETEROGENEOUS TUPLE
your_tuple = (3, 4.5, 5, 6, 7, 'help')

# TUPLE FUNCTIONS
#### LIST ALL METHODS AND ATTRIBUTES OF TUPLE
print(dir(my_tuple))  # Use parentheses instead of no arguments

# Tuples are immutable, so you can't use the `add` method.
# Instead, use the `+` operator to concatenate tuples.
new_tuple = my_tuple + your_tuple
print("NEW TUPLE", new_tuple)

new_tuple1 = my_tuple + your_tuple
print ("NEW TUPLE1", new_tuple1)
print ("MY TUPLE", my_tuple)
print ("COUNT OF ELEMENT 3 IN NEW TUPLE", new_tuple.count(3))
print ("INDEX OF ELEMENT 5 IN NEW TUPLE", new_tuple.index(5))

x = [1, 2, 3, 4, 5, 6, 7]
x_tuple = tuple(x)
print ("LIST CONVERTED TO TUPLE", x_tuple)
x_list = list(x_tuple)
print ("TUPLE CONVERTED TO LIST", x_list)



#  DICTIONARY DEFINITION
trans_dict = {'one':'wahed', 'two':'itnen', 'three':'talata'}
print ("VALUE OF KEY 'one' IS", trans_dict['one'])

# → DICTIONARY UPDATIONS
trans_dict['four'] = 'arba'
print ("ADDED KEY-VAL PAIR FOR FOUR IN DICTIONARY", trans_dict)

del trans_dict['four']
print ("DELETED THE PAIR HAVING THE KEY 'four'", trans_dict)

new_dict = {'a':[1, 2, 3, 'a', (15, 643), 'x']}
print ("ACCESS VALUES IN ITERABLES RECURSIVELY",new_dict['a'][4][0])


# → STRINGS DEFINITIONS
strx = 'HELLO'
print ("STRING", strx)
stry = 'H'
print ("STRING",stry)
strz = ''
print ("STRING",strz)

# → STRING OPERATIONS
strw = strx + stry
print ("CONCAT TWO STRINGS", strw)

# PRINTS ALL STRING FUNCTIONS AND ATTRIBUTES
print (dir(strx))

# Set function
strx = 'anup'
res = strx.capitalize()
print("MAKE THE FIRST CHAR CAPITAL", res)

strx = 'HELPING HAND HAS NO BARS'
count = strx.count('H')
print("Count of H in the string is", count)

res = strx.startswith('HELP')
print("STARTSWITH", res)

res = strx.endswith('RS')
print("ENDSWITH", res)

strx = 'HOW WILL I FIND 1 MY STRING INSIDE A STRING 2'
result = strx.find('STRING')
print("SUBSTRING FIND FROM LEFT", result)

result = strx.rfind('STR')
print("SUBSTRING FIND FROM RIGHT", result)


indx = strx.index('R')
print("INDEX OF R", indx)

rindx = strx.rindex('R')
print("INDEX OF R FROM RIGHT", rindx)


strx = 'H1B4C2CC'
alnum = strx.isalnum()
print("IS STRING ALPHANUMERIC?", alnum)

al = strx.isalpha()
print("IS STRING ALPHABETIC?", al)

num = strx.isdigit()
print("IS STRING NUMERIC OR HAVING ALL DIGITS?", num)

upper = strx.isupper()
print("IS THE STRING IN UPPERCASE?", upper)

lower = strx.islower()
print("IS THE STRING IN LOWERCASE?", lower)

space = strx.isspace()
print("IS THE STRING HAVING ONLY SPACE?", space)


x = 'Help me out with split and join.\nSure,how can I help you?'
split_list = x.split(' ')
print("SPLIT LIST FROM STRING", split_list)

rsplit_list = x.rsplit(' ', 3)
print("RIGHT SPLIT LIST FROM STRING", rsplit_list)

split_line = x.splitlines(2)
print("SPLIT LINE", split_line)

join_str = ','.join(split_list)
print("JOIN STRING FROM THE LIST OF STRINGS", join_str)

# SET DEFINITION
x = range(1, 6)
y = range(3, 9)
set_x = set(x)
set_y = set(y)

# PRINTS ALL SET FUNCTIONS AND ATTRIBUTES
print (dir(set_x))




