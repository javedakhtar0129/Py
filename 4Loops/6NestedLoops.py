for x in [0,1,2]:
    for y in [4,5,6]:
        print(f"({x},{y})")
print()

# printing F
F = [5,2,5,2,2]
for item in F:
    print(f"{item*'*'}")
print()

# printing F with another way
f = [5,2,5,2,2]
for x_count in f:
    output = ""
    for count in range(x_count):
        output += "x"
    print(output)
print()
