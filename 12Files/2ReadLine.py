# readline() automatically add \n
# there is also readlines() which
f = open("readline.txt")
result = f.readline()
print(result)
# will now read 3 characters from where
print(f.readline(3))
print(f.readline())  # This will print remaining part of the line

# there is also readlines() which give lines in a list
lines = f.readlines() # this is a list
print(lines)
