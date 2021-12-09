first = 'John'
second = 'Smith'
ss = 123.32
message = first + " ["+second+ "] is a coder"

# this below is a formatted string
# it starts with f & {} depicts holes where we can put out variables
msg = f"{first} [{second}] is a coder {ss}"

print(message)
print(msg)