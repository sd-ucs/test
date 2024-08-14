# try - except Avoiding the errors which crash the system
x = [1, 2, 3]
try:
 print (x[3])
except:
 print ("Element is not in list, Please select a proper index!")


#  using try except displaying the system error as print not as an error
x = [1, 2, 3]
try:
    print(x[3])
except Exception as e:
    print("Error:", e)


x = [1, 2, 3]
try:
    print(x[2])
except IndexError:
    print("Invalid Index!")
else:
    print("Successful!")



x = [1, 2, 3]
try:
    print(x[2])
except IndexError:
    print("Invalid Index!")
else:
    print("Successful!")
finally:
    print("This will always be called!")


# user defined

class MyException(Exception):
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return "MY Exception: " + str(self.value)

# Example usage with try-except
my_list = [15.0, 25.5, 37.3, 45.2]
try:
    print(my_list[3])
except IndexError:
    raise MyException("You must enter five elements!")
finally:
    print("::The Cleanup has been done!")

# Example usage without try-except
if len(my_list) < 5:
    raise MyException('The list should have at least five elements!')
