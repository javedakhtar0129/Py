'''
We can use unpackig in lists also
'''
coordinates = (1,2,3,4,5)
# this is one method of using elements of tuples when...
# ..needed to be used in different places
a = coordinates[0]
b = coordinates[1]
c = coordinates[2]
d = coordinates[3]
e = coordinates[4]
# But there is one more method
a, b, c, d, e = coordinates
print(d)

