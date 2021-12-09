course = "Python's course for beginners"
# strings can be used as arrays here
print(course[0] + course[12])
# negative index will print the last element of the string
print(course[-1] + course[-12])
# num1:num2 will print will print from num1 to excluding num2
print(course[0:3])
print(course[0:])
print(course[:12])
print(course[:])  # this print the whole string
print(course[1:-1])

XYZ = course[:]  # XYZ is now a copy of course

print(XYZ)

