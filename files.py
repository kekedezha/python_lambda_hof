# r = Read
# a = Append
# w = Write
# x = Create

# Read - error if it doesn't exist 

f = open("names.txt")

# print(f.read())
# print(f.read(4))
# print(f.readline())
# print(f.readline())

for line in f:
    print(line)

f.close()

# Format for attempting to open a file that may not exist
try:
    f = open("namelist.txt")
    print(f.read())
except:
    print("The file you want to open does not exist.")
finally:
    f.close()