# Class Definition, Object Creation and Calling a method of class

class my_class:
    def print_hello(self):
        print("Hello")
my_obj = my_class()
my_obj.print_hello()



# Calling the class method inside the class from another method using self

class my_class:
   def print_hello(self):
       print("hello")
   def call_hello(self):
    self.print_hello()
m_obj= my_class()
m_obj.call_hello()


# Constructor, object(Abstract Class)

class Name:
    def __init__(self):
        self.name = 'anup'

    def print_name(self):
        print("My name is", self.name)

n_obj = Name()
n_obj.print_name()

# Parameterized Constructor and calling class methods with class variables using self

class my_name(object):
    def __init__(self, name):
        self.name = name

    def print_name (self):
        print("My name is", self.name)

mn_obj = my_name('anup chavda')
mn_obj.print_name()

# Calling class methods with external parameters

class my_company_name(object):
 def print_my_company_name(self, name):
   print ("My company name is :", name)
mc_obj = my_company_name()
mc_obj.print_my_company_name('Serpent Consulting Services')


# Destructors

class some_class(object):
    def __init__(self):
       print ("object is being created")
    def __del__(self):
          print("object is being deleted")

#  call the constructor
s_obj = some_class()
# call destructor
del s_obj

  # inheritance

class ParentClass:
    def __init__(self):
        print("CONSTRUCTOR CALLED")
        self.a = 10
        self.b = 20

    def my_method(self):
        print("self", self.a)
        print("self", self.b)

    def print_method(self):
        print("print method")


class ChildClass(ParentClass):
    def child_method(self):
        print("child")

    def call_parent_method(self):
        self.my_method()


# Creating an object of child class, also calls the constructor of parent class
child_obj = ChildClass()
# Calling the methods of child class
child_obj.child_method()
# Calling the methods of parent class
child_obj.print_method()
child_obj.call_parent_method()
# Using the member variable of parent class
print(child_obj.a)
print(child_obj.b)



# Overriding methods using super

class MyParent(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add_members(self):
        return self.a + self.b

class MyChild(MyParent):
    def __init__(self, x, y, z):
        # Call the parent constructor using super
        super(MyChild, self).__init__(x, y)
        self.c = z

    def add_members(self):
        # Call the parent method using super
        res = super(MyChild, self).add_members()
        return self.c + res

# Creating an object of MyChild
mch_obj = MyChild(2, 3, 5)

# This will call the overridden method
result = mch_obj.add_members()
print(result)  # Output should be 10

