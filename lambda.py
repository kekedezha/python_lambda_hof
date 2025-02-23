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
# High Order Functions: a function that contains other functions as parameters
# or returns a function as an output
#######################

def funcBuilder(x):
    return lambda num: num + x

add_ten = funcBuilder(10)
add_twenty = funcBuilder(20)

print(add_ten(7))
print(add_twenty(7))

########################

# Map function

numbers = [3, 7, 12, 18, 20, 21]

squared_nums = map(lambda num: num * num, numbers)

print(list(squared_nums))

###############################

# Filter function

odd_nums = filter(lambda num: num % 2 != 0, numbers)

print(list(odd_nums))

###############################

# Reduce Function 
numbers = [1, 2, 3, 4, 5, 1]

total = reduce(lambda acc, curr: acc + curr, numbers, 10)

print(total)

print(sum(numbers, 10))


names = ['Dave Gray', 'Sara Ito', 'John Jacob Jingleheimerschmidt']

char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)

print(char_count)