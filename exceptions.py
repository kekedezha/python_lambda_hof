# In Python, there are several built-in Python exceptions that can be raised when an error occurs during the execution of a program.
# Different types include: SyntaxError, TypeError, NameError, IndexError, KeyError, ValueError, AttributeError, IOError, ZeroDivisionError, ImportError, etc. 

# Create an exception class and pass Exception as a parameter
class JustNotCoolError(Exception):
    pass

x = 2
try:
    raise JustNotCoolError("This just isn't cool, man.")
    # raise Exception("I'm a custom exception!")
    # print(x / 0)
    # if not type(x) is str:
    #     raise TypeError("Only strings are allowed.")
except NameError:
    print('NameError means something is probably undefined.')
except ZeroDivisionError:
    print('Please do not divide by zero.')
except Exception as error:
    print(error)
else:
    print('No errors!')
finally:
    print("I'm going to print with or without an error.")