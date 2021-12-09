def square(number):
    return number * number


def cube(number):
    print(number ** 3)


result = square(4)
print(result)
print(square(5))  # since there is no concept of void,int

print(cube(9))  # it prints none because there is nothing to return
# to avoid none dont pass it under print
cube(9)
