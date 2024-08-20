from functools import reduce

#####################################
# Lambda functions: A lambda function is a small anonymous function.
#   - It can take any number of arguments, but can only have one expression
#####################################
def squared(num): return num * num
# lambda num : num * num

print(squared(2))

def add_two(num): return num + 2
# lambda num : num + 2

print(add_two(12))

def sum_total(a, b): return a + b
# lambda a, b : a + b

print(sum_total(10, 8))

#######################
def funcBuilder(x):
    return lambda num: num + x

add_ten = funcBuilder(10)
add_twenty = funcBuilder(20)

print(add_ten(7))
print(add_twenty(7))

########################