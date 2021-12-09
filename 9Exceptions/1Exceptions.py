'''
We have three types of errors
1. Compile time error
2. Logical Error
3. Run Time error
We use exceptions for run time error
'''
try:
    age = int(input("Age: "))
    income = 2000
    risk = income/age
    print(age)
except ValueError:
    print("Invalid error has occurred,Enter only integer value! ")
except ZeroDivisionError:
    print("Age cannot be zero!")
finally:
    print("Finally will be printed always")

# exit code 1 means program crashed
